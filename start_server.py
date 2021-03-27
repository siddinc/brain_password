import uvicorn
from app.main import app
from app.core.configuration import host, port


if __name__ == "__main__":
  uvicorn.run(app, host=host, port=port)