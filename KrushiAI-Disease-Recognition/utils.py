"""
Advanced Utility Functions for Plant Disease Detection
Contains image processing, model prediction, and analysis functions
"""

import tensorflow as tf
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter
import cv2
import json
import os
import logging
from typing import Tuple, Dict, List, Any

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ImageProcessor:
    """Advanced image processing for plant disease detection"""
    
    def __init__(self, target_size=(128, 128)):
        self.target_size = target_size
        
    def preprocess_image(self, image_path: str, enhance: bool = True) -> np.ndarray:
        """
        Advanced image preprocessing with optional enhancement
        
        Args:
            image_path: Path to the image file
            enhance: Whether to apply image enhancement
            
        Returns:
            Preprocessed image array
        """
        try:
            # Load image
            image = Image.open(image_path)
            
            # Convert to RGB if needed
            if image.mode != 'RGB':
                image = image.convert('RGB')
            
            # Apply enhancements if requested
            if enhance:
                image = self._enhance_image(image)
            
            # Resize image
            image = image.resize(self.target_size, Image.LANCZOS)
            
            # Convert to array and normalize
            image_array = np.array(image, dtype=np.float32)
            image_array = image_array / 255.0
            
            # Add batch dimension
            image_array = np.expand_dims(image_array, axis=0)
            
            return image_array
            
        except Exception as e:
            logger.error(f"Error preprocessing image: {str(e)}")
            raise
    
    def _enhance_image(self, image: Image.Image) -> Image.Image:
        """
        Apply image enhancement techniques
        
        Args:
            image: PIL Image object
            
        Returns:
            Enhanced PIL Image object
        """
        # Enhance contrast
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(1.2)
        
        # Enhance sharpness
        enhancer = ImageEnhance.Sharpness(image)
        image = enhancer.enhance(1.1)
        
        # Enhance color
        enhancer = ImageEnhance.Color(image)
        image = enhancer.enhance(1.1)
        
        return image
    
    def extract_features(self, image_path: str) -> Dict[str, Any]:
        """
        Extract image features for analysis
        
        Args:
            image_path: Path to the image file
            
        Returns:
            Dictionary containing image features
        """
        try:
            # Load image with OpenCV for feature extraction
            img = cv2.imread(image_path)
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            
            # Basic image properties
            height, width, channels = img_rgb.shape
            
            # Color analysis
            mean_color = np.mean(img_rgb, axis=(0, 1))
            std_color = np.std(img_rgb, axis=(0, 1))
            
            # Brightness and contrast
            gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
            brightness = np.mean(gray)
            contrast = np.std(gray)
            
            # Edge density (measure of detail/texture)
            edges = cv2.Canny(gray, 50, 150)
            edge_density = np.sum(edges > 0) / (height * width)
            
            return {
                'dimensions': (width, height),
                'channels': channels,
                'mean_color': mean_color.tolist(),
                'std_color': std_color.tolist(),
                'brightness': float(brightness),
                'contrast': float(contrast),
                'edge_density': float(edge_density),
                'file_size': os.path.getsize(image_path)
            }
            
        except Exception as e:
            logger.error(f"Error extracting features: {str(e)}")
            return {}

