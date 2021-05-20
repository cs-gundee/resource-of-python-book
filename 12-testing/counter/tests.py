import os
import pathlib
import unittest

from selenium import webdriver

# Файлын Uniform Resourse Identifier -г олох
def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

# Веб драйверт Google Chrome -г тохируулах
# driver = webdriver.Chrome()

driver = webdriver.Chrome('C:/Users/.../Downloads/chromedriver_win32/chromedriver.exe')

class WebpageTests(unittest.TestCase):
    def test_title(self):
        """Гарчиг зөв эсэхийг шалгах"""
        driver.get(file_uri("counter-v2.html"))
        self.assertEqual(driver.title, "Тоологч апп")

    def test_add(self):
        """Нэмэх товч дээр нэг удаа дарсны дараа h1 элементийн агуулга 1 болох"""
        driver.get(file_uri("counter-v2.html"))
        add = driver.find_element_by_id("add")
        add.click()
        self.assertEqual(driver.find_element_by_tag_name("h1").text, "1")

    def test_subtract(self):
        """Хасах товч дээр нэг удаа дарсны дараа h1 элементийн агуулга -1 болох"""
        driver.get(file_uri("counter-v2.html"))
        subtract = driver.find_element_by_id("subtract")
        subtract.click()
        self.assertEqual(driver.find_element_by_tag_name("h1").text, "-1")

    def test_add_and_substract(self):
        """Нэмэх, хасах товч дээр хэд хэдэн удаа дарах"""
        driver.get(file_uri("counter-v2.html"))
        add = driver.find_element_by_id("add")
        subtract = driver.find_element_by_id("subtract")
        for i in range(5):
            add.click()
            
        subtract.click()
        subtract.click()
        self.assertEqual(driver.find_element_by_tag_name("h1").text, "3")

if __name__ == "__main__":
    unittest.main()
