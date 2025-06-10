import torch
import os
from ultralytics import YOLO
import cv2
import random
import shutil
import numpy as np
from ultralytics import YOLO
from .utils import is_data_yaml_present_and_extract_7z , download_to_data_folder

print(torch.__version__)
os.environ['TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD'] = '1'
print("CUDA available:", torch.cuda.is_available())


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class LoadModel:
    def __init__(self, model_base_path: str = None, device: str = "cuda"):
        if model_base_path is None:
            raise ValueError("Model base path must be provided.")
        self.model = YOLO(model_base_path)
        self.device = device
        self.model.to(device)

    def __call__(self, *args, **kwargs):
        return self.model(*args, **kwargs)

    def train(self, *args, **kwargs):  # 🔧 Add this line
        return self.model.train(*args, **kwargs)


    

class TrainModel:
    def __init__(self, model_path:str, data_path_url: str, epochs: int = 100, batch_size: int = 16, device: str = "cuda"):
        self.model = LoadModel(model_base_path=model_path, device=device)
        self.epochs = epochs
        self.batch_size = batch_size
        self.device = device
        self.data_path=download_to_data_folder(data_path_url,filename='fireDetection.7z')

    def train(self):
        self.model.model.train(
        data=is_data_yaml_present_and_extract_7z(self.data_path),
        epochs=self.epochs,
        imgsz=640,
        device=[0, 1],
        batch=self.batch_size,
        optimizer="AdamW",
        lr0=0.001,
        weight_decay=0.01,
        warmup_epochs=3,
        project="fire_detection",
        name="yolov8-fire-adamw",
        pretrained=True,
        amp=True,
        early_stopping=True,
        patience=10
    )
        