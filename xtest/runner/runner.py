from xtest.config import XTest
from selenium import webdriver
import unittest,inspect
import os,time,webbrowser
from xtest.runner.htmlrunner.runner import HTMLTestRunner
from xtest.utils.webdriver_manager_extend import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from logzero import logger

browsers = ["chrome","firefox","ff","gc"]

xtest="""

 ___    ___ _________  _______   ________  _________   
|\  \  /  /|\___   ___\\  ___ \ |\   ____\|\___   ___\ 
\ \  \/  / ||___ \  \_\ \   __/|\ \  \___|\|___ \  \_| 
 \ \    / /     \ \  \ \ \  \_|/_\ \_____  \   \ \  \  
  /     \/       \ \  \ \ \  \_|\ \|____|\  \   \ \  \ 
 /  /\   \        \ \__\ \ \_______\____\_\  \   \ \__\
/__/ /\ __\        \|__|  \|_______|\_________\   \|__|
|__|/ \|__|                        \|_________|        

"""


def main(path=None,browser=None,timeout=10, debug=False, title=None, description=None):
    """
    入口方法
    :param path: 运行文件路径
    :param browser: 浏览器
    :param debug: 报告生成开关
    :param timeout: 超时时间
    :param title: 报告的名称
    :param Descrption: 报告描述
    :return: 
    """

    stack_t = inspect.stack()
    ins = inspect.getframeinfo(stack_t[1][0])
    run_path = os.path.dirname(os.path.abspath(ins.filename))
    # print("调用该类的当前路径--》",os.path.dirname(os.path.abspath(ins.filename)))

    logger.info(xtest)

    if browser is None:
        browser = "firefox"
    if browser not in browsers:
        raise NameError(f"不支持{browser}浏览器。")
    if browser in ["chrome","gc"]:
        XTest.driver = webdriver.Chrome(ChromeDriverManager().install())
    if browser in ["firefox","ff"]:
        XTest.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    # 全局超时时间
    XTest.timeout = timeout

    if path is None:
        path = os.getcwd()
    suit = unittest.defaultTestLoader.discover(start_dir=path)

    if debug is False:
        report_dir = os.path.join(run_path,"reports")
        if os.path.exists(report_dir) is False:
            os.mkdir(report_dir)

        # HTML格式报告，xml格式报告
        now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
        report_file = os.path.join(report_dir,f"{now_time}result2.html")
        with(open(report_file,'wb',))as fp:
            runner = HTMLTestRunner(stream=fp,title=title,description=description)
            # runer = unittest.TextTestRunner()
            runner.run(suit)
            logger.info(f"生成测试报告:{report_file}")
            webbrowser.open_new(f"file:///{report_file}")
    else:
        runner = unittest.TextTestRunner()
        runner.run(suit)

     # 全局关闭浏览器
    if XTest.driver is not None:
        XTest.driver.quit()




