# Configuración global del proyecto

# Archivos de entrada
TRAIN_VIDEO = "train.mp4"
TRAIN_CSV = "train.csv"
TEST_VIDEO = "test.mp4"

# Carpeta de salida
OUTPUT_FOLDER = "outputs"
FRAME_FOLDER = "keyframes"

# CSV de salida para predicciones
TEST_OUTPUT_CSV = f"{OUTPUT_FOLDER}/test_resultados.csv"

# Parámetros de procesamiento
IMAGE_SIZE = (224, 224)   # Tamaño opcional si quieres redimensionar frames
STEP_SECONDS = 1          # Un frame por segundo
HIST_BINS = 64            # Número de bins para el histograma

# Modelo
N_ESTIMATORS = 100        # Número de árboles en RandomForest
RANDOM_STATE = 42         # Semilla para reproducibilidad

# Flags
SAVE_KEYFRAMES = True     # Guardar frames relevantes en FRAME_FOLDER
