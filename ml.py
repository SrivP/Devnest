# import the inference-sdk

from inference_sdk import InferenceHTTPClient

# initialize the client

def classify(file_path):
    CLIENT = InferenceHTTPClient(
        api_url="https://detect.roboflow.com",
        api_key="no."
    )

    # infer on a local image
    result = CLIENT.infer(file_path, model_id="waste-classification-wrw6h/1")

    return result["predicted_classes"][0] 