# Install

## Environment
The environment I used is:
- OS: Win10
- GPU: 1050ti
- Python: 3.6.4

## Dependency package 
Dependencies requirement:
```
numpy >= 1.16.2
requests >= 2.22.0
opencv-python >= 4.1.2
keras >= 2.2.4 and the corresponding tensorflow/tensorflow-gpu
```

## Pip install
Just run the following command:
```sh
pip install hackcaptcha --upgrade
```

## Source code install
#### Online
Just run the following command:
```sh
pip install git+https://github.com/CharlesPikachu/hackcaptcha.git@master
```
#### Offline
First, clone the project:
```sh
git clone https://github.com/CharlesPikachu/hackcaptcha.git
```
Then, run the following command:
```sh
cd hackcaptcha
```
Finally, run the following command to install:
```sh
python setup.py install
```