# Webapis

## Click Captcha
```
Unsupported now.
```

## Digital Captcha
#### Baidu API
Here is an example:
```
from hackcaptcha.crackers import WebapisCracker
cracker = WebapisCracker()
infos_return = cracker.digital(imagepath='CAPTCHA IMAGE PATH', webapi_type='baidu', app_id='AppID', api_key='API Key', secret_key='Secret Key')
```
the format of infos_return is:
```
{
    'is_success': True,
    'result': 'AFD2',
    'error_msg': ''
}
```

## Slider Captcha
```
Unsupported now.
```