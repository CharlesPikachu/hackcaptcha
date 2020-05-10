'''
Function:
	12306验证码破解
Author:
	Charles
微信公众号:
	Charles的皮卡丘
GitHub:
	https://github.com/CharlesPikachu
更新日期:
	2020-05-10
'''
import cv2
import keras
import numpy as np


'''all texts'''
TEXTS = ['打字机', '调色板', '跑步机', '毛线', '老虎', '安全帽', '沙包', '盘子', '本子', '药片',
		 '双面胶', '龙舟', '红酒', '拖把', '卷尺', '海苔', '红豆', '黑板', '热水袋', '烛台', '钟表',
		 '路灯', '沙拉', '海报', '公交卡', '樱桃', '创可贴', '牌坊', '苍蝇拍', '高压锅', '电线', '网球拍',
		 '海鸥', '风铃', '订书机', '冰箱', '话梅', '排风机', '锅铲', '绿豆', '航母', '电子秤', '红枣', '金字塔',
		 '鞭炮', '菠萝', '开瓶器', '电饭煲', '仪表盘', '棉棒', '篮球', '狮子', '蚂蚁', '蜡烛', '茶盅', '印章', '茶几',
		 '啤酒', '档案袋', '挂钟', '刺绣', '铃铛', '护腕', '手掌印', '锦旗', '文具盒', '辣椒酱', '耳塞', '中国结', '蜥蜴',
		 '剪纸', '漏斗', '锣', '蒸笼', '珊瑚', '雨靴', '薯条', '蜜蜂', '日历', '口哨']


'''zt12306 cracker'''
class Zt12306Cracker():
	def __init__(self, **kwargs):
		self.info = 'zt12306 cracker for click captcha.'
	'''外部调用的识别函数'''
	def recognize(self, imagepath, **kwargs):
		text_model_path, object_model_path = kwargs.get('text_model_path', ''), kwargs.get('object_model_path', '')
		assert text_model_path and object_model_path
		# 定义返回的信息
		infos_return = {'is_success': False, 'result': ''}
		# 读取图片
		image = cv2.imread(imagepath)
		image_text = self.__getImageText(image)
		image_objects = self.__getImageObjects(image)
		# 识别文字
		text_results = []
		text_model = keras.models.load_model(text_model_path)
		label = text_model.predict(image_text).argmax()
		result = TEXTS[label]
		text_results.append(result)
		offset = {1: 27, 2: 47, 3: 60}.get(len(text))
		image_text = self.__getImageText(image, offset)
		if image_text.mean() < 0.95:
			label = text_model.predict(image_text).argmax()
			result = TEXTS[label]
			text_results.append(result)
		# 识别目标
		object_model = keras.models.load_model(object_model_path)
		labels = object_model.predict(image_objects)
		labels = labels.argmax(axis=1)
		# 文字所指的类别匹配目标类别
		results = []
		for idx, label in enumerate(labels):
			if TEXTS[label] in text_results:
				results.append(idx+1)
		infos_return.update({'result': ','.join(results)})
		# 返回识别结果
		return infos_return
	'''获取文字部分的图片'''
	def __getImageText(self, image, offset=0):
		image_text = image[3: 22, 120+offset: 177+offset]
		image_text = cv2.cvtColor(image_text, cv2.COLOR_BGR2GRAY) / 255.0
		image_text = image_text.reshape(1, image_text.shape[0], image_text.shape[1], 1)
		return image_text
	'''获取目标部分的图片'''
	def __getImageObjects(self, image, interval=5, length=67):
		image_objects = []
		for i in range(40, image.shape[0]-length, interval+length):
			for j in range(interval, image.shape[1]-length, interval+length):
				image_object = image[i: i+length, j: j+length]
				image_object -= [103.939, 116.779, 123.68]
				image_objects.append(image_object)
		return image_objects
	'''repr'''
	def __repr__(self):
		return self.info