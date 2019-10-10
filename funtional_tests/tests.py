from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import WebDriverException
MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()


    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self,row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError,WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)


    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://127.0.0.1:8000/home/')

        self.assertIn('To-Do',self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)

        #应用邀请她输入一个待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        #她在文本框输入了'Buy peacock feathers'
        #伊迪斯的爱好是使用假蝇做鱼饵钓鱼
        inputbox.send_keys('Buy peacock feathers')

        #他按回车键后，页面更新了
        #待办事项表格中显示了"1:Buy peacock feathers"
        inputbox.send_keys(Keys.ENTER)
        time.sleep(10)
        self.wait_for_row_in_list_table('1:Buy peacock feathers')


        #页面中又显示了一个文本框，可以输入其他待办事项
        #他输入了“Use peacock feathers to make a fly”
        #伊迪斯做事很有条理
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        time.sleep(10)

        #页面再次更新，她的清单中显示了这两个待办事项
        self.wait_for_row_in_list_table('1:Buy peacock feathers')
        self.wait_for_row_in_list_table('2:Use peacock feathers to make a fly')

        self.fail('Finish the test!')
