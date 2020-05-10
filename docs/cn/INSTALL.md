# 安装

## 测试环境
本人测试时使用的环境如下:
- 操作系统: Win10
- 显卡: 1050ti
- Python版本: 3.6.4

## 依赖包 
hackcaptcha相关依赖包需求如下:
```
numpy >= 1.16.2
requests >= 2.22.0
opencv-python >= 4.1.2
keras >= 2.2.4以及和keras版本相对应的tensorflow/tensorflow-gpu
```

## PIP安装
在终端运行如下命令即可(请保证python在环境变量中):
```sh
pip install hackcaptcha --upgrade
```

## 源代码安装
#### 在线安装
运行如下命令即可在线安装:
```sh
pip install git+https://github.com/CharlesPikachu/hackcaptcha.git@master
```
#### 离线安装
利用如下命令下载hackcaptcha源代码到本地:
```sh
git clone https://github.com/CharlesPikachu/hackcaptcha.git
```
接着, 切到hackcaptcha目录下:
```sh
cd hackcaptcha
```
最后运行如下命令进行安装:
```sh
python setup.py install
```