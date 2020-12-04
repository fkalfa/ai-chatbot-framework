import os

class Config(object):
    DEBUG = False
    #MONGODB_HOST = "mongodb://127.0.0.1:27017/iky-ai"
    MONGODB_HOST = "mongodb+srv://chatbot:chatbot1234@cluster0.iwgv8.mongodb.net/iky-ai?retryWrites=true&w=majority"
    # Intent Classifier model details
    MODELS_DIR = "model_files/"
    INTENT_MODEL_NAME = "intent.model"
    DEFAULT_FALLBACK_INTENT_NAME = "fallback"
    DEFAULT_WELCOME_INTENT_NAME = "init_conversation"
    USE_WORD_VECTORS = True


class Development(Config):
    DEBUG = True
    MONGODB_HOST = "mongodb+srv://chatbot:chatbot1234@cluster0.iwgv8.mongodb.net/iky-ai?retryWrites=true&w=majority"


class Production(Config):
    # MongoDB Database Details
   #MONGODB_HOST = "mongodb://mongodb:27017/iky-ai"
    MONGODB_HOST = "mongodb+srv://chatbot:chatbot1234@cluster0.iwgv8.mongodb.net/iky-ai?retryWrites=true&w=majority"
    # Web Server details
    WEB_SERVER_PORT = 8001

class Heroku(Production):
    #MONGODB_HOST = os.environ.get('MONGO_URL')
    MONGODB_HOST = "mongodb+srv://chatbot:chatbot1234@cluster0.iwgv8.mongodb.net/iky-ai?retryWrites=true&w=majority"
