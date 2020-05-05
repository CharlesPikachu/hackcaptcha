'''
Function:
	使用canny算子识别滑块验证码滑块缺口位置, 推荐用于:
	--腾讯滑块验证码
Author:
	Charles
微信公众号:
	Charles的皮卡丘
GitHub:
	https://github.com/CharlesPikachu
更新日期:
	2020-03-08
'''
import cv2


'''canny cracker'''
class CannyCracker():
	def __init__(self, **kwargs):
		self.info = 'canny cracker for slider captcha.'
	'''外部调用的识别函数'''
	def recognize(self, imagepath, **kwargs):
		# 定义返回的信息
		infos_return = {'is_success': False, 'result': [], 'tip': 'the format of the result is (cx, cy, w, h)'}
		# 图片提取
		image = cv2.imread(imagepath)
		# 利用canny算子找滑块缺口位置
		image_gb = cv2.GaussianBlur(image, (5, 5), 0)
		image_canny = cv2.Canny(image_gb, 200, 400)
		contours, hierarchy = cv2.findContours(image_canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		for contour in contours:
			m = cv2.moments(contour)
			if m['m00'] == 0:
				continue
			cx, cy = m['m10']/m['m00'], m['m01']/m['m00']
			if (6000 < cv2.contourArea(contour) < 8000) and (370 < cv2.arcLength(contour, True) < 390):
				if cx < 400: continue
				x, y, w, h = cv2.boundingRect(contour)
				cx = x - w / 2
				cy = y - h / 2
				infos_return.update({'is_success': True, 'result': [cx, cy, w, h]})
				break
		# 返回必要的数据
		return infos_return
	'''repr'''
	def __repr__(self):
		return self.info