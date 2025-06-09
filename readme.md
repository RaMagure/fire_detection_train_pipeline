# Crowd Estimation 

## Installation
```
Tested on python 3.10.11
pip install -r magai_main0.txt --no-deps
withGPU :- conda install pytorch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 pytorch-cuda=12.4 -c pytorch -c nvidia
           or pip install torch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 --index-url https://download.pytorch.org/whl/cu124

without GPU :- conda install pytorch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 cpuonly -c pytorch
          or pip install torch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 --index-url https://download.pytorch.org/whl/cpu

```

## Inference
```
for image:-  python -m fast_and_paced --target-image-path "Path to input image .jpg/.png file"
for Video:-  python -m fast_and_paced --Video_feed "D:\padme_model\videos\fast_and_paced.mp4"
```

## Test
```
python start_server.py --run-test True
Note - Have to install dependencies manually now as the module is not integrated.
```