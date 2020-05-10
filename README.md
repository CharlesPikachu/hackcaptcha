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
|  Digital             |   0								 |    1                                  |   数字验证码    |
|  Click               |   1								 |    0                                  |   点击验证码    |


# Install
#### Pip install
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
infos_return = cracker.click(imagepath='CAPTCHA IMAGE PATH', algorithm_type='zt12306', text_model_path='text.h5', object_model_path='object.h5')
```
#### hack captcha by webapis
```
from hackcaptcha.crackers import WebapisCracker

cracker = WebapisCracker()
# slider captcha
# digital captcha
infos_return = cracker.digital(imagepath='CAPTCHA IMAGE PATH', webapi_type='baidu', app_id='AppID', api_key='API Key', secret_key='Secret Key')
# click captcha
```

# References
```
[1]. https://github.com/zhaipro/easy12306
```

# More
#### WeChat Official Accounts
*Charles_pikachu*  
![img](pikachu.jpg)