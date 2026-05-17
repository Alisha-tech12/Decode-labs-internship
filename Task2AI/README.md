# Project 2: Iris Flower Classification Using K-Nearest Neighbors

A supervised machine learning project that classifies Iris flowers into three species (Setosa, Versicolor, Virginica) based on sepal and petal measurements using the K-Nearest Neighbors algorithm. This is the second project in the DecodeLabs Artificial Intelligence Training Program (Batch 2026).

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Learning Objectives](#learning-objectives)
3. [Dataset Description](#dataset-description)
4. [Algorithm Explanation](#algorithm-explanation)
5. [Installation Instructions](#installation-instructions)
6. [Code Walkthrough](#code-walkthrough)
7. [Results and Evaluation](#results-and-evaluation)
8. [Experimentation](#experimentation)
9. [Key Takeaways](#key-takeaways)
10. [Troubleshooting](#troubleshooting)
11. [References](#references)

---

## Project Overview

### What is this project?

This project builds a classification model that can identify three species of Iris flowers based on four physical measurements. The model learns patterns from example data rather than following explicit rules written by a programmer.

### Problem Statement

Given the sepal length, sepal width, petal length, and petal width of an Iris flower, predict whether it is a Setosa, Versicolor, or Virginica.

### Why this matters

Classification is one of the most common tasks in machine learning. Applications include:
- Medical diagnosis (disease vs no disease)
- Email filtering (spam vs not spam)
- Image recognition (cat vs dog)
- Fraud detection (legitimate vs fraudulent)

---

## Learning Objectives

After completing this project, you will understand:

| Concept | Description |
|---------|-------------|
| Supervised Learning | Training a model using labeled data |
| Train-Test Split | Separating data for training and evaluation |
| Feature Scaling | Normalizing data for distance-based algorithms |
| K-Nearest Neighbors | A simple instance-based learning algorithm |
| Confusion Matrix | Visualizing classification performance |
| Hyperparameter Tuning | Selecting the optimal K value |
| Model Evaluation | Measuring accuracy and interpreting results |

---

## Dataset Description

### Source

The Iris dataset is built into the scikit-learn library. It was introduced by statistician Ronald Fisher in 1936 and is considered the "Hello World" of machine learning.

### Dataset Statistics

| Property | Value |
|----------|-------|
| Total samples | 150 |
| Samples per class | 50 (perfectly balanced) |
| Number of features | 4 |
| Number of classes | 3 |
| Missing values | 0 |
| Data type | Numerical (continuous) |

### Features (Input Variables)

| Feature Name | Description | Range (cm) |
|--------------|-------------|-------------|
| Sepal length | Length of the outer flower part | 4.3 - 7.9 |
| Sepal width | Width of the outer flower part | 2.0 - 4.4 |
| Petal length | Length of the inner flower part | 1.0 - 6.9 |
| Petal width | Width of the inner flower part | 0.1 - 2.5 |

### Target Classes (Output Labels)

| Class Code | Species Name |
|------------|--------------|
| 0 | Setosa |
| 1 | Versicolor |
| 2 | Virginica |

### Sample Data

| Sepal Length | Sepal Width | Petal Length | Petal Width | Species |
|--------------|-------------|--------------|-------------|---------|
| 5.1 | 3.5 | 1.4 | 0.2 | Setosa |
| 7.0 | 3.2 | 4.7 | 1.4 | Versicolor |
| 6.3 | 3.3 | 6.0 | 2.5 | Virginica |

---

## Algorithm Explanation

### What is K-Nearest Neighbors (KNN)?

KNN is a simple, intuitive algorithm that makes predictions based on similarity. It does not learn a model during training; instead, it memorizes the training data and makes decisions at prediction time. This is called "lazy learning."

### How KNN Works

Step 1: Store all training data
Step 2: When a new flower needs classification, calculate its distance to every training sample
Step 3: Select the K closest neighbors
Step 4: Take a majority vote of their labels
Step 5: Assign the majority label to the new flower

### Visual Example

Suppose K = 5 and we have a new flower. The algorithm finds the 5 closest training flowers:

- Neighbor 1: Setosa
- Neighbor 2: Setosa
- Neighbor 3: Versicolor
- Neighbor 4: Setosa
- Neighbor 5: Setosa

Count: Setosa = 4, Versicolor = 1, Virginica = 0
Prediction: Setosa (majority vote)

### Distance Calculation

Euclidean distance is used to measure similarity:

Distance = sqrt((x1 - y1)^2 + (x2 - y2)^2 + (x3 - y3)^2 + (x4 - y4)^2)

Smaller distance means more similar flowers.

### Choosing the Right K

| K Value | Effect |
|---------|--------|
| Too small (K=1) | Sensitive to noise, may overfit |
| Too large (K=20) | May include irrelevant neighbors, underfit |
| Optimal (K=3-7) | Balances bias and variance |

For the Iris dataset, K=3 or K=5 works best.

---

## Installation Instructions

### Prerequisites

- Python 3.7 or higher installed on your system
- pip package manager

### Step 1: Install Required Libraries

Open terminal or command prompt and run:

```bash
pip install scikit-learn
pip install pandas
pip install numpy
