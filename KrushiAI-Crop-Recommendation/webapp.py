## Importing necessary libraries for the web app
import streamlit as st
import numpy as np
import pandas as pd
import pickle
import os
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Set page configuration
st.set_page_config(
    page_title="KrushiAI - Crop Recommendation System",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI with dark mode
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stApp {
        background-color: #1a1a1a;
        color: #ffffff;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        width: 100%;
        border: none;
        box-shadow: 0 2px 4px rgba(76, 175, 80, 0.3);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #45a049;
        box-shadow: 0 4px 8px rgba(76, 175, 80, 0.4);
        transform: translateY(-1px);
    }
    h1, h2, h3 {
        color: #66BB6A !important;
        font-weight: bold;
    }
    .stSidebar {
        background-color: #2d2d2d;
        padding: 1rem;
        border-right: 1px solid #444;
    }
    .stSidebar .stMarkdown {
        color: #ffffff;
    }
    /* Input field styling */
    .stNumberInput > div > div > input {
        background-color: #333333;
        color: #ffffff;
        border: 1px solid #555;
        border-radius: 4px;
    }
    .stNumberInput > div > div > input:focus {
        border-color: #4CAF50;
        box-shadow: 0 0 0 1px #4CAF50;
    }
    /* Label styling */
    .stNumberInput > label {
        color: #ffffff !important;
        font-weight: 500;
    }
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        background-color: #2d2d2d;
    }
    .stTabs [data-baseweb="tab"] {
        color: #ffffff;
        background-color: #333333;
    }
    .stTabs [aria-selected="true"] {
        background-color: #4CAF50 !important;
        color: white !important;
    }
    /* Dataframe styling */
    .stDataFrame {
        background-color: #333333;
    }
    /* Text elements */
    .stMarkdown {
        color: #ffffff;
    }
    /* Info box styling */
    .stInfo {
        background-color: #2d4a2d;
        color: #ffffff;
        border: 1px solid #4CAF50;
    }
    /* Success/warning boxes */
    .stSuccess {
        background-color: #1b4d1b;
        color: #ffffff;
    }
    .stError {
        background-color: #4d1b1b;
        color: #ffffff;
    }
    /* Metric styling */
    [data-testid="metric-container"] {
        background-color: #333333;
        border: 1px solid #555;
        padding: 1rem;
        border-radius: 8px;
        color: #ffffff;
    }
    </style>
