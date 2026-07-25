from fastapi import FastAPI, UploadFile, File
from fastapi.responses import Response
from rembg import remove
from PIL import Image
from io import BytesIO

app = FastAPI()

@app.get("/")
def home():
    return {"status": "VintClean AI API is running 🚀"}


@app.post("/remove-background")
async def remove_background(file: UploadFile = File(...)):

    try:
        print("Image reçue")

        image_bytes = await file.read()

        print("Taille image :", len(image_bytes))

        input_image = Image.open(
            BytesIO(image_bytes)
        )

        print("Image ouverte")

        output = remove(input_image)

        print("Fond supprimé")

        output_bytes = BytesIO()

        output.save(
            output_bytes,
            format="PNG"
        )

        print("PNG créé")

        return Response(
            content=output_bytes.getvalue(),
            media_type="image/png"
        )

    except Exception as e:
        print("ERREUR :", e)
        return {
            "error": str(e)
        }