from ultralytics import YOLO
import os


def __main__():
    os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "max_split_size_mb:21"

    model = YOLO('yolov3u')

    results = model.train(
        data='config.yaml',
        imgsz=640,
        epochs=200,
        batch=4,
        name='yolov3-32',
        save_period=20
    )


if __name__ == "__main__":
    __main__()