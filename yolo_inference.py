from ultralytics import YOLO

model = YOLO("yolo11x")

results = model.track("input_video/input_video.mp4", conf=0.2, save=True)

# print(results)
# print("boxes:")
# for box in results[0].boxes:
#     print(box)
