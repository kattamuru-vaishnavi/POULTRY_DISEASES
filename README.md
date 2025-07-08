# 🐔 Transfer Learning-Based Classification of Poultry Diseases

This project leverages **transfer learning** and **deep learning** to build an AI-powered poultry disease detection system. The system is integrated into a mobile-friendly web application where users (primarily farmers) can input symptoms or images of their poultry to receive real-time diagnosis and treatment suggestions.

---

## 📝 Project Overview

Poultry farming is highly susceptible to disease outbreaks, which can lead to significant economic losses. This system classifies poultry health into **four categories**:
- **Salmonella**
- **Newcastle Disease**
- **Coccidiosis**
- **Healthy**

Using a transfer learning model (CNN-based), this solution helps users:
- Diagnose poultry diseases
- Receive actionable treatment suggestions
- Prevent the spread of infection
- Reduce reliance on immediate veterinary access

---

## 📲 Features

- 📸 Image-based disease detection using deep learning
- 📝 Manual input of symptoms and environmental conditions
- 🧾 Treatment suggestions and emergency guidance
- 🗂 Disease history and recovery logging
- 🌐 Mobile-friendly user interface
- 🔒 Secure backend using Flask API

---

## 🚀 How It Works

1. **User Input**  
   - Upload an image of the poultry or input symptoms.
2. **Backend Processing**  
   - A Flask API receives the input and passes it to a pretrained CNN model.
3. **Disease Prediction**  
   - The model predicts the disease class and returns the result.
4. **Output**  
   - The app displays the disease name, brief description, and treatment advice.

---

## 🧠 Tech Stack

| Component        | Technology Used           |
|------------------|----------------------------|
| Model Training   | TensorFlow, Keras, Google Colab |
| Backend API      | Flask                      |
| Frontend         | HTML, CSS, JavaScript (or React) |
| Deployment       | Render / Localhost         |
| Data Source      | Roboflow (Custom Dataset)  |

---

## 📊 Model Performance

- ✅ Train Accuracy: 98.2%  
- ✅ Validation Accuracy: 94.6%  
- ✅ Post-Fine-Tuning Accuracy: 95.3%  
- 🧪 Dataset: 4-Class poultry disease images (Coccidiosis, Newcastle, Salmonella, Healthy)

---

## 💡 Real-World Scenarios

1. **Rural Outbreak Management**  
   Farmers in remote areas can quickly diagnose issues without waiting for vet support.

2. **Commercial Farm Monitoring**  
   Regular scanning of poultry batches ensures early intervention and prevents mass loss.

3. **Veterinary Education**  
   Students can simulate real-world cases to learn disease diagnosis and treatment planning.

---

## 🔮 Future Scope

- Add more poultry diseases (e.g., Avian Influenza)
- Launch Android/iOS app version
- Multilingual support for rural areas
- Suggest dosage of medicines
- Integrate voice input/output for accessibility
- Continuous learning model with feedback loop



