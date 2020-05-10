# Algorithms

## Click Captcha
#### zt12306
Here is an example:
```
from hackcaptcha.crackers import AlgorithmsCracker
cracker = AlgorithmsCracker()
infos_return = cracker.click(imagepath='CAPTCHA IMAGE PATH', algorithm_type='zt12306', text_model_path='text.h5', object_model_path='object.h5')
```
the format of infos_return is:
```
{
    'is_success': True, 
    'result': '1,2,5'
}
```

## Digital Captcha
```
Unsupported now.
```

## Slider Captcha
#### Canny
Here is an example:
```
from hackcaptcha.crackers import AlgorithmsCracker
cracker = AlgorithmsCracker()
infos_return = cracker.slider(imagepath='CAPTCHA IMAGE PATH', algorithm_type='canny')
```
the format of infos_return is:
```
{
    'is_success': True, 
    'result': [cx, cy, w, h], 
    'tip': 'the format of the result is (cx, cy, w, h)'
}
```
