# FireDetection training 

## Installation
```
Tested on python 3.10.11
pip install -r magai_main0.txt --no-deps
withGPU :- conda install pytorch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 pytorch-cuda=12.4 -c pytorch -c nvidia
           or pip install torch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 --index-url https://download.pytorch.org/whl/cu124

without GPU :- conda install pytorch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 cpuonly -c pytorch
          or pip install torch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 --index-url https://download.pytorch.org/whl/cpu

```
## Infrence 
```
python main.py
```