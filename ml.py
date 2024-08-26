# import the inference-sdk

from os import getenv

from dotenv import load_dotenv
from inference_sdk import InferenceHTTPClient

# initialize the client

load_dotenv()

def classify(file_path):
    CLIENT = InferenceHTTPClient(
        api_url="https://detect.roboflow.com",
        api_key=getenv("API_KEY")
    )

    # infer on a local image
    result = CLIENT.infer(file_path, model_id="waste-classification-wrw6h/1")

    if (len(result["predicted_classes"]) == 0):
        return ""
    return result["predicted_classes"][0]