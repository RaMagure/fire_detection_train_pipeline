from pipeline.traning_pipeline import TrainModel

def main():
    TrainModel(model_path="models/firedetect-11s.pt",batch_size=64,data_path_url="https://drive.google.com/file/d/1yM4ududikzC2PYyeUIZP4TypgGzwSF2z/view?usp=drive_link").train()
    pass


if __name__ == "__main__":
    main()