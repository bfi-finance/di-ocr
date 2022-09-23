import uvicorn
from app.config import(SERVER_HOST,SERVER_PORT,LOG_LEVEL,)
from app import app
if __name__ == "__main__":
    uvicorn.run("app:app", host=SERVER_HOST, port=SERVER_PORT, log_level=LOG_LEVEL)