from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()
class Settings(BaseSettings):
    def __init__(self):
        super().__init__()
        self.GMAIL_USER = os.environ.get("GMAIL_USER")
        self.GMAIL_PASSWORD = os.environ.get("GMAIL_PASSWORD")
    GMAIL_USER: str
    GMAIL_PASSWORD: str

settings = Settings()

# Encoding fix 