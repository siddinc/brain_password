import uvicorn
from app.main import app
from app.core.config import HOST, PORT


if __name__ == "__main__":
  uvicorn.run(app, host=HOST, port=PORT)