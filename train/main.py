from ultralytics import YOLO
import os
from pathlib import Path


def __main__():
    model = YOLO(model="yolo12m.pt")

    results = model.train(
        data=Path(__file__).resolve().parent / "config.yaml",
        imgsz=640,
        epochs=100,
        batch=-1,
        save_period=20,
    )


if __name__ == "__main__":
    __main__()