class ModelPredictor:
    """Advanced model prediction with confidence analysis"""
    
    def __init__(self, model_path: str):
        self.model_path = model_path
        self.model = None
        self.class_names = [
            'Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
            'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 
            'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 
            'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 
            'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 
            'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot',
            'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 
            'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 
            'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 
            'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 
            'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 
            'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 
            'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus',
            'Tomato___healthy'
        ]
        self.load_model()
    
    def load_model(self):
        """Load the trained model"""
        try:
            self.model = tf.keras.models.load_model(self.model_path)
            logger.info("Model loaded successfully")
        except Exception as e:
            logger.error(f"Error loading model: {str(e)}")
            raise
    
    def predict(self, image_array: np.ndarray) -> Dict[str, Any]:
        """
        Make prediction with confidence analysis
        
        Args:
            image_array: Preprocessed image array
            
        Returns:
            Dictionary containing prediction results
        """
        try:
            # Make prediction
            predictions = self.model.predict(image_array, verbose=0)
            
            # Get probabilities
            probabilities = tf.nn.softmax(predictions[0]).numpy()
            
            # Get top predictions
            top_indices = np.argsort(probabilities)[::-1][:5]
            top_predictions = [
                {
                    'class': self.class_names[idx],
                    'confidence': float(probabilities[idx]),
                    'percentage': float(probabilities[idx] * 100)
                }
                for idx in top_indices
            ]
            
            # Primary prediction
            primary_idx = np.argmax(probabilities)
            primary_prediction = {
                'class': self.class_names[primary_idx],
                'confidence': float(probabilities[primary_idx]),
                'percentage': float(probabilities[primary_idx] * 100)
            }
            
            # Confidence analysis
            confidence_level = self._analyze_confidence(probabilities[primary_idx])
            
            return {
                'primary_prediction': primary_prediction,
                'top_predictions': top_predictions,
                'confidence_level': confidence_level,
                'all_probabilities': probabilities.tolist(),
                'prediction_entropy': float(-np.sum(probabilities * np.log(probabilities + 1e-8)))
            }
            
        except Exception as e:
            logger.error(f"Error making prediction: {str(e)}")
            raise
    
    def _analyze_confidence(self, confidence: float) -> str:
        """
        Analyze confidence level and return descriptive text
        
        Args:
            confidence: Confidence score (0-1)
            
        Returns:
            Confidence level description
        """
        if confidence >= 0.9:
            return "Very High"
        elif confidence >= 0.8:
            return "High"
        elif confidence >= 0.7:
            return "Moderate"
        elif confidence >= 0.6:
            return "Low"
        else:
            return "Very Low"
    
    def batch_predict(self, image_paths: List[str]) -> List[Dict[str, Any]]:
        """
        Make predictions on multiple images
        
        Args:
            image_paths: List of image file paths
            
        Returns:
            List of prediction dictionaries
        """
        results = []
        processor = ImageProcessor()
        
        for image_path in image_paths:
            try:
                image_array = processor.preprocess_image(image_path)
                prediction = self.predict(image_array)
                prediction['image_path'] = image_path
                results.append(prediction)
            except Exception as e:
                logger.error(f"Error predicting {image_path}: {str(e)}")
                results.append({'error': str(e), 'image_path': image_path})
        
        return results

class ModelAnalyzer:
    """Analyze model performance and training history"""
    
    def __init__(self, history_path: str = None):
        self.history_path = history_path
        self.history = None
        if history_path and os.path.exists(history_path):
            self.load_history()
    
    def load_history(self):
        """Load training history from JSON file"""
        try:
            with open(self.history_path, 'r') as f:
                self.history = json.load(f)
            logger.info("Training history loaded successfully")
        except Exception as e:
            logger.error(f"Error loading history: {str(e)}")
    
    def get_training_stats(self) -> Dict[str, Any]:
        """
        Get training statistics
        
        Returns:
            Dictionary containing training statistics
        """
        if not self.history:
            return {}
        
        try:
            epochs = len(self.history['accuracy'])
            final_accuracy = self.history['accuracy'][-1]
            final_val_accuracy = self.history['val_accuracy'][-1]
            final_loss = self.history['loss'][-1]
            final_val_loss = self.history['val_loss'][-1]
            
            best_val_accuracy = max(self.history['val_accuracy'])
            best_val_accuracy_epoch = self.history['val_accuracy'].index(best_val_accuracy) + 1
            
            return {
                'total_epochs': epochs,
                'final_accuracy': round(final_accuracy, 4),
                'final_val_accuracy': round(final_val_accuracy, 4),
                'final_loss': round(final_loss, 4),
                'final_val_loss': round(final_val_loss, 4),
                'best_val_accuracy': round(best_val_accuracy, 4),
                'best_val_accuracy_epoch': best_val_accuracy_epoch,
                'overfitting_indicator': final_accuracy - final_val_accuracy > 0.1
            }
            
        except Exception as e:
            logger.error(f"Error calculating stats: {str(e)}")
            return {}
    
    def get_performance_analysis(self) -> Dict[str, str]:
        """
        Analyze model performance
        
        Returns:
            Dictionary containing performance analysis
        """
        stats = self.get_training_stats()
        if not stats:
            return {'analysis': 'Training history not available'}
        
        analysis = []
        
        # Accuracy analysis
        if stats['final_val_accuracy'] >= 0.95:
            analysis.append("🎯 Excellent model performance with >95% validation accuracy")
        elif stats['final_val_accuracy'] >= 0.90:
            analysis.append("✅ Good model performance with >90% validation accuracy")
        elif stats['final_val_accuracy'] >= 0.80:
            analysis.append("⚠️ Moderate performance - consider additional training")
        else:
            analysis.append("🔴 Low performance - model may need improvement")
        
        # Overfitting analysis
        if stats.get('overfitting_indicator', False):
            analysis.append("📊 Model shows signs of overfitting")
        else:
            analysis.append("📈 Model shows good generalization")
        
        # Best performance
        analysis.append(f"🏆 Best validation accuracy: {stats['best_val_accuracy']:.1%} at epoch {stats['best_val_accuracy_epoch']}")
        
        return {
            'analysis': ' | '.join(analysis),
            'recommendation': self._get_recommendation(stats)
        }
    
    def _get_recommendation(self, stats: Dict[str, Any]) -> str:
        """Get recommendation based on model performance"""
        if stats['final_val_accuracy'] >= 0.95:
            return "Model is performing excellently and ready for deployment."
        elif stats['final_val_accuracy'] >= 0.90:
            return "Good performance. Consider fine-tuning for specific use cases."
        elif stats['final_val_accuracy'] >= 0.80:
            return "Moderate performance. Consider data augmentation or architecture changes."
        else:
            return "Performance needs improvement. Consider more data or model redesign."

