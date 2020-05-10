'''
Function:
	setup
Author:
	Charles
微信公众号:
	Charles的皮卡丘
GitHub:
	https://github.com/CharlesPikachu
更新日期:
	2020-03-08
'''
import hackcaptcha
from setuptools import setup, find_packages


'''readme'''
with open('README.md', 'r', encoding='utf-8') as f:
	long_description = f.read()


'''setup'''
setup(
	name='hackcaptcha',
	version=hackcaptcha.__version__,
	description='Provide api functions for captcha recognition.',
	long_description=long_description,
	long_description_content_type='text/markdown',
	classifiers=[
			'License :: OSI Approved :: MIT License',
			'Programming Language :: Python :: 3',
			'Intended Audience :: Developers',
			'Operating System :: OS Independent'],
	author='Charles',
	url='https://github.com/CharlesPikachu/hackcaptcha',
	author_email='charlesjzc@qq.com',
	license='MIT',
	include_package_data=True,
	install_requires=['opencv-python >= 4.1.2', 'requests >= 2.22.0', 'keras >= 2.2.4', 'numpy >= 1.16.2'],
	zip_safe=True,
	packages=find_packages()
)