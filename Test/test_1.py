from selenium import webdriver
import unittest
import HtmlTestRunner

class GoogleSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="../driver/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_automation(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("youtube krishnaik")
        self.driver.find_element_by_name("btnK").click()

    def test_search_myname(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("anilkumar")
        self.driver.find_element_by_name("btnK").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.refresh()
        cls.driver.quit()
print("test completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Anilkup/PycharmProjects/seleniumTest/reports'))








