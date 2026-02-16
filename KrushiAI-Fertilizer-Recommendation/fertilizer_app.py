import streamlit as st
import pickle
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os
from datetime import datetime

# Page config
st.set_page_config(
    page_title="🌾 KrushiAI - Smart Fertilizer Recommendation",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Dark mode CSS styling
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    /* Main app styling */
    .stApp {
        background: linear-gradient(135deg, #0c0c0c 0%, #1a1a1a 100%);
        color: #ffffff;
        font-family: 'Inter', sans-serif;
    }
    
    /* Header styling */
    .main-header {
        background: linear-gradient(90deg, #2E7D32 0%, #388E3C 50%, #4CAF50 100%);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .main-title {
        font-size: 3rem;
        font-weight: 700;
        color: #ffffff;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        margin-bottom: 0.5rem;
    }
    
    .main-subtitle {
        font-size: 1.2rem;
        color: #E8F5E8;
        font-weight: 300;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #1a1a1a 0%, #2d2d2d 100%);
    }
    
    /* Input styling */
    .stSelectbox > div > div {
        background-color: #2d2d2d;
        border: 1px solid #4CAF50;
        border-radius: 8px;
    }
    
    .stNumberInput > div > div > input {
        background-color: #2d2d2d;
        border: 1px solid #4CAF50;
        border-radius: 8px;
        color: #ffffff;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(45deg, #4CAF50 0%, #45a049 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(76, 175, 80, 0.3);
    }
    
    .stButton > button:hover {
        background: linear-gradient(45deg, #45a049 0%, #4CAF50 100%);
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(76, 175, 80, 0.4);
    }
    
    /* Card styling */
    .metric-card {
        background: linear-gradient(135deg, #2d2d2d 0%, #3d3d3d 100%);
        padding: 1.5rem;
        border-radius: 15px;
        border: 1px solid rgba(76, 175, 80, 0.3);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
        margin: 1rem 0;
    }
    
    /* Success message styling */
    .stSuccess {
        background: linear-gradient(90deg, #4CAF50 0%, #45a049 100%);
        border-radius: 15px;
        border: none;
        box-shadow: 0 4px 20px rgba(76, 175, 80, 0.3);
    }
    
    /* Info box styling */
    .stInfo {
        background: linear-gradient(90deg, #2196F3 0%, #1976D2 100%);
        border-radius: 15px;
        border: none;
    }
    
    /* Warning styling */
    .stWarning {
        background: linear-gradient(90deg, #FF9800 0%, #F57C00 100%);
        border-radius: 15px;
        border: none;
    }
    
    /* Hide streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Custom animations */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .fade-in {
        animation: fadeIn 0.5s ease-in;
    }
</style>
""", unsafe_allow_html=True)

# Helper functions
@st.cache_data
def load_model_components():
    """Load all model components with error handling"""
    try:
        model = pickle.load(open("Fertilizer_RF.pkl", "rb"))
        soil_encoder = pickle.load(open("soil_encoder.pkl", "rb"))
        crop_encoder = pickle.load(open("crop_encoder.pkl", "rb"))
        fertilizer_encoder = pickle.load(open("fertilizer_encoder.pkl", "rb"))
        
        # Load scaler and metrics if available
        try:
            scaler = pickle.load(open("feature_scaler.pkl", "rb"))
            model_metrics = pickle.load(open("model_metrics.pkl", "rb"))
        except:
            scaler = None
            model_metrics = None
            
        return model, soil_encoder, crop_encoder, fertilizer_encoder, scaler, model_metrics
    except Exception as e:
        st.error(f"❌ Error loading model components: {str(e)}")
        return None, None, None, None, None, None

def validate_inputs(temp, humidity, moisture, nitrogen, potassium, phosphorous):
    """Validate user inputs"""
    errors = []
    
    if temp < 0 or temp > 60:
        errors.append("⚠️ Temperature should be between 0°C and 60°C")
    if humidity < 0 or humidity > 100:
        errors.append("⚠️ Humidity should be between 0% and 100%")
    if moisture < 0 or moisture > 100:
        errors.append("⚠️ Soil moisture should be between 0% and 100%")
    if nitrogen < 0 or nitrogen > 300:
        errors.append("⚠️ Nitrogen should be between 0 and 300 mg/kg")
    if potassium < 0 or potassium > 300:
        errors.append("⚠️ Potassium should be between 0 and 300 mg/kg")
    if phosphorous < 0 or phosphorous > 300:
        errors.append("⚠️ Phosphorous should be between 0 and 300 mg/kg")
        
    return errors

def get_fertilizer_info(fertilizer_name):
    """Get detailed information about the recommended fertilizer"""
    fertilizer_info = {
        "Urea": {
            "description": "High nitrogen content fertilizer (46% N)",
            "benefits": ["Promotes leafy growth", "Improves protein content", "Quick nitrogen release"],
            "best_for": ["Cereals", "Leafy vegetables", "Grass crops"],
            "application_rate": "100-200 kg/ha",
            "timing": "Pre-planting and top-dressing"
        },
        "DAP": {
            "description": "Di-ammonium Phosphate (18% N, 46% P₂O₅)",
            "benefits": ["Root development", "Early plant growth", "Flower and fruit formation"],
            "best_for": ["All crops", "Especially during planting"],
            "application_rate": "50-100 kg/ha",
            "timing": "At planting time"
        },
        "14-35-14": {
            "description": "NPK complex fertilizer (14% N, 35% P₂O₅, 14% K₂O)",
            "benefits": ["Balanced nutrition", "Root development", "Overall plant health"],
            "best_for": ["Fruit crops", "Vegetables", "Cash crops"],
            "application_rate": "150-250 kg/ha",
            "timing": "At planting and flowering"
        },
        "28-28": {
            "description": "NPK fertilizer (28% N, 28% P₂O₅)",
            "benefits": ["Balanced N-P nutrition", "Strong root system", "Healthy growth"],
            "best_for": ["Field crops", "Vegetables"],
            "application_rate": "100-150 kg/ha",
            "timing": "At planting and vegetative stage"
        },
        "17-17-17": {
            "description": "Balanced NPK fertilizer (17% each of N, P₂O₅, K₂O)",
            "benefits": ["Complete balanced nutrition", "All-round growth", "Stress tolerance"],
            "best_for": ["All crops", "General purpose"],
            "application_rate": "150-200 kg/ha",
            "timing": "Throughout growing season"
        },
        "20-20": {
            "description": "NPK fertilizer (20% N, 20% P₂O₅)",
            "benefits": ["Good N-P balance", "Vigorous growth", "High yield potential"],
            "best_for": ["Cereals", "Pulses", "Oilseeds"],
            "application_rate": "125-175 kg/ha",
            "timing": "At sowing and top-dressing"
        },
        "10-26-26": {
            "description": "NPK fertilizer (10% N, 26% P₂O₅, 26% K₂O)",
            "benefits": ["High P-K content", "Root development", "Disease resistance"],
            "best_for": ["Fruit crops", "Vegetables", "High K requirement crops"],
            "application_rate": "100-200 kg/ha",
            "timing": "At planting and fruit development"
        }
    }
    
    return fertilizer_info.get(fertilizer_name, {
        "description": "Specialized fertilizer blend",
        "benefits": ["Optimized nutrition", "Improved yield", "Better quality"],
        "best_for": ["As recommended for your specific crop"],
        "application_rate": "As per soil test recommendations",
        "timing": "As per crop growth stage"
    })

# Load model components
model, soil_encoder, crop_encoder, fertilizer_encoder, scaler, model_metrics = load_model_components()

if model is None:
    st.error("❌ Failed to load model components. Please ensure all model files are present.")
    st.stop()

# Header
st.markdown("""
<div class="main-header fade-in">
    <h1 class="main-title">🌾 KrushiAI</h1>
    <p class="main-subtitle">Smart Fertilizer Recommendation System</p>
    <p style="font-size: 0.9rem; opacity: 0.8;">Powered by Machine Learning • Optimized for Indian Agriculture</p>
</div>
""", unsafe_allow_html=True)

# Sidebar for inputs
with st.sidebar:
    st.markdown("### 🌱 Agricultural Input Parameters")
    
    # Environmental factors
    st.markdown("#### 🌤️ Environmental Conditions")
    temp = st.number_input(
        "🌡️ Temperature (°C)", 
        min_value=0.0, max_value=60.0, value=26.0, step=0.5,
        help="Average temperature during crop growth period"
    )
    
    humidity = st.number_input(
        "💧 Humidity (%)", 
        min_value=0.0, max_value=100.0, value=52.0, step=1.0,
        help="Relative humidity percentage"
    )
    
    moisture = st.number_input(
        "🌿 Soil Moisture (%)", 
        min_value=0.0, max_value=100.0, value=38.0, step=1.0,
        help="Soil moisture content percentage"
    )
    
    # Soil and crop selection
    st.markdown("#### 🌱 Crop & Soil Information")
    soil = st.selectbox(
        "🟤 Soil Type", 
        options=soil_encoder.classes_,
        help="Select the predominant soil type in your field"
    )
    
    crop = st.selectbox(
        "🌾 Crop Type", 
        options=crop_encoder.classes_,
        help="Select the crop you want to grow"
    )
    
    # Nutrient levels
    st.markdown("#### 🧪 Soil Nutrient Levels (mg/kg)")
    nitrogen = st.number_input(
        "🔵 Nitrogen (N)", 
        min_value=0.0, max_value=300.0, value=37.0, step=1.0,
        help="Available nitrogen content in soil"
    )
    
    potassium = st.number_input(
        "🟡 Potassium (K)", 
        min_value=0.0, max_value=300.0, value=0.0, step=1.0,
        help="Available potassium content in soil"
    )
    
    phosphorous = st.number_input(
        "🔴 Phosphorous (P)", 
        min_value=0.0, max_value=300.0, value=0.0, step=1.0,
        help="Available phosphorous content in soil"
    )
    
    st.markdown("---")
    
    # Predict button
    predict_button = st.button(
        "🔮 Get Fertilizer Recommendation", 
        help="Click to get AI-powered fertilizer recommendation"
    )

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    # Model information
    if model_metrics:
        st.markdown("### 📊 Model Performance")
        metric_col1, metric_col2, metric_col3 = st.columns(3)
        
        with metric_col1:
            st.metric(
                "Model Accuracy", 
                f"{model_metrics['accuracy']:.1%}",
                help="Overall prediction accuracy on test data"
            )
        
        with metric_col2:
            st.metric(
                "Cross-Validation Score", 
                f"{model_metrics['cv_mean']:.1%}",
                delta=f"±{model_metrics['cv_std']:.1%}",
                help="Average accuracy across multiple validation folds"
            )
            
        with metric_col3:
            st.metric(
                "Training Samples", 
                "1000+",
                help="Number of samples used for training"
            )
    
    # Prediction section
    if predict_button:
        # Validate inputs
        validation_errors = validate_inputs(temp, humidity, moisture, nitrogen, potassium, phosphorous)
        
        if validation_errors:
            for error in validation_errors:
                st.warning(error)
        else:
            with st.spinner("🔍 Analyzing soil conditions and generating recommendation..."):
                try:
                    # Encode categorical inputs
                    soil_encoded = soil_encoder.transform([soil])[0]
                    crop_encoded = crop_encoder.transform([crop])[0]
                    
                    # Prepare features
                    features = np.array([[temp, humidity, moisture, soil_encoded, crop_encoded,
                                        nitrogen, potassium, phosphorous]])
                    
                    # Scale features if scaler is available
                    if scaler:
                        features = scaler.transform(features)
                    
                    # Make prediction
                    pred = model.predict(features)[0]
                    fertilizer_name = fertilizer_encoder.inverse_transform([pred])[0]
                    
                    # Get prediction probability
                    pred_proba = model.predict_proba(features)[0]
                    confidence = np.max(pred_proba) * 100
                    
                    # Display results
                    st.markdown("### 🎯 Recommendation Results")
                    
                    # Main recommendation
                    st.success(f"🏆 **Recommended Fertilizer: {fertilizer_name}**")
                    st.info(f"🎯 **Confidence Score: {confidence:.1f}%**")
                    
                    # Detailed fertilizer information
                    fert_info = get_fertilizer_info(fertilizer_name)
                    
                    st.markdown("#### 📋 Fertilizer Details")
                    
                    col_info1, col_info2 = st.columns(2)
                    
                    with col_info1:
                        st.markdown(f"**Description:** {fert_info['description']}")
                        st.markdown(f"**Application Rate:** {fert_info['application_rate']}")
                        st.markdown(f"**Best Timing:** {fert_info['timing']}")
                    
                    with col_info2:
                        st.markdown("**Key Benefits:**")
                        for benefit in fert_info['benefits']:
                            st.markdown(f"• {benefit}")
                        
                        st.markdown("**Best For:**")
                        for crop_type in fert_info['best_for']:
                            st.markdown(f"• {crop_type}")
                    
                    # Additional recommendations
                    st.markdown("#### 💡 Additional Tips")
                    
                    tip_col1, tip_col2 = st.columns(2)
                    
                    with tip_col1:
                        st.info("""
                        **🌱 Application Guidelines:**
                        • Conduct soil test before application
                        • Apply during optimal weather conditions
                        • Follow recommended dosage
                        • Split application for better efficiency
                        """)
                    
                    with tip_col2:
                        st.warning("""
                        **⚠️ Important Notes:**
                        • Store fertilizer in dry place
                        • Avoid over-application
                        • Monitor plant response
                        • Consult local agricultural expert
                        """)
                    
                    # Save prediction history (optional)
                    prediction_data = {
                        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        'temperature': temp,
                        'humidity': humidity,
                        'moisture': moisture,
                        'soil_type': soil,
                        'crop_type': crop,
                        'nitrogen': nitrogen,
                        'potassium': potassium,
                        'phosphorous': phosphorous,
                        'recommended_fertilizer': fertilizer_name,
                        'confidence': confidence
                    }
                    
                except Exception as e:
                    st.error(f"❌ Error making prediction: {str(e)}")
                    st.info("Please check your inputs and try again.")

with col2:
    # Information panel
    st.markdown("### 📚 Quick Guide")
    
    st.markdown("""
    **🌾 How to Use:**
    1. Enter environmental conditions
    2. Select your soil and crop type
    3. Input current nutrient levels
    4. Click 'Get Recommendation'
    
    **🎯 Accuracy Note:**
    Our AI model is trained on extensive agricultural data and provides recommendations based on scientific principles.
    
    **📞 Need Help?**
    Consult with local agricultural experts for best results.
    """)
    
    # Nutrient guide
    with st.expander("🧪 Nutrient Guide", expanded=False):
        st.markdown("""
        **Nitrogen (N):**
        - Promotes leaf growth
        - Essential for protein synthesis
        - Deficiency: Yellowing leaves
        
        **Phosphorous (P):**
        - Root development
        - Flower and fruit formation
        - Deficiency: Purple leaves
        
        **Potassium (K):**
        - Disease resistance
        - Water regulation
        - Deficiency: Brown leaf edges
        """)
    
    # Soil type guide
    with st.expander("🌍 Soil Types", expanded=False):
        st.markdown("""
        **Sandy Soil:**
        - Good drainage
        - Quick nutrient loss
        - Frequent fertilization needed
        
        **Clay Soil:**
        - Poor drainage
        - High nutrient retention
        - Less frequent fertilization
        
        **Loamy Soil:**
        - Best for most crops
        - Balanced properties
        - Moderate fertilization
        
        **Black/Red Soil:**
        - Rich in specific minerals
        - Region-specific properties
        - Varied fertilization needs
        """)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; opacity: 0.7; margin-top: 2rem;">
    <p>🌾 KrushiAI - Smart Fertilizer Recommendation System</p>
    <p>Empowering Farmers with AI-Driven Agricultural Intelligence</p>
</div>
""", unsafe_allow_html=True)
