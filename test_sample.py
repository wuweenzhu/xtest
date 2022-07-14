import xtest
class SampleTest(xtest.TestCase):
    def test_case(self):
        """a simple test case """
        self.open("http://www.baidu.com")
        self.assert_Intitle("百度一下")
        self.type(tag="input", index=7, text="xtest")
        self.click(css="#su")


if __name__ == '__main__':
    xtest.main(browser="ff",debug=False)