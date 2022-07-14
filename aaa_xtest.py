import xtest
import click
from xtest import data,file_data,data_class

# 参数化类
# @data_class(
#     ("name","keyword"),
#     [("case1","测试"),
#     ("case2","unitest")]
# )

# class BaiduTest(xtest.TestCase):
#
#     # 参数化方法
#     # @file_data("data.csv",line=1)
#     #
#     def test_baidu(self):
#         # print("keyword-->",keyword)
#         self.open("http://www.baidu.com")
#         self.type(tag="input",index=7,text="xtest")
#         self.click(css="#su")
#         # print(self.get_title)
#         self.sleep(2)
#         # self.assertEqual(self.get_title,keyword+"_百度搜索")
#         # self.assert_title(keyword+"_百度搜索")
#         # self.assert_Intitle(keyword)
#         # self.assertInUrl("wd=xtest")
#         self.assertText(css="div > h3 > a",index=0,text="xtest - Bing 词典22")


    # def test_baidu2(self):
    #     self.open("http://www.baidu.com")
    #     self.type(id_="kw",text="xtest框架")
    #     self.click(css="#su")
    #     self.sleep(2)
    #     # text = self.get_text(class_name="s-bottom-layer-content")
    #     # print(text)



if __name__ == '__main__':
    run()


