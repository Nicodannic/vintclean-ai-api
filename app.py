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

    image_bytes = await file.read()

    input_image = Image.open(
        BytesIO(image_bytes)
    )

    output = remove(input_image)

    output_bytes = BytesIO()
    output.save(output_bytes, format="PNG")

    return Response(
        content=output_bytes.getvalue(),
        media_type="image/png"
    )