# 算法破解

## 点击验证码
#### zt12306
调用zt12306进行点击验证码识别的代码示例如下:
```
from hackcaptcha.crackers import AlgorithmsCracker
cracker = AlgorithmsCracker()
infos_return = cracker.click(imagepath='CAPTCHA IMAGE PATH', algorithm_type='zt12306', text_model_path='text.h5', object_model_path='object.h5')
```
返回的结果示例:
```
{
    'is_success': True, 
    'result': '1,2,5'
}
```

## 数字验证码
```
暂不支持
```

## 滑块验证码
#### Canny算子
调用Canny算子进行滑块验证码识别的代码示例如下:
```
from hackcaptcha.crackers import AlgorithmsCracker
cracker = AlgorithmsCracker()
infos_return = cracker.slider(imagepath='CAPTCHA IMAGE PATH', algorithm_type='canny')
```
返回的结果示例:
```
{
    'is_success': True, 
    'result': [cx, cy, w, h], 
    'tip': 'the format of the result is (cx, cy, w, h)'
}
```
