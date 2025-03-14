import os
import cv2
import albumentations as A

# Paths
input_dir = "Egg-BearingLobsters" 
output_img_dir = "Egg-BearingNew"


os.makedirs(output_img_dir, exist_ok=True)


augmentations = [
    A.HorizontalFlip(p=1),
    A.VerticalFlip(p=1),
    A.RandomBrightnessContrast(p=1, brightness_limit=0.2, contrast_limit=0.2),
    A.GaussianBlur(p=1, blur_limit=(3, 7)),
    A.ShiftScaleRotate(p=1, shift_limit=0.1, scale_limit=0.2, rotate_limit=30, border_mode=cv2.BORDER_CONSTANT),
]

image_files = [f for f in os.listdir(input_dir) if f.endswith((".png", ".jpg", ".jpeg"))]

for img_file in image_files:
    img_path = os.path.join(input_dir, img_file)
    image = cv2.imread(img_path)

    if image is None:
        print(f"Skipping {img_file} due to loading error.")
        continue

 
    for i, aug in enumerate(augmentations):
        augmented = aug(image=image)["image"]

        aug_img_path = os.path.join(output_img_dir, f"{img_file.split('.')[0]}_aug{i}.jpg")
        cv2.imwrite(aug_img_path, augmented)

print("Augmentation complete! Augmented images are saved.")
