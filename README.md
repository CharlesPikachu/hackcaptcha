# hackcaptcha
```
Provide api functions for captcha recognition, this repo is created mainly for https://github.com/CharlesPikachu/DecryptLogin
You can star this repository to keep track of the project if it's helpful for you, thank you for your support.
```

# Documents
still on the way

# Support List
|  Captcha Type        |   Number of supported algorithms    |    Number of supported webapis        |   in Chinese    |
|  :----:              |   :----:                            |    :----:                             |   :----:        |
|  Slider              |   1								 |    0                                  |   滑块验证码    |
|  Digital             |   0								 |    0                                  |   数字验证码    |
|  Click               |   0								 |    0                                  |   点击验证码    |


# Install
#### Pip install(preparing)
```
run "pip install hackcaptcha"
```
#### Source code install
```sh
(1) Offline
Step1: git clone https://github.com/CharlesPikachu/hackcaptcha.git
Step2: cd hackcaptcha -> run "python setup.py install"
(2) Online
run "pip install git+https://github.com/CharlesPikachu/hackcaptcha.git@master"
```

# Quick Start
#### hack captcha by algorithms
```
from hackcaptcha.crackers import AlgorithmsCracker

cracker = AlgorithmsCracker()
# slider captcha
infos_return = cracker.slider(imagepath='CAPTCHA IMAGE PATH', algorithm_type='canny')
# digital captcha
# click captcha
```
#### hack captcha by webapis
```
from hackcaptcha.crackers import WebapisCracker

cracker = WebapisCracker()
# slider captcha
# digital captcha
# click captcha
```

# More
#### WeChat Official Accounts
*Charles_pikachu*  
![img](pikachu.jpg)