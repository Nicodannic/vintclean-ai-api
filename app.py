from fastapi import FastAPI, UploadFile, File
from fastapi.responses import Response
from rembg import remove, new_session
from PIL import Image, ImageEnhance
from io import BytesIO
import cv2
import numpy as np


app = FastAPI()

session = new_session("u2netp")


@app.get("/")
def home():
    return {
        "status": "VintClean AI API is running 🚀"
    }


@app.post("/remove-background")
async def remove_background(file: UploadFile = File(...)):

    image_bytes = await file.read()

    image = Image.open(
        BytesIO(image_bytes)
    ).convert("RGBA")


    # Suppression fond
    result = remove(
        image,
        session=session
    )


    # Amélioration luminosité
    rgb = result.convert("RGB")

    enhancer = ImageEnhance.Brightness(rgb)
    rgb = enhancer.enhance(1.08)


    enhancer = ImageEnhance.Contrast(rgb)
    rgb = enhancer.enhance(1.15)


    # Netteté
    enhancer = ImageEnhance.Sharpness(rgb)
    rgb = enhancer.enhance(1.25)


    # Retour PNG
    output = BytesIO()

    rgb.save(
        output,
        format="PNG"
    )


    return Response(
        content=output.getvalue(),
        media_type="image/png"
    )