# 🌾 KrushiAI - Crop Recommendation System 🌾

Welcome to the **KrushiAI Crop Recommendation System**! This intelligent web application is a key component of my final year mega project, **"KrushiAI - AI Based Plant Diseases Identification, Crop & Fertilizer Recommendation"**. This tool leverages Machine Learning to help farmers make informed decisions by recommending the most suitable crop to plant based on various soil and environmental factors.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://krushiai-crop-recommendation-system.streamlit.app/)

## 🚀 Live Demo

You can access the live application here:
[https://krushiai-crop-recommendation-system.streamlit.app/](https://krushiai-crop-recommendation-system.streamlit.app/)

## ✨ Features

-   **User-Friendly Interface**: A simple and intuitive web interface built with Streamlit.
-   **Real-time Predictions**: Get instant crop recommendations based on your input.
-   **Data-Driven Insights**: The recommendations are powered by a robust Random Forest model.
-   **Informative**: Provides details about the recommended crop.
-   **Interactive Visualizations**: Shows a chart of the input parameters.

## ⚙️ How It Works

The application follows a simple workflow:
1.  The user enters soil parameters (Nitrogen, Phosphorus, Potassium, and pH) and environmental factors (Temperature, Humidity, and Rainfall).
2.  These inputs are fed into a pre-trained Random Forest model.
3.  The model processes the data and predicts the most suitable crop.
4.  The recommended crop is displayed to the user along with some information about it.

## 🛠️ Tech Stack

This project is built using the following technologies:

-   **Python**: The core programming language.
-   **Pandas & NumPy**: For data manipulation and numerical operations.
-   **Scikit-learn**: For building and evaluating machine learning models.
-   **Streamlit**: For creating and deploying the web application.
-   **Matplotlib & Seaborn**: For data visualization.
-   **Jupyter Notebook**: For model development and experimentation.

## 📊 Dataset

The model was trained on the `Crop_recommendation.csv` dataset, which contains 2200 data points. The dataset has the following 8 columns:
-   `N`: Nitrogen content in soil
-   `P`: Phosphorus content in soil
-   `K`: Potassium content in soil
-   `temperature`: Temperature in Celsius
-   `humidity`: Relative humidity in %
-   `ph`: pH value of the soil
-   `rainfall`: Rainfall in mm
-   `label`: The recommended crop (22 unique crop types)

## 🧠 Model Training & Evaluation

Several machine learning models were trained and evaluated to find the best one for this task. The models included:
-   Decision Tree
-   Gaussian Naive Bayes
-   Support Vector Machine (SVM)
-   Logistic Regression
-   **Random Forest**
-   XGBoost
-   K-Nearest Neighbors (KNN)

The Random Forest model was chosen for the final application due to its high accuracy of **99.5%** on the test set.

<!-- You can add your model accuracy comparison image here -->

## 🚀 How to Run Locally

To run this project on your local machine, follow these steps:

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/PRINCE-GUPTA-101/AI-Crop-Recommendation-System.git
    cd AI-Crop-Recommendation-System
    ```

2.  **Create a virtual environment (recommended):**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit application:**
    ```sh
    streamlit run webapp.py
    ```

The application will then be available at `http://localhost:8501`.

## 🌟 Future Scope

-   Integrate with real-time weather APIs to automatically fetch climate data.
-   Add a fertilizer recommendation feature.
-   Include a plant disease identification module as part of the larger KrushiAI project.
-   Improve the user interface and add more visualizations.

## 🙏 Acknowledgements

A big thank you to the open-source community for providing the tools and libraries that made this project possible.

---
*This README was generated with the help of an AI assistant.*
