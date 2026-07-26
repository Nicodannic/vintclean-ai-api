from fastapi import FastAPI, UploadFile, File
from fastapi.responses import Response
from PIL import Image
from io import BytesIO

app = FastAPI()


@app.get("/")
def home():
    return {
        "status": "VintClean AI API is running 🚀"
    }


@app.post("/remove-background")
async def remove_background(file: UploadFile = File(...)):

    print("Image reçue")

    image_bytes = await file.read()

    image = Image.open(
        BytesIO(image_bytes)
    )

    print("Image ouverte")

    output = BytesIO()

    image.save(
        output,
        format="PNG"
    )

    print("Image renvoyée")

    return Response(
        content=output.getvalue(),
        media_type="image/png"
    )