def format_disease_name(disease_key: str) -> str:
    """
    Format disease key into readable name
    
    Args:
        disease_key: Raw disease classification key
        
    Returns:
        Formatted disease name
    """
    # Replace underscores with spaces
    formatted = disease_key.replace('___', ' - ').replace('_', ' ')
    
    # Handle special cases
    formatted = formatted.replace('(including sour)', '(Including Sour)')
    formatted = formatted.replace('bell', 'Bell')
    formatted = formatted.replace('maize', 'Maize')
    
    # Capitalize words
    words = formatted.split()
    formatted_words = []
    for word in words:
        if word.lower() in ['and', 'or', 'the', 'of', 'in', 'on', 'at', 'to', 'for']:
            formatted_words.append(word.lower())
        else:
            formatted_words.append(word.capitalize())
    
    return ' '.join(formatted_words)

def get_severity_color(severity: str) -> str:
    """
    Get color code for disease severity
    
    Args:
        severity: Severity level
        
    Returns:
        Color code
    """
    severity_colors = {
        'Critical': '#FF4B4B',  # Red
        'High': '#FF8C42',      # Orange
        'Medium': '#FFD93D',    # Yellow
        'Low': '#6BCF7F',       # Light Green
        'None': '#4CAF50',      # Green
        'Unknown': '#9E9E9E'    # Gray
    }
    return severity_colors.get(severity, '#9E9E9E')

def create_confidence_message(confidence: float, confidence_level: str) -> str:
    """
    Create user-friendly confidence message
    
    Args:
        confidence: Confidence score (0-1)
        confidence_level: Confidence level description
        
    Returns:
        Formatted confidence message
    """
    percentage = confidence * 100
    
    if confidence >= 0.9:
        emoji = "🎯"
        message = f"I'm very confident ({percentage:.1f}%) in this prediction."
    elif confidence >= 0.8:
        emoji = "✅"
        message = f"I'm quite confident ({percentage:.1f}%) in this prediction."
    elif confidence >= 0.7:
        emoji = "👍"
        message = f"I'm moderately confident ({percentage:.1f}%) in this prediction."
    elif confidence >= 0.6:
        emoji = "⚠️"
        message = f"I have low confidence ({percentage:.1f}%) in this prediction."
    else:
        emoji = "🤔"
        message = f"I have very low confidence ({percentage:.1f}%) in this prediction. Consider taking another photo."
    
    return f"{emoji} {message}"