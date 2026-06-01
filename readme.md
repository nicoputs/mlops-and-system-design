# MLOps and System Design — Nicolás Santis Rojas

This repository contains the exercises and activities developed during the MLOps and System Design course.

---

# Repository Structure

```text
.github/workflows/
session_1/
session_2/
session_3/
session_4/
README.md
requirements.txt
```

---

# Session 1 — Git & GitHub Fundamentals

## Objective

Practice the basic workflow of version control using Git and GitHub.

## Activities

- Creating a GitHub repository
- Working with branches
- Making commits
- Pushing changes to GitHub
- Understanding pull requests and merge workflows

## Technologies Used

- Git
- GitHub
- Python

---

# Session 2 — ML Pipeline & MLflow

## Objective

Build a simple Machine Learning workflow for customer churn prediction and track experiments using MLflow.

## Activities

- Exploratory Data Analysis (EDA)
- Data preprocessing
- Feature engineering
- Training Machine Learning models
- Evaluating model performance
- Tracking experiments with MLflow

## Models Used

- Decision Tree Classifier
- Random Forest Classifier

## Technologies Used

- Python
- Pandas
- Scikit-learn
- MLflow
- Jupyter Notebook

## Evidence

The `session_2/mlflow/` folder contains screenshots of the MLflow experiments and model metrics.

---

# Session 3 — Model Deployment & Inference

## Objective

Implement a basic model deployment workflow using a model trained and tracked in MLflow. This session focuses on loading an existing MLflow model and using it for both batch inference and online inference.

## Activities

- Reusing MLflow experiments from Session 2
- Loading a trained model from MLflow using its model URI
- Preparing validation data for inference
- Applying the same preprocessing logic used during training
- Running batch inference on a validation dataset
- Serving the model locally with MLflow
- Sending online inference requests to the local model endpoint
- Validating the model response through a successful API request

## Files

- `ejercicio 3.ipynb`: Deployment and inference notebook
- `ejercicio 3 test.csv`: Dataset used for model preparation
- `ejercicio 3 val.csv`: Validation dataset used for inference testing

## Inference Methods

- Batch inference using `mlflow.pyfunc.load_model()`
- Online inference using a local MLflow model server and HTTP requests

## Technologies Used

- Python
- Pandas
- Scikit-learn
- MLflow
- Requests
- Jupyter Notebook

## Result

The online inference endpoint successfully returned a prediction with status code `200`, confirming that the model was served locally and was able to respond to inference requests.

---

# Session 4 — ML Pipeline Automation with CI/CD

## Objective

Build a modular Machine Learning pipeline and automate its testing and deployment using GitHub Actions (Continuous Integration and Continuous Deployment).

## Activities

- Structuring the ML pipeline into separate modules (load, transform, train, store)
- Loading and balancing the dataset
- Transforming the data (binary mapping, month mapping, one-hot encoding)
- Training a Decision Tree model
- Saving the trained model with a timestamped file name
- Writing unit tests for the data transformer with pytest
- Configuring a Continuous Integration (CI) workflow
- Configuring a Continuous Deployment (CD) workflow
- Opening a pull request and validating the workflow runs

## Pipeline Structure

```text
session_4/
├── datasets/        # Input dataset
├── models/          # Trained models (generated automatically)
├── src/
│   ├── load.py      # Loads the CSV dataset
│   ├── transform.py # Data transformation and balancing
│   ├── train.py     # Trains the Decision Tree model
│   └── store.py     # Saves the trained model
├── tests/
│   └── test_transformer.py  # Unit tests for the transformer
├── main.py          # Orchestrates the full pipeline
└── metadata.py      # Constants, paths and model parameters
```

## Models Used

- Decision Tree Classifier

## CI/CD Workflows

The workflows are defined in the `.github/workflows/` folder.

- `ci.yaml` (Continuous Integration): runs on every pull request to `main`. It installs dependencies, runs the tests with pytest, formats the code with black, and commits the formatting changes back to the branch.
- `cd.yaml` (Continuous Deployment): runs on every push to `main` and on a weekly schedule (every Sunday at midnight). It installs dependencies, executes the pipeline, and commits the newly generated model to the repository.

## Technologies Used

- Python
- Pandas
- Scikit-learn
- pytest
- black
- GitHub Actions (CI/CD)

## Result

Both workflows ran successfully. The CI workflow validated the tests and formatted the code, and the CD workflow generated and committed a new trained model into the `session_4/models/` folder automatically.

---
