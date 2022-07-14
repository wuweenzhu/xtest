# coding=utf-8
import re
import ast
from setuptools import setup, find_packages
from os.path import dirname, join, abspath



_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('xtest/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))
    print(version)


setup(
    name='xtest',
    version=version,
    url='https://github.com/wuweenzhu/xtest/',
    license='BSD',
    author='文竹测试',
    author_email='784653875@qq.com',
    description='WebUI/HTTP automation testing framework based on unittest.',
    long_description="",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'selenium>=4.0.0',
        'parameterized==0.8.1',
        'colorama>=0.4.4',
        'logzero>=1.7.0',
        'webdriver-manager>=3.8.0',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        "Topic :: Software Development :: Testing",
    ],
    entry_points='''
        [console_scripts]
        xtest=xtest.cli:main
    ''',
    py_modules=['whyteboard'],
    scripts=[
        'xtest/runner/html/heading-en.html',
        'xtest/runner/html/heading-zh-CN.html',
        'xtest/runner/html/mail.html',
        'xtest/runner/html/report-en.html',
        'xtest/runner/html/report-zh-CN.html',
        'xtest/runner/html/stylesheet.html',
        'xtest/runner/html/template.html',
    ],
)