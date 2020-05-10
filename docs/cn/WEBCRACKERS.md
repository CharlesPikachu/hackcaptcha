# 接口破解

## 点击验证码
```
暂不支持
```

## 数字验证码
#### 百度API
调用百度API进行数字验证码识别的代码示例如下:
```
from hackcaptcha.crackers import WebapisCracker
cracker = WebapisCracker()
infos_return = cracker.digital(imagepath='CAPTCHA IMAGE PATH', webapi_type='baidu', app_id='AppID', api_key='API Key', secret_key='Secret Key')
```
返回的结果示例:
```
{
    'is_success': True,
    'result': 'AFD2',
    'error_msg': ''
}
```

## 滑块验证码
```
暂不支持
```