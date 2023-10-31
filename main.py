
from app_factory import create_app
import os

if __name__ == "__main__":
    app = create_app()
    app.run("0.0.0.0", port=os.getenv('PORT', 6969))
