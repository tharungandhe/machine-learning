from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from src.utils import save_object

class ModelTrainer:

    def initiate_model_trainer(self, X_train, X_test, y_train, y_test):

        model = LinearRegression()
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)

        score = r2_score(y_test, y_pred)

        save_object("artifacts/model.pkl", model)
        print("Model Training Completed")
        print("R2 Score:", score)


        return score
