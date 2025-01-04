import time

from ultralytics import YOLO


model = YOLO("bestV11.pt")
results = model.predict("D:/cable-damage/test")
for result in results:
    result.save()

print(time.process_time())


