# import the inference-sdk
from inference_sdk import InferenceHTTPClient
from dotenv import load_dotenv
import os

load_dotenv()

# initialize the client

def classify(file_path):
    CLIENT = InferenceHTTPClient(
        api_url="https://detect.roboflow.com",
        api_key=os.getenv("API_KEY")
    )

    # infer on a local image
    result = CLIENT.infer(file_path, model_id="waste-classification-wrw6h/1")

    return result["predicted_classes"][0] 