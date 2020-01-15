from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import time 
import unittest
from edu.models import Tutor 

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_match_for_one_user(self):
        
        #set up database 
        first_tutor = Tutor()
        first_tutor.name = 'Frankin'
        first_tutor.expert = 'Statistic'
        first_tutor.save()

        second_tutor = Tutor()
        second_tutor.name = 'Ronnie'
        second_tutor.expert = 'Signal'
        second_tutor.save()

        #Mark is a student at some university. 
        #He feel very stressed about upcomming midterm exam.
        #His friend suggest a tutor-finder online app. So he goes
        # to check out its homepage.
         
        self.browser.get(self.live_server_url)

        #He notices the page title and header mention SPARK
        self.assertIn('SPARK',self.browser.title)

        #He see a ton of Tutor list in that website 
        table = self.browser.find_element_by_id('user_list_table')
        rows = table.find_elements_by_tag_name('td')
        self.assertTrue(
            any(row.text == 'Tutor: Frankin' for row in rows),
           f"Tutor: Frankin did not appear in table. Content were: \n{table.text}"
        )
        self.assertTrue(
            any(row.text == 'Tutor: Ronnie' for row in rows),
           f"Tutor: Ronnie did not appear in table. Content were: \n{table.text}"
        )
        time.sleep(1)
        #He see textbox with "Subject".So he enter subject that he
        #want to learn straight away.
        #He types "Signal" into a text box
        inputbox = self.browser.find_element_by_id('user_select_subject')  
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter your Subject that you need help!!!'
        )
        inputbox.send_keys('Signal')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        #After that he could see a list of tutor user that agree
        #to teach with that subject that he enter.
        table = self.browser.find_element_by_id('user_list_table')
        rows = table.find_elements_by_tag_name('td')
        self.assertIn('Tutor: Ronnie', [row.text for row in rows])
        time.sleep(1)
        #He select Ronnie to be his tutor.
        #He click on a Ronnie's match button.

        button = table.find_element_by_name('Ronnie')
        button.send_keys(Keys.ENTER)
    
        #The page will show that tutor Ronnie is match for him.
        result = self.browser.find_element_by_id('match_result')
        self.assertEqual(result.text,'match!!!')
        
        self.fail('finist the test !!')


    def test_can_register_user(self):
        #Mark Parker is a student at some university. 
        #He has no members.
        #So he goes to register.
        
        self.browser.get(self.live_server_url)
        #He click on a register button.
        register_table = self.browser.find_element_by_id('user_register_and_sign_in')
        register_button = table.find_element_by_name('register')
        register_button.send_keys(Keys.ENTER)

        #He notices the page title and header mention register
        self.assertIn('Register',self.browser.title)

        #He see form for register
        form_table = self.browser.find_element_by_id('user_register_form')

        #He see textbox with "Username".So he enter username
        #He types "MarkZa55" into a text box
        username_box = self.browser.find_element_by_id('username')  
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter your Username'
        )
        inputbox.send_keys('MarkZa55')

        #He see textbox with "Password".So he enter password
        #He types "123456" into a text box
        password_box = self.browser.find_element_by_id('password')  
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter your Password'
        )
        inputbox.send_keys('123456')

        #He see textbox with "Name".So he enter name
        #He types "Mark" into a text box
        name_box = self.browser.find_element_by_id('name')  
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter your Name'
        )
        inputbox.send_keys('Mark')

        #He see textbox with "Last name".So he enter lastname
        #He types "Parker" into a text box
        lastname_box = self.browser.find_element_by_id('lastname')  
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter your Last name'
        )
        inputbox.send_keys('Parker')


        #He see textbox with "Email".So he enter email
        #He types "Spiderman@email.com" into a text box
        email_box = self.browser.find_element_by_id('email')  
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter your Email'
        )
        inputbox.send_keys('Spiderman@email.com')

        #He click on a Register button.
        button = table.find_element_by_name('sign_up')
        button.send_keys(Keys.ENTER)


        self.fail('finist the test !!')
        



       
