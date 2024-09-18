from dotenv import load_dotenv
import os
from app.src.infra.entrypoints.app import App

load_dotenv()

app = App()

if __name__ == '__main__':
    app.run()
