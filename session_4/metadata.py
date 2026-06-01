# Paths
MODELS_FOLDER = "session_4/models"
DATASETS_FOLDER = "session_4/datasets"

# The exercise asks for the model file to be named:
# class_model-{your_name}-{timestamp}.joblib
MODEL_NAME = "class_model-nicoputs"

# Columns configuration for the bank-full dataset
COLUMNS_TO_DROP = []
BINARY_FEATURES = [
    "housing",
    "loan",
    "default",
]
ONE_HOT_ENCODE_COLUMNS = [
    "marital",
    "job",
    "education",
    "poutcome",
    "contact",
]

# Decision tree model parameters
MODEL_PARAMS = {
    "criterion": "gini",
    "max_depth": 10,
    "random_state": 8888,
}
