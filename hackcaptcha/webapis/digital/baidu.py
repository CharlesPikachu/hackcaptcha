'''
Function:
	利用百度提供的接口进行数字验证码识别
Author:
	Charles
微信公众号:
	Charles的皮卡丘
GitHub:
	https://github.com/CharlesPikachu
更新日期:
	2020-05-05
'''
import urllib
import base64
import requests


'''baiduapi cracker'''
class BaiduAPICracker():
	def __init__(self, **kwargs):
		self.info = 'baiduapi cracker for digital captcha.'
		self.token_url = 'https://aip.baidubce.com/oauth/2.0/token'
		self.ocr_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token=%s'
	'''外部调用的识别函数'''
	def recognize(self, imagepath, **kwargs):
		# 定义返回的信息
		infos_return = {'is_success': False, 'result': '', 'error_msg': ''}
		# 获得token
		app_id, api_key, secret_key = kwargs.get('app_id', ''), kwargs.get('api_key', ''), kwargs.get('secret_key', '')
		data = {
					'grant_type': 'client_credentials',
					'client_id': api_key,
					'client_secret': secret_key
				}
		access_token = requests.post(self.token_url, data=data).json()['access_token']
		# 调用api识别验证码
		headers = {'Content-Type': 'application/x-www-form-urlencoded'}
		data = urllib.parse.urlencode({'image': base64.b64encode(open(imagepath, 'rb').read())})
		response = requests.post(self.ocr_url % access_token, headers=headers, data=data)
		if response.status_code == 200:
			response_json = response.json()
			if 'error_msg' in response_json:
				infos_return.update({'error_msg': response_json['error_msg']})
			else:
				result = self.__filterResult(response_json['words_result'][0]['words'])
				infos_return.update({'is_success': True, 'result': result})
		# 返回必要的数据
		return infos_return
	'''filter result'''
	def __filterResult(self, result):
		result_filtered = []
		for c in result:
			if c.isdigit() or c.isalpha():
				result_filtered.append(c)
		return ''.join(result_filtered)
	'''repr'''
	def __repr__(self):
		return self.info