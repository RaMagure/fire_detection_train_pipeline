from pipeline.traning_pipeline import TrainModel

def main():
    train=TrainModel(model_path="models/firedetect-11s.pt",batch_size=64,data_path_url="https://drive.google.com/drive/folders/10k5qeGudeWV7_gJHQvQWHFu-whnOM8PV?usp=drive_link")
    train.train()
    pass


if __name__ == "__main__":
    main()