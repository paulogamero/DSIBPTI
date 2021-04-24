# Atividade final do módulo - EX1
# Autor: Newmar Wegner, Paulo, Kleberson
# Date: 23/05/2021

from pickle import dump
import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn import preprocessing, metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


# Function to normalize data considering Min Max Scaler sklearn
def normalize_data_minmax(df):
    normalizer = preprocessing.MinMaxScaler()

    return normalizer.fit(df), normalizer.fit_transform(df)

# Function to normalize dummy data
def normalize_data_dummies(df):
    return pd.get_dummies(df, prefix=df.columns)


# function to create categorical and numerical dataset
def create_num(df, class_column):
    numerical = df.drop(columns=class_column, axis=1)

    return numerical


# Function to Balance dataset
def balance_data(final_data, class_column):
    x, y = final_data.iloc[:, :-1], final_data[class_column]
    oversample = SMOTE()

    return oversample.fit_resample(x, y)


# Function to save model
def save_model(model):
    return dump(model, open(f'../Aula10_04_21/model_diabetes.pkl', 'wb'))


if __name__ == '__main__':
    # Input parameters
    df = pd.read_csv('../dataset/diabetes.csv', sep=',')
    class_column = ['class',]

    # print(create_num(df, class_column))
    # Creating categorical and numerical dataset
    numerical = create_num(df, class_column)

    # Numerical dataset to normalize with minmax scaler
    model, num_normalize = normalize_data_minmax(numerical)
    num_normalize = pd.DataFrame(num_normalize, columns=numerical.columns)

    # Saving normalizer
    dump(model, open(f'../dataset/MinMaxScaler_diabetes.pkl', 'wb'))

    # Saving final normalizer dataset
    final_data = num_normalize.join(df['class'], how='left')
    final_data.to_csv(f"../dataset/diabetes_normalize.csv", index=False, sep=';')

    # Get balanced dataset
    x_oversample, y_oversample = balance_data(final_data, class_column)

    # Slice test and train data
    X_train, X_test, Y_train, Y_test = train_test_split(x_oversample, y_oversample, test_size=0.3)

    # Get model
    rf_diabetes = RandomForestClassifier().fit(X_train, Y_train.values.ravel())
    Clas
    # Test predict
    y_predict = rf_diabetes.predict(X_test)
    print(y_predict)

    # Accuracy: compare y_predict with Y_test
    print(f'Global Accuracy RandomForest: {round(metrics.accuracy_score(Y_test, y_predict), 3)}')

    # Save model
    save_model(rf_diabetes)