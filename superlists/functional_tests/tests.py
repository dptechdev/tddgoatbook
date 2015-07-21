from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(LiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()
	
	#helper method
	def check_for_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])

	@unittest.skip
	def test_can_start_a_list_and_retrieve_it_later(self):
		#Edit has heard about a cool new online to-do app. She goes
		#to check out its homepage
		self.browser.get('http://localhost:8000')
		
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		inputbox = self.browser.find_element_by_id('id_new_item')
		
		inputbox.send_keys('1: Buy peacock feathers')
		inputbox.send_keys(Keys.ENTER)
		
		self.check_for_row_in_list_table('1: Buy peacock feathers')
		self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')	
	
		self.fail('Finish the test!')
	
	@unittest.skip
	def test_can_start_a_list_and_retrieve_it_later(self):
		self.browser.get(self.live_server_url)
if __name__ == '__main__':
	unittest.main()




