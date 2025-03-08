# Aquaseg_Lobster_Dataset

This repository contains curated and synthetic datasets designed for **few-shot segmentation of lobsters**, with a particular emphasis on **egg-bearing (berried) lobsters**. The dataset aims to support **marine life conservation** by improving the **automated detection and segmentation** of lobsters across diverse aquatic environments.

The dataset is tailored for training lightweight segmentation models, facilitating **real-time detection** in a cross-platform mobile and desktop application. This effort aligns with ongoing conservation initiatives focused on protecting breeding lobster populations.

---

## 📌 Data Sources

To ensure a diverse and robust dataset, we aggregated data from multiple sources and further enhanced it through **synthetic data augmentation**. The sources include:

1. **Underwater Lobster Dataset** – Extracted from the [Sea Animals Image Dataset on Kaggle](https://www.kaggle.com/datasets/vencerlanz09/sea-animals-image-dataste) (Lobster subset). Annotations were performed manually for segmentation.
2. **Offshore Lobster Dataset** – Sourced from the [Crustaceans Dataset on GitHub](https://github.com/ifiaber/Crustaceans/tree/main/Lobsters) (Lobster subset with provided annotations).
3. **Male, Female & Egg-Bearing Lobsters Dataset** – Additional data was sourced from various online repositories (**[Provide Source]**) to ensure coverage of different lobster types. Backgrounds were removed to facilitate synthetic augmentation.

---

## 🎨 Synthetic Data Augmentation

Given the **few-shot segmentation task**, we augmented the dataset to improve model generalization across various environments. Our augmentation strategy involved:

### 1. Background Replacement
- Extracted lobsters were placed on diverse underwater and offshore backgrounds.
- This simulates real-world environments where the lobsters might appear.

### 2. Lobster Type Diversity
We ensured that our dataset contains a broad variety of lobster types to improve generalization:
- **Male Lobsters**
- **Female Lobsters**
- **Egg-Bearing (Berried) Lobsters** (Primary focus for segmentation)

### 3. Feature Emphasis
To improve segmentation of egg-bearing lobsters, we applied targeted augmentations that emphasized key body parts:
- **Abdomen Region** – This is typically distended in berried lobsters due to the egg mass.
- **Swimmerets (Pleopods)** – The small limbs under the tail that carry the eggs.

---

## 🦞 Purpose & Application

The primary goal of this dataset is to train few-shot segmentation models for **automated detection of egg-bearing lobsters**. This work is critical for:
- **Marine conservation efforts** – Ensuring egg-bearing lobsters are protected during their breeding phase.
- **Real-time monitoring** – Developing lightweight and deployable segmentation models for mobile and
