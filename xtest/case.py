import unittest
from xtest.webdriver import WebDriver
from .config import XTest

class TestCase(unittest.TestCase,WebDriver):

    def assert_title(self,title=None):
        """
        断言当前标题是否是title
        :param title:
        :return:
        """
        if title is None:
            raise NameError("title不能为空")
        Now_title =XTest.driver.title
        self.assertEqual(Now_title,title)

    def assert_Intitle(self,title=None):
        """
        断言当前标题是否包含title
        :param title:
        :return:
        """
        if title is None:
            raise NameError("title不能为空")
        Now_title =XTest.driver.title
        self.assertIn(title,Now_title)

    def assertUrl(self,url):
        """
        断言当前当前网址是否为url
        :param title:
        :return:
        """
        if url is None:
            raise NameError("url不能为空")
        Now_url =XTest.driver.current_url
        self.assertEqual(url,Now_url)

    def assertInUrl(self,url):
        """
        断言当前当前网址是否为url
        :param url:
        :return:
        """
        if url is None:
            raise NameError("url不能为空")
        Now_url =XTest.driver.current_url
        self.assertIn(url,Now_url)

    def assertText(self,text,index=None,**kwargs):
        """
        断言元素文本
        :param url:
        :return:
        """
        if text is None:
            raise NameError("元素文本不能为空")
        element_text =self.get_text(**kwargs,index=index)
        self.assertEqual(element_text,text)