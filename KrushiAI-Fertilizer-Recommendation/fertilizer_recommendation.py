import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pickle

# 1️⃣ Load dataset
df = pd.read_csv("Fertilizer_recommendation.csv")

# 2️⃣ Encode categorical columns
le_soil = LabelEncoder()
le_crop = LabelEncoder()
le_fert = LabelEncoder()

df['Soil Type'] = le_soil.fit_transform(df['Soil Type'])
df['Crop Type'] = le_crop.fit_transform(df['Crop Type'])
df['Fertilizer Name'] = le_fert.fit_transform(df['Fertilizer Name'])

# Features & labels
X = df.drop(columns=['Fertilizer Name'])
y = df['Fertilizer Name']

# 3️⃣ Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4️⃣ Train RandomForest model
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# 5️⃣ Save model + encoders
pickle.dump(model, open("Fertilizer_RF.pkl", "wb"))
pickle.dump(le_soil, open("soil_encoder.pkl", "wb"))
pickle.dump(le_crop, open("crop_encoder.pkl", "wb"))
pickle.dump(le_fert, open("fertilizer_encoder.pkl", "wb"))

print("✅ Model and encoders saved successfully!")

# 6️⃣ Test prediction (manual input)
print("\n--- Test Prediction ---")
temp = float(input("Enter Temperature: "))
humidity = float(input("Enter Humidity: "))
moisture = float(input("Enter Moisture: "))
soil = input("Enter Soil Type (e.g. Sandy, Clayey, Loamy, Red, Black): ")
crop = input("Enter Crop Type (e.g. Maize, Wheat, Sugarcane, Tobacco): ")
nitrogen = float(input("Enter Nitrogen value: "))
potassium = float(input("Enter Potassium value: "))
phosphorous = float(input("Enter Phosphorous value: "))

# Encode categorical inputs
soil_encoded = le_soil.transform([soil])[0]
crop_encoded = le_crop.transform([crop])[0]

features = [[temp, humidity, moisture, soil_encoded, crop_encoded, nitrogen, potassium, phosphorous]]
pred = model.predict(features)[0]
fertilizer_name = le_fert.inverse_transform([pred])[0]

print(f"\n✅ Recommended Fertilizer: {fertilizer_name}")
