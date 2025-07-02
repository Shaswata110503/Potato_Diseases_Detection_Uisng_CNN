# 🍃 Potato Leaf Disease Detection Web App

A full-stack machine learning web application that identifies potato plant diseases from leaf images and provides actionable remedies. Powered by TensorFlow and FastAPI with an interactive drag-and-drop user interface.

## 🔍 Features

- 🎯 Accurate prediction using a trained CNN model
- 🖼️ Drag-and-drop UI for seamless image uploads
- 📈 Confidence score included with every prediction
- 💡 Shows remedy and trusted agricultural resource links
- ⚠️ Warns user if prediction confidence is below 70%
- 🔐 Clean backend API built with FastAPI

---

## 🧠 Model Details

- **Model Type**: Convolutional Neural Network (CNN)
- **Input Image Size**: 128×128 pixels
- **Output Classes**:
  - `Early Blight`
  - `Late Blight`
  - `Healthy`

---

## 🧪 Sample Prediction Response

```json
{
  "predicted_class": "Late Blight",
  "confidence": 92.15,
  "remedy": "Apply late blight specific fungicides immediately. Click at Learn More",
  "google_search_url": "https://www.pau.edu/potato/lb_mang.php",
  "warning": ""
}

**How to Run Locally**
1.Clone the Repository
2.Install Dependencies
3.Run the App
4.Now open your browser and go to:
👉 http://localhost:8000

📌 **Future Enhancements**
🧠 Grad-CAM visualization to show prediction focus
📊 Prediction history page
📱 Mobile-responsive UI
🌐 Add support for other crops

