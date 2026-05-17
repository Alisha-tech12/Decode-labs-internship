# STEP 1: Import required libraries
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

# STEP 2: Load the dataset
print("PROJECT 2: DATA CLASSIFICATION USING AI")
print("Iris Flower Classification with KNN")

iris = load_iris()

print(f"\nDataset shape: {iris.data.shape}")
print(f"Number of samples: {len(iris.data)}")
print(f"Number of features: {len(iris.feature_names)}")
print(f"Features: {iris.feature_names}")
print(f"Target classes: {iris.target_names}")

df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target
df['species_name'] = df['species'].map({0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'})

print("\nFirst 5 rows of the dataset:")
print(df.head())

print("\nClass distribution:")
print(df['species_name'].value_counts())

# STEP 3: Split data into features (X) and target (y)
X = iris.data  # Features (sepal length, sepal width, petal length, petal width)
y = iris.target  # Target (0=Setosa, 1=Versicolor, 2=Virginica)

# STEP 4: Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.3,      
    random_state=42,    
    stratify=y          
)

print(f"\nTraining set size: {len(X_train)} samples")
print(f"Testing set size: {len(X_test)} samples")

# STEP 5: Scale the features (CRITICAL for KNN)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  
X_test_scaled = scaler.transform(X_test)        

print("\nFeature scaling completed:")
print(f"Training data mean (after scaling): {X_train_scaled.mean():.10f}")
print(f"Training data std (after scaling): {X_train_scaled.std():.2f}")

# STEP 6: Create and train the KNN model
k_value = 5
model = KNeighborsClassifier(n_neighbors=k_value)
model.fit(X_train_scaled, y_train)

print(f"\nModel: K-Nearest Neighbors (K={k_value})")
print("Model trained successfully!")

# STEP 7: Make predictions
y_pred = model.predict(X_test_scaled)

# STEP 8: Evaluate the model
print("\n" + "=" * 50)
print("MODEL EVALUATION RESULTS")
print("=" * 50)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"\nAccuracy: {accuracy:.4f} ({accuracy * 100:.2f}%)")

# Confusion Matrix
print("\nConfusion Matrix:")
print("(Rows = Actual, Columns = Predicted)")
print("Order: Setosa (0), Versicolor (1), Virginica (2)")
cm = confusion_matrix(y_test, y_pred)
print(cm)

# Interpret confusion matrix
print("\nConfusion Matrix Interpretation:")
print(f"Setosa correctly classified: {cm[0][0]} out of {sum(cm[0])}")
print(f"Versicolor correctly classified: {cm[1][1]} out of {sum(cm[1])}")
print(f"Virginica correctly classified: {cm[2][2]} out of {sum(cm[2])}")

# Detailed classification report
print("\nDetailed Classification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# STEP 9: Test with a new flower (your own input)

print("TEST WITH A CUSTOM FLOWER")

def predict_flower(sepal_length, sepal_width, petal_length, petal_width):
    """Predict the species of a flower based on measurements"""
    new_flower = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    new_flower_scaled = scaler.transform(new_flower)
    prediction = model.predict(new_flower_scaled)[0]
    species = iris.target_names[prediction]
    
    # Get distances to nearest neighbors for confidence
    distances, indices = model.kneighbors(new_flower_scaled)
    
    return species, distances[0]

# Example predictions
print("\nExample 1: Small petals (likely Setosa)")
species, distances = predict_flower(5.0, 3.5, 1.4, 0.2)
print(f"Measurements: [5.0, 3.5, 1.4, 0.2]")
print(f"Predicted: {species}")
print(f"Distance to 5 nearest neighbors: {[round(d, 3) for d in distances]}")

print("\nExample 2: Large petals (likely Virginica)")
species, distances = predict_flower(6.5, 3.0, 5.5, 2.0)
print(f"Measurements: [6.5, 3.0, 5.5, 2.0]")
print(f"Predicted: {species}")

print("\nExample 3: Medium petals (likely Versicolor)")
species, distances = predict_flower(6.0, 2.8, 4.5, 1.3)
print(f"Measurements: [6.0, 2.8, 4.5, 1.3]")
print(f"Predicted: {species}")

# STEP 10: Experiment with different K values

print("EXPERIMENT: DIFFERENT K VALUES")


print("\nK value | Accuracy")
print("-" * 25)
for k in [1, 3, 5, 7, 9, 11, 15]:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train_scaled, y_train)
    pred = knn.predict(X_test_scaled)
    acc = accuracy_score(y_test, pred)
    print(f"   {k}    |   {acc:.4f}")