""", unsafe_allow_html=True)

# Display header with logo
col1, col2 = st.columns([1, 3])
with col1:
    # Display Images
    from PIL import Image
    try:
        img = Image.open("crop.png")
        st.image(img, width=150)
    except:
        st.write("🌱")

with col2:
    st.markdown("<h1 style='text-align: left;'>KrushiAI: Smart Crop Recommendation System</h1>", unsafe_allow_html=True)

# Load the dataset for reference and display
@st.cache_data
def load_data():
    return pd.read_csv('Crop_recommendation.csv')

# Load the model
@st.cache_resource
def load_model():
    return pickle.load(open('RF.pkl', 'rb'))

# Function to make predictions
def predict_crop(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall):
    model = load_model()
    prediction = model.predict(np.array([nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]).reshape(1, -1))
    return prediction

# Dictionary with crop information
crop_info = {
    'rice': "Rice thrives in warm, humid conditions with abundant water. Ideal for lowland areas with good irrigation.",
    'maize': "Maize (corn) grows well in well-drained soils with moderate rainfall and warm temperatures.",
    'chickpea': "Chickpeas prefer cool, dry conditions and can tolerate drought. They enrich soil with nitrogen.",
    'kidneybeans': "Kidney beans need warm temperatures and moderate rainfall. They prefer well-drained, fertile soil.",
    'pigeonpeas': "Pigeon peas are drought-resistant and grow well in semi-arid regions with minimal rainfall.",
    'mothbeans': "Moth beans are extremely drought-tolerant and thrive in hot, dry conditions with minimal water.",
    'mungbean': "Mung beans prefer warm temperatures and moderate rainfall. They have a short growing season.",
    'blackgram': "Black gram thrives in warm, humid conditions and can tolerate some drought.",
    'lentil': "Lentils prefer cool growing conditions and moderate rainfall. They're adaptable to various soil types.",
    'pomegranate': "Pomegranates thrive in hot, dry climates and are drought-tolerant once established.",
    'banana': "Bananas need consistent warmth, high humidity, and abundant water. They're sensitive to frost.",
    'mango': "Mangoes require tropical conditions with a distinct dry season for flowering. They're frost-sensitive.",
    'grapes': "Grapes grow best in temperate climates with warm, dry summers and mild winters.",
    'watermelon': "Watermelons need hot temperatures, plenty of sunlight, and moderate water during growth.",
    'muskmelon': "Muskmelons require warm temperatures, full sun, and moderate, consistent moisture.",
    'apple': "Apples need a cold winter period for dormancy and moderate summers. They prefer well-drained soil.",
    'orange': "Oranges thrive in subtropical climates with mild winters and warm summers.",
    'papaya': "Papayas need consistent warmth and moisture. They're very frost-sensitive.",
    'coconut': "Coconuts require tropical conditions with high humidity, warm temperatures, and regular rainfall.",
    'cotton': "Cotton thrives in warm climates with long growing seasons and moderate rainfall.",
    'jute': "Jute needs warm, humid conditions with high rainfall during the growing season.",
    'coffee': "Coffee grows best in tropical highlands with moderate temperatures and regular rainfall."
}

## Streamlit code for the web app interface
def main():
    # Create tabs for different sections
    tab1, tab2, tab3 = st.tabs(["🔮 Prediction", "📊 Dataset Info", "ℹ️ About"])
    
    with tab1:
        st.markdown("### Get Your Crop Recommendation")
        st.write("Enter your soil and climate parameters to get a personalized crop recommendation.")
        
        # Create two columns for input and results
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.subheader("Soil Parameters")
            nitrogen = st.number_input("🧪 Nitrogen (kg/ha)", min_value=0.0, max_value=140.0, value=50.0, step=1.0)
            phosphorus = st.number_input("🧪 Phosphorus (kg/ha)", min_value=0.0, max_value=145.0, value=50.0, step=1.0)
            potassium = st.number_input("🧪 Potassium (kg/ha)", min_value=0.0, max_value=205.0, value=50.0, step=1.0)
            ph = st.number_input("🧪 pH Level", min_value=0.0, max_value=14.0, value=6.5, step=0.1)
            
            st.subheader("Climate Parameters")
            temperature = st.number_input("🌡️ Temperature (°C)", min_value=0.0, max_value=51.0, value=25.0, step=0.1)
            humidity = st.number_input("💧 Humidity (%)", min_value=0.0, max_value=100.0, value=60.0, step=0.1)
            rainfall = st.number_input("🌧️ Rainfall (mm)", min_value=0.0, max_value=500.0, value=100.0, step=0.1)
            
            predict_button = st.button("🔮 Predict Crop")
        
        with col2:
            st.subheader("Recommendation Results")
            if predict_button:
                inputs = np.array([[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]])
                if not inputs.any() or np.isnan(inputs).any() or (inputs == 0).all():
                    st.error("Please fill in all input fields with valid values before predicting.")
                else:
                    with st.spinner('Analyzing your parameters...'):
                        prediction = predict_crop(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall)
                        recommended_crop = prediction[0].lower()
                        
                        # Display result with styling
                        st.markdown(f"""
                        <div style="background-color:#2d5a2d; padding:20px; border-radius:10px; margin-bottom:20px; border: 2px solid #4CAF50; box-shadow: 0 4px 8px rgba(76, 175, 80, 0.3);">
                            <h3 style="color:#81C784; text-align:center; margin-bottom:10px; font-weight:bold;">🌱 Recommended Crop</h3>
                            <h2 style="color:#A5D6A7; text-align:center; text-transform:uppercase; font-size:2.5rem; margin:0; text-shadow: 0 2px 4px rgba(0,0,0,0.3);">{prediction[0]}</h2>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Display crop information
                        if recommended_crop in crop_info:
                            st.markdown("### Crop Information")
                            st.info(crop_info[recommended_crop])
                        
                        # Display parameter importance visualization
                        st.markdown("### Parameter Importance")
                        
                        # Create a simple visualization of the input parameters
                        param_names = ['Nitrogen', 'Phosphorus', 'Potassium', 'Temperature', 'Humidity', 'pH', 'Rainfall']
                        param_values = [nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]
                        
                        # Set dark theme for matplotlib
                        plt.style.use('dark_background')
                        fig, ax = plt.subplots(figsize=(10, 5), facecolor='#1a1a1a')
                        bars = ax.bar(param_names, param_values, color=['#1976D2', '#4CAF50', '#FFC107', '#F44336', '#9C27B0', '#00BCD4', '#3F51B5'])
                        ax.set_title('Your Input Parameters', color='white', fontsize=14, fontweight='bold')
                        ax.set_ylabel('Value', color='white', fontweight='bold')
                        ax.set_facecolor('#2d2d2d')
                        ax.tick_params(colors='white')
                        ax.spines['bottom'].set_color('white')
                        ax.spines['top'].set_color('white')
                        ax.spines['right'].set_color('white')
                        ax.spines['left'].set_color('white')
                        plt.xticks(rotation=45, color='white')
                        plt.yticks(color='white')
                        plt.tight_layout()
                        st.pyplot(fig)
            else:
                st.info("Fill in the parameters and click 'Predict Crop' to get your recommendation.")
                
    with tab2:
        st.markdown("### Dataset Information")
        df = load_data()
        st.write("This application uses a dataset with the following characteristics:")
        st.write(f"- **Number of records**: {df.shape[0]}")
        st.write(f"- **Number of features**: {df.shape[1]-1}")
        st.write(f"- **Crop varieties**: {df['label'].nunique()}")
        
        # Show sample data
        st.subheader("Sample Data")
        st.dataframe(df.head())
        
        # Show distribution of crops in the dataset
        st.subheader("Crop Distribution")
        plt.style.use('dark_background')
        fig, ax = plt.subplots(figsize=(12, 6), facecolor='#1a1a1a')
        crop_counts = df['label'].value_counts()
        sns.barplot(x=crop_counts.index, y=crop_counts.values, ax=ax, palette='viridis')
        ax.set_facecolor('#2d2d2d')
        ax.set_title('Distribution of Crops in Dataset', color='white', fontsize=14, fontweight='bold')
        ax.set_xlabel('Crop Type', color='white', fontweight='bold')
        ax.set_ylabel('Number of Records', color='white', fontweight='bold')
        ax.tick_params(colors='white')
        ax.spines['bottom'].set_color('white')
        ax.spines['top'].set_color('white')
        ax.spines['right'].set_color('white')
        ax.spines['left'].set_color('white')
        plt.xticks(rotation=90, color='white')
        plt.yticks(color='white')
        plt.tight_layout()
        st.pyplot(fig)
        
    with tab3:
        st.markdown("### About KrushiAI")
        
        # Create a styled container using Streamlit's native components
        st.markdown("""
        <div style="background-color: #2d2d2d; padding: 25px; border-radius: 12px; border: 2px solid #4CAF50; margin-bottom: 20px;">
            <p style="color: #ffffff; font-size: 18px; line-height: 1.8; margin-bottom: 25px;">
                🌾 <strong>KrushiAI</strong> is an intelligent crop recommendation system that uses machine learning 
                to suggest the most suitable crops based on soil composition and environmental factors.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # How it works section
        st.markdown("""
        <div style="background-color: #2d2d2d; padding: 20px; border-radius: 10px; border-left: 4px solid #4CAF50; margin-bottom: 20px;">
            <h4 style="color: #81C784; margin-top: 0; margin-bottom: 15px;">🔬 How it works:</h4>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 20])
        with col1:
            st.write("")
        with col2:
            st.markdown("**1.** The system analyzes your input parameters (N, P, K values, temperature, humidity, pH, and rainfall)")
            st.markdown("**2.** It processes this data through a trained Random Forest model")
            st.markdown("**3.** The model predicts the most suitable crop for your conditions")
        
        # Benefits section
        st.markdown("""
        <div style="background-color: #2d2d2d; padding: 20px; border-radius: 10px; border-left: 4px solid #4CAF50; margin: 20px 0;">
            <h4 style="color: #81C784; margin-top: 0; margin-bottom: 15px;">🎯 Benefits:</h4>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 20])
        with col1:
            st.write("")
        with col2:
            st.markdown("• 🚀 **Optimize agricultural yield** by planting suitable crops")
            st.markdown("• 💰 **Reduce resource wastage** by avoiding unsuitable crop selections")
            st.markdown("• 📊 **Make data-driven farming decisions**")
            st.markdown("• 🌱 **Promote sustainable farming practices**")
        
        # Footer section
        st.markdown("""
        <div style="background-color: #1a4a1a; padding: 15px; border-radius: 8px; text-align: center; margin-top: 30px; border: 1px solid #4CAF50;">
            <p style="color: #A5D6A7; font-size: 14px; margin: 0;">
                🛠️ Built with <strong>Streamlit</strong> and <strong>scikit-learn</strong> | 🧠 Powered by <strong>Random Forest</strong> algorithm
            </p>
        </div>
        """, unsafe_allow_html=True)

## Running the main function
if __name__ == '__main__':
    main()

