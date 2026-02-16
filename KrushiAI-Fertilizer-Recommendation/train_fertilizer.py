import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Load dataset
print("📊 Loading and analyzing dataset...")
df = pd.read_csv("Fertilizer_recommendation.csv")
print(f"Dataset shape: {df.shape}")
print(f"\nDataset info:")
print(df.info())
print(f"\nMissing values: {df.isnull().sum().sum()}")

# Fix column name typo
if 'Temparature' in df.columns:
    df = df.rename(columns={'Temparature': 'Temperature'})

# Remove leading/trailing spaces in column names
df.columns = df.columns.str.strip()

# Display basic statistics
print(f"\nDataset Statistics:")
print(df.describe())

# Encode categorical columns
print("\n🔄 Encoding categorical variables...")
le_soil = LabelEncoder()
le_crop = LabelEncoder()
le_fert = LabelEncoder()

df['Soil Type'] = le_soil.fit_transform(df['Soil Type'])
df['Crop Type'] = le_crop.fit_transform(df['Crop Type'])
df['Fertilizer Name'] = le_fert.fit_transform(df['Fertilizer Name'])

print(f"Soil types: {list(le_soil.classes_)}")
print(f"Crop types: {list(le_crop.classes_)}")
print(f"Fertilizer types: {list(le_fert.classes_)}")

# Features & labels
X = df.drop(columns=['Fertilizer Name'])
y = df['Fertilizer Name']

# Feature scaling for better performance
print("\n⚖️ Scaling features...")
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split dataset with stratification
print("\n📊 Splitting dataset...")
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42, stratify=y
)

# Hyperparameter tuning
print("\n🎯 Performing hyperparameter tuning...")
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [10, 20, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

rf = RandomForestClassifier(random_state=42)
grid_search = GridSearchCV(rf, param_grid, cv=5, scoring='accuracy', n_jobs=-1, verbose=1)
grid_search.fit(X_train, y_train)

print(f"Best parameters: {grid_search.best_params_}")
print(f"Best cross-validation score: {grid_search.best_score_:.4f}")

# Train best model
model = grid_search.best_estimator_

# Cross-validation
print("\n🔄 Performing cross-validation...")
cv_scores = cross_val_score(model, X_train, y_train, cv=5, scoring='accuracy')
print(f"Cross-validation scores: {cv_scores}")
print(f"Mean CV score: {cv_scores.mean():.4f} (+/- {cv_scores.std() * 2:.4f})")

# Model evaluation
print("\n📈 Evaluating model performance...")
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Test Accuracy: {accuracy:.4f}")

# Detailed classification report
print("\n📋 Classification Report:")
report = classification_report(y_test, y_pred, target_names=le_fert.classes_)
print(report)

# Feature importance
print("\n🎯 Feature Importance:")
feature_names = X.columns
importances = model.feature_importances_
feature_importance = pd.DataFrame({
    'feature': feature_names,
    'importance': importances
}).sort_values('importance', ascending=False)

print(feature_importance)

# Save model, encoders, and scaler
print("\n💾 Saving model and preprocessing objects...")
pickle.dump(model, open("Fertilizer_RF.pkl", "wb"))
pickle.dump(le_soil, open("soil_encoder.pkl", "wb"))
pickle.dump(le_crop, open("crop_encoder.pkl", "wb"))
pickle.dump(le_fert, open("fertilizer_encoder.pkl", "wb"))
pickle.dump(scaler, open("feature_scaler.pkl", "wb"))

# Save model metrics
model_metrics = {
    'accuracy': accuracy,
    'cv_mean': cv_scores.mean(),
    'cv_std': cv_scores.std(),
    'best_params': grid_search.best_params_,
    'feature_importance': feature_importance.to_dict('records')
}
pickle.dump(model_metrics, open("model_metrics.pkl", "wb"))

print("✅ Model, encoders, scaler, and metrics saved successfully!")
print(f"✅ Final model accuracy: {accuracy:.4f}")
