import os
import requests
from dotenv import load_dotenv

from processor import MoneyProcessor


class MoneyDetector:

    def __init__(self):
        load_dotenv()

        self.url = os.getenv("DEPLOYMENT_URL")
        self.api_key = os.getenv("DEPLOYMENT_API_KEY")

        self.headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

        self.data = {
            "conf": 0.1,
            "iou": 0.5,
            "imgsz": 1280
        }

    def _send_request(self, image_path):

        with open(image_path, "rb") as f:
            response = requests.post(
                self.url,
                headers=self.headers,
                data=self.data,
                files={"file": f}
            )

        return response.json()

    def inference(self, image_path):

        result = self._send_request(image_path)

        detections = result["images"][0]["results"]

        # фильтр confidence
        detections = [d for d in detections if d["confidence"] > 0.5]

        # удаление дубликатов
        detections = MoneyProcessor.remove_duplicates(detections)

        # подсчёт денег
        total = MoneyProcessor.count_money(detections)

        return total