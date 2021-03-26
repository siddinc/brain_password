import uvicorn
from app.core.config import host, port, app


if __name__ == "__main__":
  uvicorn.run(app, host=host, port=port)