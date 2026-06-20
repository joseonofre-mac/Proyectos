import cv2
import numpy as np
import os
from config import IMAGE_SIZE, FRAME_FOLDER, SAVE_KEYFRAMES

def segundos_a_hhmmss(segundos):
    horas = int(segundos // 3600)
    minutos = int((segundos % 3600) // 60)
    segs = int(segundos % 60)
    return f"{horas:02}:{minutos:02}:{segs:02}"

def extraer_histograma(frame, bins=64):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hist = cv2.calcHist([gray], [0], None, [bins], [0, 256])
    cv2.normalize(hist, hist)
    return hist.flatten()

def procesar_video(video_path, step_seconds=1, bins=64):
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_step = int(fps * step_seconds)

    features = []
    tiempos = []

    if SAVE_KEYFRAMES and not os.path.exists(FRAME_FOLDER):
        os.makedirs(FRAME_FOLDER)

    for frame_index in range(0, total_frames, frame_step):
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
        ret, frame = cap.read()
        if not ret:
            break

        # Redimensionar si se definió IMAGE_SIZE
        if IMAGE_SIZE:
            frame = cv2.resize(frame, IMAGE_SIZE)

        hist = extraer_histograma(frame, bins)
        segundo = frame_index / fps
        tiempo_str = segundos_a_hhmmss(segundo)

        features.append(hist)
        tiempos.append(tiempo_str)

    cap.release()
    return np.array(features), tiempos
