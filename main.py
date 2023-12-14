from transformers import DetrImageProcessor, DetrForObjectDetection
import torch
from PIL import Image
import requests
import matplotlib.pyplot as plt
import matplotlib.patches as patches

image_path = "image1.jpg"
image = Image.open(image_path)

# You can specify the revision tag if you don't want the timm dependency
processor = DetrImageProcessor.from_pretrained("facebook/detr-resnet-50", revision="no_timm")
model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50", revision="no_timm")

inputs = processor(images=image, return_tensors="pt")
outputs = model(**inputs)

# Convert outputs (bounding boxes and class logits) to COCO API
# Let's only keep detections with a score > 0.8 (80% confidence)
target_sizes = torch.tensor([image.size[::-1]])
results = processor.post_process_object_detection(outputs, target_sizes=target_sizes, threshold=0.7)[0]

# Visualize the image with bounding boxes around chess pieces
fig, ax = plt.subplots(1)
ax.imshow(image)

# Print information about detected chess pieces
for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
    box = [round(i, 2) for i in box.tolist()]
    class_name = model.config.id2label[label.item()]

    # Create a rectangle patch
    rect = patches.Rectangle((box[0], box[1]), box[2] - box[0], box[3] - box[1], linewidth=2, edgecolor='r',
                             facecolor='none')

    # Add the patch to the Axes
    ax.add_patch(rect)

    # Display class label and confidence score
    ax.text(box[0], box[1], f'{class_name} {round(score.item(), 3)}', color='r', verticalalignment='top')

    print(
        f"Chess Piece: {class_name} - Confidence: {round(score.item() * 100, 2)}%"
        f" - Position: {box}")

plt.show()




























