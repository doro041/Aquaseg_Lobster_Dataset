import os
import shutil
import random

# Define paths
source_dir = "Egg-BearingNew"  
output_dir = "Egg-BearingNewnew"  
train_ratio, val_ratio, test_ratio = 0.8, 0.20, 0.10  # 

# Create output directories
for split in ["train", "val", "test"]:
    os.makedirs(os.path.join(output_dir, split), exist_ok=True)

# Get all files
all_files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]
random.shuffle(all_files)  # Shuffle for randomness

# Split data
train_split = int(len(all_files) * train_ratio)
val_split = int(len(all_files) * (train_ratio + val_ratio))

train_files = all_files[:train_split]
val_files = all_files[train_split:val_split]
test_files = all_files[val_split:]

# Move files
for f in train_files:
    shutil.move(os.path.join(source_dir, f), os.path.join(output_dir, "train", f))
for f in val_files:
    shutil.move(os.path.join(source_dir, f), os.path.join(output_dir, "val", f))
for f in test_files:
    shutil.move(os.path.join(source_dir, f), os.path.join(output_dir, "test", f))

print(f"Split complete: Train={len(train_files)}, Val={len(val_files)}, Test={len(test_files)}")
