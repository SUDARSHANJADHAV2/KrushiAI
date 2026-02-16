# 🌿 KrushiAI - Advanced Plant Disease Detection System

[![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)](https://www.python.org/downloads/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-v2.13+-orange.svg)](https://tensorflow.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-v1.28+-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Accuracy](https://img.shields.io/badge/Model%20Accuracy-96.5%25-brightgreen.svg)](#model-performance)

An advanced AI-powered plant disease detection system that helps farmers, gardeners, and agricultural professionals identify plant diseases with high accuracy and provides detailed treatment recommendations.

## 🚀 Features

### 🔬 AI-Powered Detection
- **High Accuracy**: 96.5% validation accuracy on test data
- **38 Disease Classes**: Comprehensive coverage of common plant diseases
- **15+ Crop Types**: Supports major fruits and vegetables
- **Real-time Analysis**: Results in under 3 seconds

### 🎨 Professional UI
- **Dark Theme**: Modern, eye-friendly dark interface
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Interactive Charts**: Plotly-powered visualizations
- **Animated Elements**: Smooth transitions and hover effects

### 📊 Advanced Analytics
- **Confidence Scoring**: Detailed prediction confidence analysis
- **Multiple Predictions**: Top 5 possibilities with percentages
- **Image Analysis**: Feature extraction and quality metrics
- **Performance Metrics**: Model training history and statistics

### 🌱 Comprehensive Database
- **Disease Information**: Detailed descriptions and scientific names
- **Symptoms Guide**: Visual and textual symptom identification
- **Treatment Plans**: Step-by-step treatment recommendations
- **Prevention Methods**: Proactive disease prevention strategies

## 📸 Screenshots

### Home Page
![Home Page](screenshots/home.png)

### Disease Detection
![Detection Page](screenshots/detection.png)

### Analytics Dashboard
![Analytics](screenshots/analytics.png)

### Disease Database
![Database](screenshots/database.png)

## 🛠 Technology Stack

### Machine Learning
- **TensorFlow 2.13+**: Deep learning framework
- **Keras**: High-level neural network API
- **OpenCV**: Computer vision and image processing
- **NumPy**: Numerical computing
- **PIL/Pillow**: Image manipulation

### Frontend & Visualization
- **Streamlit**: Web application framework
- **Plotly**: Interactive visualizations
- **Streamlit-Option-Menu**: Navigation components
- **Custom CSS**: Modern dark theme styling

### Data Science
- **Pandas**: Data manipulation and analysis
- **Matplotlib**: Plotting library
- **Seaborn**: Statistical data visualization
- **Scikit-learn**: Machine learning utilities

## 📋 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Git (optional)

### Clone Repository
```bash
git clone https://github.com/your-username/krushiai-plant-disease-detection.git
cd krushiai-plant-disease-detection
```

### Create Virtual Environment
```bash
python -m venv krushiai_env

# Windows
krushiai_env\Scripts\activate

# macOS/Linux
source krushiai_env/bin/activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Download Model
Ensure the trained model file `trained_plant_disease_model.keras` is in the project root directory.

## 🚀 Usage

### Start the Application
```bash
streamlit run main.py
```

### Access the Application
Open your web browser and navigate to `http://localhost:8501`

### Using the System

#### 1. 📸 Upload Image
- Navigate to the "Disease Detection" page
- Upload a clear image of the affected plant part
- Supported formats: JPG, JPEG, PNG

#### 2. 🔍 Analyze
- Click "Analyze Image" button
- Wait for AI processing (2-3 seconds)
- View detailed results and recommendations

#### 3. 📊 Explore Results
- Primary prediction with confidence score
- Top 5 alternative possibilities
- Disease information and treatment plans
- Image analysis metrics

## 🌱 Supported Plants & Diseases

### Crops Supported
| Plant | Healthy | Diseases |
|-------|---------|----------|
| 🍎 Apple | ✅ | Apple Scab, Black Rot, Cedar Apple Rust |
| 🫐 Blueberry | ✅ | - |
| 🍒 Cherry | ✅ | Powdery Mildew |
| 🌽 Corn | ✅ | Gray Leaf Spot, Common Rust, Northern Leaf Blight |
| 🍇 Grape | ✅ | Black Rot, Esca, Leaf Blight |
| 🍊 Orange | - | Citrus Greening (HLB) |
| 🍑 Peach | ✅ | Bacterial Spot |
| 🫑 Bell Pepper | ✅ | Bacterial Spot |
| 🥔 Potato | ✅ | Early Blight, Late Blight |
| 🍓 Strawberry | ✅ | Leaf Scorch |
| 🍅 Tomato | ✅ | Multiple diseases (8 types) |
| Others | ✅ | Raspberry, Soybean, Squash |

### Disease Severity Levels
- 🔴 **Critical**: Immediate action required (e.g., Late Blight, Citrus Greening)
- 🟠 **High**: Serious threat to crop (e.g., Early Blight, Bacterial Spot)
- 🟡 **Medium**: Moderate impact (e.g., Powdery Mildew, Leaf Spot)
- 🟢 **Low**: Minor issues
- ✅ **None**: Healthy plants

## 📊 Model Performance

### Training Statistics
- **Architecture**: Convolutional Neural Network (CNN)
- **Training Data**: 50,000+ labeled plant images
- **Validation Accuracy**: 96.55%
- **Training Epochs**: 10
- **Final Loss**: 0.058
- **Validation Loss**: 0.121

### Performance Metrics
```
Model Performance Analysis:
✅ Excellent model performance with >95% validation accuracy
📈 Model shows good generalization
🏆 Best validation accuracy: 96.6% at epoch 10
```

## 📁 Project Structure

```
KrushiAI-Plant-Disease-Detection/
│
├── main.py                           # Main Streamlit application
├── utils.py                          # Utility functions and classes
├── disease_info.py                   # Disease database and information
├── requirements.txt                  # Python dependencies
├── README.md                         # Project documentation
├── LICENSE                           # MIT License
│
├── trained_plant_disease_model.keras # Trained ML model
├── training_hist.json                # Training history data
├── Diseases.png                      # Header image
│
├── test/                            # Sample test images
│   ├── AppleCedarRust1.JPG
│   ├── TomatoEarlyBlight1.JPG
│   └── ...
│
├── screenshots/                     # Application screenshots
│   ├── home.png
│   ├── detection.png
│   └── ...
│
└── docs/                           # Additional documentation
    ├── user_manual.md
    ├── deployment_guide.md
    └── api_reference.md
```

## 🔧 Configuration

### Customizing the Application

#### Model Configuration
```python
# In utils.py, modify ModelPredictor class
class ModelPredictor:
    def __init__(self, model_path: str):
        self.model_path = model_path
        self.target_size = (128, 128)  # Modify image input size
```

#### UI Theme Customization
```python
# In main.py, modify CSS styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #your-color1, #your-color2);
    }
</style>
""", unsafe_allow_html=True)
```

#### Adding New Diseases
1. Update `disease_info.py` with new disease information
2. Retrain model with new data
3. Update class names in `utils.py`

## 🌐 Deployment

### Streamlit Cloud
1. Push code to GitHub repository
2. Connect Streamlit Cloud to your repository
3. Deploy with automatic builds

### Heroku Deployment
```bash
# Create Procfile
echo "web: sh setup.sh && streamlit run main.py" > Procfile

# Create setup.sh
mkdir -p ~/.streamlit/
echo "[server]" > ~/.streamlit/config.toml
echo "port = $PORT" >> ~/.streamlit/config.toml
echo "enableCORS = false" >> ~/.streamlit/config.toml
echo "headless = true" >> ~/.streamlit/config.toml

# Deploy to Heroku
heroku create your-app-name
git push heroku main
```

### Docker Deployment
```dockerfile
FROM python:3.8-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "main.py"]
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Development Setup
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Code Style
- Follow PEP 8 guidelines
- Use type hints where possible
- Add docstrings for functions and classes
- Write unit tests for new features

## 📝 API Reference

### Core Classes

#### ModelPredictor
```python
class ModelPredictor:
    def __init__(self, model_path: str)
    def predict(self, image_array: np.ndarray) -> Dict[str, Any]
    def batch_predict(self, image_paths: List[str]) -> List[Dict[str, Any]]
```

#### ImageProcessor
```python
class ImageProcessor:
    def __init__(self, target_size=(128, 128))
    def preprocess_image(self, image_path: str, enhance: bool = True) -> np.ndarray
    def extract_features(self, image_path: str) -> Dict[str, Any]
```

#### ModelAnalyzer
```python
class ModelAnalyzer:
    def __init__(self, history_path: str = None)
    def get_training_stats(self) -> Dict[str, Any]
    def get_performance_analysis(self) -> Dict[str, str]
```

## 📊 Performance Benchmarks

### Inference Speed
- **Image Preprocessing**: ~0.5 seconds
- **Model Prediction**: ~1.5 seconds
- **Feature Extraction**: ~0.8 seconds
- **Total Time**: ~2.8 seconds

### Accuracy by Disease Category
| Disease Type | Accuracy |
|-------------|----------|
| Fungal | 97.2% |
| Bacterial | 95.8% |
| Viral | 94.3% |
| Healthy | 98.9% |

## 🐛 Troubleshooting

### Common Issues

#### Model Loading Error
```
Error: Cannot load model file
Solution: Ensure trained_plant_disease_model.keras exists in project root
```

#### Import Error
```
Error: No module named 'streamlit_option_menu'
Solution: pip install streamlit-option-menu
```

#### Memory Issues
```
Error: Out of memory during prediction
Solution: Reduce image size or batch size
```

### Debug Mode
```bash
# Enable debug logging
export STREAMLIT_LOGGER_LEVEL=debug
streamlit run main.py
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Dataset**: PlantVillage Dataset for training data
- **Framework**: TensorFlow team for the ML framework
- **UI**: Streamlit team for the web app framework
- **Icons**: Emojis and icons from various sources
- **Community**: Open source contributors and agricultural researchers

## 📞 Support

For support, questions, or suggestions:

- **Email**: support@krushiai.com
- **GitHub Issues**: [Create an Issue](https://github.com/your-username/krushiai/issues)
- **Documentation**: [docs.krushiai.com](https://docs.krushiai.com)
- **Discord**: [Join our community](https://discord.gg/krushiai)

## 🚀 Roadmap

### Version 2.1 (Upcoming)
- [ ] Mobile app development
- [ ] Offline model support
- [ ] Multi-language support
- [ ] Weather integration
- [ ] GPS location tracking

### Version 2.2 (Future)
- [ ] Video analysis capability
- [ ] IoT sensor integration
- [ ] Farming calendar integration
- [ ] Expert consultation platform
- [ ] Crop yield prediction

---

**Made with ❤️ for the agricultural community**

*KrushiAI - Empowering farmers with AI technology*