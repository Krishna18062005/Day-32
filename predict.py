from tensorflow.keras.models import load_model
import numpy as np

model=load_model('heart_disease_model.h5')

model.summary()




# Input features: age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal
age=int(input("Enter age: "))
sex=int(input("Enter male or female: "))
cp=int(input("Chest pain type: "))
trestbps=int(input("Resting blood pressure: "))
chol=int(input("Cholestrol rate: "))
fbs=int(input("fast blood sugar: "))
restecg=int(input("restecg: "))
thalach=int(input("enter thalach: "))
exang=int(input("Enter exang: "))
oldpeak=int(input("Enter old peak: "))
slope=int(input("Slope: "))
ca=int(input("ca: "))
thal=int(input("Thal: "))



input_data = np.array([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])


prediction = model.predict(input_data)

# Output the prediction
# Assuming binary classification (0 = No heart disease, 1 = Heart disease)
if prediction[0][0] > 0.5:
    print("Prediction: Heart disease detected")
else:
    print("Prediction: No heart disease")