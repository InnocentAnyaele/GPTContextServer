from dotenv import load_dotenv
load_dotenv()
import os

class Config():
    # BEARER_TOKEN = 'Bearer SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'
    BEARER_TOKEN = os.getenv('BEARER_TOKEN')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
    HARDCODED_INDEX_KEY = 'bb02481f-eb66-11ed-9c16-20c19bff2da0'

    
class DevelopmentConfig(Config):
    DEBUG = True
