"""Training-only preprocessing used for the October comparison.

This is the pipeline in notebooks/OctoberMilestones/October_Gate_3.ipynb.
Fit it on training rows only, then call transform on validation rows.
"""

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


def build_preprocessor(numeric_features, categorical_features):
    """Median-fill numbers and one-hot encode categories.

    numeric_features and categorical_features are the column names from
    field_roles.csv. id and loss stay out of both lists.
    """
    numeric_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median"))
    ])
    categorical_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
    ])
    return ColumnTransformer([
        ("numeric", numeric_pipeline, numeric_features),
        ("categorical", categorical_pipeline, categorical_features),
    ])
