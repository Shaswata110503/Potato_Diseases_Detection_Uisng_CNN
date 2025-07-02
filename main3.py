from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

from fastapi import FastAPI, File, UploadFile
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf

app = FastAPI()

# Load the trained model
MODEL = tf.keras.models.load_model(
    r"C:\Users\desha\Downloads\ML JUPYTER\Potato_Diseases\my model\my_model.keras"
)

CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

disease_info = {
    'Early Blight': {
        'name': 'Early Blight',
        'remedy': 'Use appropriate fungicides and crop rotation.Click at Learn More',
        'google_search': 'https://agritech.tnau.ac.in/crop_protection/crop_prot_crop%20diseases_veg_potato_2.html'
    },
    'Late Blight': {
        'name': 'Late Blight',
        'remedy': 'Apply late blight specific fungicides immediately.Click at Learn More',
        'google_search': 'https://www.pau.edu/potato/lb_mang.php'
    },
    'Healthy': {
        'name': 'Healthy',
        'remedy': 'No remedy needed. Maintain good plant care.',
        'google_search': 'https://www.google.com/search?q=healthy+potato+plant+care'
    }
}


# Serve static files and templates
app.mount("/static", StaticFiles(directory="templates\static"), name="static")
templates = Jinja2Templates(directory="templates")

# Home route (drag-and-drop UI)
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index4.html", {"request": request})

# Simple test route
@app.get("/ping")
async def ping():
    return "hello! I am alive"

# Read image file into NumPy array
def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image, 0)
    prediction = MODEL.predict(img_batch)
    predicted_class = CLASS_NAMES[np.argmax(prediction[0])]
    confidence = np.max(prediction[0])*100 # Convert to percentage

    # Fetch disease information
    disease_details = disease_info.get(predicted_class, {})
    remedy = disease_details.get('remedy', 'No remedy available')
    google_search_url = disease_details.get('google_search', '#')

    warning = ""
    if confidence < 70:
        warning = "⚠️ Prediction might be uncertain. Please try another image."

    return {
        "predicted_class": predicted_class,
        "confidence": round(float(confidence), 2),
        "remedy": remedy,
        "google_search_url": google_search_url,
        "warning": warning
    }


# Run the server
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
