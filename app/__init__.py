from fastapi import FastAPI
from app.route import api_router
description = "License Plate Plate, ID (KTP), STNK Detector "
app = FastAPI(title="Optical Character Recognition",description=description,version="0.1.0")
app.include_router(api_router)
