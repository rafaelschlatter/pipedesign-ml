import os
from ml import preprocessor
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from apis.cache import cache


class Model():
    """This class holds a machine learning model which is exposed in the flask app.
    Client applications can request predictions from this model.
    """

    def __init__(self):
        """Constructor."""
        self.features = None
        self.classifier = None


    def train(self, training_data):
        """Trains a model on the given data.

        Args:
            training_data (pandas df): A dataframe containing training data for pipedesigns (namely geometry coordinates).

        Returns: A trained random forest classifier.
        """

        y = pd.factorize(training_data["viability.viable"])[0]
        clf = RandomForestClassifier(n_jobs=2, random_state=0)
        self.features = training_data.columns[5: ]
        clf.fit(training_data[self.features], y)
        self.classifier = clf


    def predict(self, json_data):
        """Returns a prediction for a single case, given the input data.

        Args:
            json_data (dictionary): Input data to make a prediction.
        """

        proc = preprocessor.Preprocessor()
        test_data_df = proc.flatten_pipesegments(json_data)
        label = self.classifier.predict(test_data_df[self.features])
        confidence = self.classifier.predict_proba(test_data_df[self.features])
        return label, confidence
