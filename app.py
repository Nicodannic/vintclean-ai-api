from fastapi import FastAPI, UploadFile, File
from fastapi.responses import Response
from rembg import remove, new_session
from PIL import Image
from io import BytesIO

app = FastAPI()

session = new_session("u2netp")


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

    print("Traitement avec u2netp")

    result = remove(
        image,
        session=session
    )

    output = BytesIO()

    result.save(
        output,
        format="PNG"
    )

    print("Terminé")

    return Response(
        content=output.getvalue(),
        media_type="image/png"
    )