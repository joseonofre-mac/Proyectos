import csv
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from config import TRAIN_VIDEO, TRAIN_CSV, TEST_VIDEO, TEST_OUTPUT_CSV, STEP_SECONDS, HIST_BINS, RANDOM_STATE, N_ESTIMATORS
from utils import procesar_video

def entrenar_modelo():
    # Procesar video de entrenamiento
    X_train, tiempos_train = procesar_video(TRAIN_VIDEO, step_seconds=STEP_SECONDS, bins=HIST_BINS)

    # Leer etiquetas
    df_labels = pd.read_csv(TRAIN_CSV)
    y_train = df_labels["relevante"].values

    # Entrenar modelo
    clf = RandomForestClassifier(n_estimators=N_ESTIMATORS, random_state=RANDOM_STATE)
    clf.fit(X_train, y_train)

    print("Modelo entrenado con train.mp4 y train.csv")
    return clf

def predecir_video(clf):
    # Procesar video de prueba
    X_test, tiempos_test = procesar_video(TEST_VIDEO, step_seconds=STEP_SECONDS, bins=HIST_BINS)

    # Predecir relevancia
    y_pred = clf.predict(X_test)

    # Guardar resultados
    with open(TEST_OUTPUT_CSV, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["segundo", "relevante"])
        for tiempo, label in zip(tiempos_test, y_pred):
            writer.writerow([tiempo, int(label)])

    print(f"Predicciones guardadas en {TEST_OUTPUT_CSV}")

if __name__ == "__main__":
    modelo = entrenar_modelo()
    predecir_video(modelo)
