import requests
from collections import Counter
from processing_money import count_money, remove_duplicates
from dotenv import load_dotenv
import os

load_dotenv()


url = os.getenv("DEPLOYMENT_URL")
api_key = os.getenv("DEPLOYMENT_API_KEY")

headers = {f"Authorization": "Bearer " + api_key}

data = {"conf": 0.1, "iou": 0.5, "imgsz": 1280}
def inference(image_path):
    with open(image_path, "rb") as f:
        response = requests.post(url, headers=headers, data=data, files={"file": f})

    result = response.json()

    detections = result["images"][0]["results"]

    # фильтр по confidence
    detections = [d for d in detections if d["confidence"] > 0.5]

    # убираем дубликаты
    detections = remove_duplicates(detections)

    names = [d["name"] for d in detections]

    # считаем
    total = count_money(Counter(names))
