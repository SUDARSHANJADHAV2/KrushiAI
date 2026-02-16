#!/usr/bin/env python3
"""
Health Check Script for KrushiAI Deployment
This script checks all dependencies and requirements before the main app starts
"""

import sys
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def check_python_version():
    """Check Python version compatibility"""
    logger.info(f"Python version: {sys.version}")
    if sys.version_info < (3, 8):
        logger.error("Python 3.8+ is required")
        return False
    return True

def check_required_packages():
    """Check if all required packages are available"""
    required_packages = [
        'streamlit', 'numpy', 'pandas', 'matplotlib', 'seaborn',
        'scikit-learn', 'tensorflow', 'PIL', 'plotly', 
        'streamlit_option_menu', 'cv2'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            if package == 'PIL':
                import PIL
            elif package == 'cv2':
                import cv2
            else:
                __import__(package)
            logger.info(f"✓ {package} - Available")
        except ImportError as e:
            logger.error(f"✗ {package} - Missing: {str(e)}")
            missing_packages.append(package)
    
    return len(missing_packages) == 0, missing_packages

def check_model_files():
    """Check if model files exist"""
    model_files = [
        'trained_plant_disease_model.keras',
        'training_hist.json',
        'utils.py',
        'disease_info.py'
    ]
    
    missing_files = []
    
    for file_path in model_files:
        if os.path.exists(file_path):
            logger.info(f"✓ {file_path} - Found")
        else:
            logger.error(f"✗ {file_path} - Missing")
            missing_files.append(file_path)
    
    return len(missing_files) == 0, missing_files

def check_tensorflow_compatibility():
    """Check TensorFlow installation and GPU availability"""
    try:
        import tensorflow as tf
        logger.info(f"TensorFlow version: {tf.__version__}")
        
        # Check if TensorFlow can load
        logger.info("Testing TensorFlow functionality...")
        test_tensor = tf.constant([1, 2, 3])
        logger.info("✓ TensorFlow working correctly")
        
        # Check for GPU (optional)
        gpus = tf.config.list_physical_devices('GPU')
        if gpus:
            logger.info(f"GPU devices available: {len(gpus)}")
        else:
            logger.info("No GPU devices found (CPU mode)")
            
        return True
    except Exception as e:
        logger.error(f"TensorFlow issue: {str(e)}")
        return False

def check_model_loading():
    """Test loading the actual model file"""
    try:
        import tensorflow as tf
        model_path = 'trained_plant_disease_model.keras'
        
        if not os.path.exists(model_path):
            logger.error(f"Model file not found: {model_path}")
            return False
            
        logger.info("Testing model loading...")
        model = tf.keras.models.load_model(model_path)
        logger.info("✓ Model loaded successfully")
        
        # Check model architecture
        logger.info(f"Model input shape: {model.input_shape}")
        logger.info(f"Model output shape: {model.output_shape}")
        
        return True
    except Exception as e:
        logger.error(f"Model loading failed: {str(e)}")
        return False

def check_streamlit_config():
    """Check Streamlit configuration"""
    config_path = '.streamlit/config.toml'
    if os.path.exists(config_path):
        logger.info("✓ Streamlit config found")
        try:
            import toml
            with open(config_path, 'r') as f:
                config = toml.load(f)
            logger.info("✓ Streamlit config valid")
        except:
            logger.warning("Streamlit config may have issues")
    else:
        logger.warning("No Streamlit config found")
    return True

def main():
    """Run all health checks"""
    logger.info("Starting KrushiAI Health Check...")
    
    checks = [
        ("Python Version", check_python_version),
        ("Required Packages", lambda: check_required_packages()[0]),
        ("Model Files", lambda: check_model_files()[0]),
        ("TensorFlow", check_tensorflow_compatibility),
        ("Model Loading", check_model_loading),
        ("Streamlit Config", check_streamlit_config)
    ]
    
    failed_checks = []
    
    for check_name, check_func in checks:
        logger.info(f"\n--- {check_name} Check ---")
        try:
            if check_func():
                logger.info(f"✓ {check_name} - PASSED")
            else:
                logger.error(f"✗ {check_name} - FAILED")
                failed_checks.append(check_name)
        except Exception as e:
            logger.error(f"✗ {check_name} - ERROR: {str(e)}")
            failed_checks.append(check_name)
    
    # Summary
    logger.info(f"\n{'='*50}")
    logger.info("HEALTH CHECK SUMMARY")
    logger.info(f"{'='*50}")
    
    if not failed_checks:
        logger.info("✓ All checks passed! App should work correctly.")
        return True
    else:
        logger.error(f"✗ {len(failed_checks)} checks failed:")
        for check in failed_checks:
            logger.error(f"  - {check}")
        logger.info("Please fix these issues before deployment.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)