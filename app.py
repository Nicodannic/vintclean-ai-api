from fastapi import FastAPI, UploadFile, File
from fastapi.responses import Response
from rembg import remove, new_session
from PIL import Image
from io import BytesIO

app = FastAPI()

session = None


@app.get("/")
def home():
    return {
        "status": "VintClean AI API is running 🚀"
    }


@app.post("/remove-background")
async def remove_background(file: UploadFile = File(...)):

    global session

    try:
        print("Image reçue")

        if session is None:
            print("Chargement modèle u2netp...")
            session = new_session("u2netp")
            print("Modèle chargé")

        image_bytes = await file.read()

        print("Taille :", len(image_bytes))

        image = Image.open(
            BytesIO(image_bytes)
        )

        print("Image ouverte")

        result = remove(
            image,
            session=session
        )

        print("Fond supprimé")

        output = BytesIO()

        result.save(
            output,
            format="PNG"
        )

        print("PNG créé")

        return Response(
            content=output.getvalue(),
            media_type="image/png"
        )

    except Exception as e:
        print("ERREUR :", e)
        return {
            "error": str(e)
        }