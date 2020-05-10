'''
Function:
	验证码识别, 主要服务于DecryptLogin库
Author:
	Charles
微信公众号:
	Charles的皮卡丘
GitHub:
	https://github.com/CharlesPikachu
更新日期:
	2020-05-05
'''
from . import webapis
from . import algorithms


'''借助图像算法破解'''
class AlgorithmsCracker(object):
	def __init__(self, **kwargs):
		self.info = 'algorithms cracker'
	'''滑块验证码'''
	def slider(self, imagepath, algorithm_type='canny', **kwargs):
		# 利用canny算子识别缺口
		if algorithm_type == 'canny':
			cracker = algorithms.slider.CannyCracker()
		# 不支持该算法类型则报错
		else:
			raise ValueError('Unsupport algorithm_type %s in AlgorithmsCracker.slider...' % algorithm_type)
		# 利用对应的cracker识别并返回结果
		return cracker.recognize(imagepath, **kwargs)
	'''点击验证码'''
	def click(self, imagepath, algorithm_type='zt12306', **kwargs):
		# 12306点击验证码
		if algorithm_type == 'zt12306':
			cracker = algorithms.click.Zt12306Cracker()
		# 不支持该算法类型则报错
		else:
			raise ValueError('Unsupport algorithm_type %s in AlgorithmsCracker.click...' % algorithm_type)
		# 利用对应的cracker识别并返回结果
		return cracker.recognize(imagepath, **kwargs)
	'''repr'''
	def __repr__(self):
		return self.info


'''借助一些开放的API进行破解'''
class WebapisCracker(object):
	def __init__(self, **kwargs):
		self.info = 'webapis cracker'
	'''数字验证码'''
	def digital(self, imagepath, webapi_type='baidu', **kwargs):
		# 利用百度提供的接口识别验证码
		if webapi_type == 'baidu':
			cracker = webapis.digital.BaiduAPICracker()
		# 不支持该算法类型则报错
		else:
			raise ValueError('Unsupport webapi_type %s in WebapisCracker.digital...' % webapi_type)
		# 利用对应的cracker识别并返回结果
		return cracker.recognize(imagepath, **kwargs)
	'''repr'''
	def __repr__(self):
		return self.info