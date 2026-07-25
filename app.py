from fastapi import FastAPI, UploadFile, File
from fastapi.responses import Response
from rembg import remove
from PIL import Image
import io

app = FastAPI()

@app.get("/")
def home():
    return {"status": "VintClean AI API is running 🚀"}

@app.post("/remove-background")
async def remove_background(file: UploadFile = File(...)):

    image_bytes = await file.read()

    input_image = Image.open(io.BytesIO(image_bytes))

    output_image = remove(input_image)

    output_bytes = io.BytesIO()
    output_image.save(output_bytes, format="PNG")

    return Response(
        content=output_bytes.getvalue(),
        media_type="image/png"
    )