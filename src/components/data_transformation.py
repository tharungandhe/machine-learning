import pandas as pd
from sklearn.preprocessing import StandardScaler

class DataTransformation:
    def initiate_data_transformation(self, train_path, test_path):

        train_df = pd.read_csv(train_path)
        test_df = pd.read_csv(test_path)

        # Automatically take last column as target
        target_column = train_df.columns[-1]

        X_train = train_df.drop(columns=[target_column])
        y_train = train_df[target_column]

        X_test = test_df.drop(columns=[target_column])
        y_test = test_df[target_column]

        X_train = pd.get_dummies(X_train)
        X_test = pd.get_dummies(X_test)

        X_train, X_test = X_train.align(X_test, join="left", axis=1, fill_value=0)

        scaler = StandardScaler()

        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

        print("Data Transformation Completed")

        return X_train, X_test, y_train, y_test
