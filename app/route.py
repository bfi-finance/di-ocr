from fastapi import APIRouter,UploadFile,File
from app.core import (
    text_detection_google_vision,
    get_text_plate,get_text_stnk,get_text_ktp
)

api_router = APIRouter()
@api_router.get("/")
def read_root():
    return {"Hello": "World"}

@api_router.post("/read_police_number")
def read_police_number_image(file : UploadFile=File(...)):
    try:
        contents = file.file.read()
        response = text_detection_google_vision(contents)
        text_plate_response = get_text_plate(response=response)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()
    return text_plate_response

@api_router.post("/scan_police_number")
def detect_police_number(file_bytes: bytes = File()):
    try:
        response = text_detection_google_vision(file_bytes)
        text_plate_response = get_text_plate(response=response)
    except Exception:
        return {"message": "There was an error uploading the file"}
    return text_plate_response


@api_router.post("/scan_stnk")
def read_stnk_image(file : UploadFile=File(...)):
    try:
        contents = file.file.read()
        response = text_detection_google_vision(contents)
        text_plate_response = get_text_stnk(response=response)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()
    return text_plate_response

@api_router.post("/scan_stnk_by_bytes")
def scan_stnk_image_by_bytes(file_bytes: bytes = File()):
    try:
        response = text_detection_google_vision(file_bytes)
        parse_stnk = get_text_stnk(response=response)
    except Exception:
        return {"message": "There was an error uploading the file"}
    return parse_stnk

@api_router.post("/scan_ktp")
def read_ktp_image(file : UploadFile=File(...)):
    try:
        contents = file.file.read()
        with open(file.filename, 'wb') as f:
            f.write(contents)
        response = text_detection_google_vision(contents)
        text_plate_response = get_text_ktp(response=response)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()
    return text_plate_response

@api_router.post("/scan_ktp_by_bytes")
def scan_ktp_image_by_bytes(file_bytes: bytes = File()):
    try:
        response = text_detection_google_vision(file_bytes)
        text_plate_response = get_text_ktp(response=response)
    except Exception:
        return {"message": "There was an error uploading the file"}

    return text_plate_response