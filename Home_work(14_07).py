import io
import os
from PIL import Image
from fastapi import FastAPI, UploadFile, File, HTTPException, BackgroundTasks
from typing import List
from starlette.testclient import TestClient

app = FastAPI()
UPLOAD_DIRECTORY = "/file/"
MAX_FILE_SIZE = 10 * 1024 * 1024
ALLOWED_IMAGE_TYPES = ["image/jpeg", "image/png"]
client = TestClient(app)


def resize_image(image_data: bytes, max_size: tuple = (800, 600)) -> bytes:
    with Image.open(io.BytesIO(image_data)) as img:
        img.thumbnail(max_size)
        img_byte_array = io.BytesIO()
        img.save(img_byte_array, format=img.format)
        return img_byte_array.getvalue()


async def process_image(file_path: str):
    with open(file_path, "rb") as file:
        resized_image = resize_image(file.read())
    with open(file_path, "wb") as file:
        file.write(resized_image)


def test_upload_photo():
    with open("test_files/test_image.jpg", "rb") as file:
        response = client.post(
            "/upload-photo/",
            files={"file": ("test_image.jpg", file, "image/jpeg")}
        )
    assert response.status_code == 200
    assert "Фотографія завантажена, розпочато обробку." in response.json().get("info")


def test_upload_invalid_file_format():
    with open("test_files/test_document.pdf", "rb") as file:
        response = client.post(
            "/upload-photo/",
            files={"file": ("test_document.pdf", file, "application/pdf")}
        )
    assert response.status_code == 400
    assert "Недопустимий формат файлу" in response.json().get("detail")


def validate_and_sanitize_image(file: UploadFile):
    if file.content_type not in ALLOWED_IMAGE_TYPES:
        raise HTTPException(status_code=400, detail="Недозволений формат файлу.")

    try:
        image = Image.open(file.file)
        buffered = io.BytesIO()
        image.save(buffered, format=image.format)
        return buffered.getvalue()
    except Exception:
        raise HTTPException(status_code=400, detail="Неможливо обробити файл.")


@app.post("/create-post/")
def asd(background_tasks: BackgroundTasks, file: List[UploadFile] = File(...)):
    file_data = validate_and_sanitize_image(file)
    if file.file.__sizeof__() > MAX_FILE_SIZE:
        raise HTTPException(status_code=413, detail="Файл занадто великий")
    if file.content_type not in ALLOWED_IMAGE_TYPES:
        raise HTTPException(status_code=400, detail="Недопустимий формат файлу")

    file_path = os.path.join(UPLOAD_DIRECTORY, file.filename)
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    file_location = f"temp/{file.filename}"
    with open(file_location, "wb") as saved_file:
        saved_file.write(file.file.read())

    background_tasks.add_task(process_image, file_location)

