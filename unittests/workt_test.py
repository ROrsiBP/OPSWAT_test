import unittest
import common_logic
import errors

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)

class TestFundamental(unittest.TestCase):  
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.get("https://www.saucedemo.com")
        self.Login_page_logic = common_logic.Login_Page("standard_user", "secret_sauce", self.driver)

    def test_title_is_correct(self):
        self.assertEqual(self.Login_page_logic.title_correct(), "Swag Labs")
        
class TestBasicMethods(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.get("https://www.saucedemo.com")
        self.Login_page_logic = common_logic.Login_Page("standard_user", "secret_sauce", self.driver)
        self.Main_page_logic = common_logic.Main_Page(self.driver)
        self.Cart_page_logic = common_logic.Cart_Page(self.driver)
        self.Checkout_data_page_logic = common_logic.Checkout_Data_Page(self.driver)

    def test_login(self):
        is_success = self.Login_page_logic.login()
        self.assertEqual(is_success,"https://www.saucedemo.com/inventory.html")

    def test_one_product_to_chart_badge_appeared(self):
        self.Login_page_logic.login()
        added_amount = self.Main_page_logic.one_product_to_chart()
        self.assertEqual(added_amount,'1')
    
    def test_remove_one_product_from_chart(self):
        self.Login_page_logic.login()
        self.Main_page_logic.one_product_to_chart()
        add_to_cart_button_text = self.Main_page_logic.remove_one_product_from_chart()
        self.assertEqual(add_to_cart_button_text,"Add to cart")

    def test_can_to_to_cart(self):
        self.Login_page_logic.login()
        self.Cart_page_logic.go_to_cart()
        self.assertTrue(self.driver.current_url == "https://www.saucedemo.com/cart.html")

    def test_can_write_in_first_name_checkout(self):
        self.Login_page_logic.login()
        self.Cart_page_logic.go_to_cart()
        self.Checkout_data_page_logic.go_to_checkout_data()
        name = self.Checkout_data_page_logic.user_first_name_write_in("Ruzsin")
        self.assertTrue(name == "Ruzsin")

class TestVisuals(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.get("https://www.saucedemo.com")
        self.Login_page_logic = common_logic.Login_Page("standard_user", "secret_sauce", self.driver)
        self.Main_page_logic = common_logic.Main_Page(self.driver)

    def test_images_visible(self):
        self.Login_page_logic.login()
        is_visible = self.Main_page_logic.pics_can_be_seen()
        self.assertTrue(is_visible)

    def test_cart_is_at_place(self):
        cart_expected_pos = ['40px','40px','10px','20px']
        self.Login_page_logic.login()
        cart_pos = self.Main_page_logic.cart_at_position()

        self.assertEqual(cart_expected_pos,cart_pos)

class TestUsers(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.get("https://www.saucedemo.com")
        self.Main_page_logic = common_logic.Main_Page(self.driver)
    
    def test_locked_out_user_can_not_log_in(self):
        Login_page_logic = common_logic.Login_Page("locked_out_user", "secret_sauce", self.driver)
        Login_page_logic.login()
        err_message = Login_page_logic.locked_out_error_correct()
        self.assertEqual(err_message, "Epic sadface: Sorry, this user has been locked out.")

    def test_problem_user_can_not_remove_item_on_main_page(self):
        Login_page_logic = common_logic.Login_Page("problem_user", "secret_sauce", self.driver)
        Login_page_logic.login()
        self.Main_page_logic.one_product_to_chart()
        with self.assertRaises(errors.NoSuchButton):
            self.Main_page_logic.remove_one_product_from_chart()
    
    def test_visual_user_cart_not_at_correct_place(self):
        Login_page_logic = common_logic.Login_Page("visual_user", "secret_sauce", self.driver)
        cart_expected_pos = ['40px','40px','10px','20px']
        Login_page_logic.login()
        cart_pos = self.Main_page_logic.cart_at_position()

        self.assertNotEqual(cart_expected_pos,cart_pos)

    

        