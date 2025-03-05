# Aquaseg_Lobster_Dataset
This repository contains datasets for few-shot segmentation of lobsters, specifically focusing on egg-bearing (berried) lobsters. The dataset supports marine life conservation efforts by improving automated detection and segmentation of lobsters in varying aquatic environments.
📌 Data Sources

To ensure diversity in the dataset, we sourced lobsters from different environments and curated synthetic data:

    Underwater Lobster Dataset – [Provide Source]
    Offshore Lobster Dataset – [Provide Source]
    Male, Female & Egg-Bearing Lobsters – Sourced from various online datasets ([Provide Source]) and used for synthetic data augmentation.

🎨 Synthetic Data Augmentation

Since few-shot segmentation requires adaptable models that generalize well to new environments, synthetic data was generated to diversify the dataset and improve model robustness. The process involved:

    Background Replacement: Extracted lobsters were placed onto varied underwater and offshore backgrounds to simulate real-world conditions.
    Lobster Type Variability: Ensuring coverage of different lobster categories:
        Male Lobsters
        Female Lobsters
        Egg-Bearing (Berried) Lobsters (Primary focus for segmentation)
    Feature Emphasis: Augmenting specific body parts such as the abdomen and swimmerets, which are crucial for distinguishing egg-bearing lobsters.

🦞 Purpose & Application

This dataset is developed for few-shot segmentation models and will be used in a cross-platform  application designed for automated detection of egg-bearing lobsters. The goal is to aid in marine conservation efforts by providing a lightweight, deployable segmentation model for real-world monitoring.
