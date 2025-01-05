import time

from ultralytics import YOLO


model = YOLO("bestV11.pt")
results = model.predict("./testpictures/")
for result in results:
    result.save()

print(time.process_time())


