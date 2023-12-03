from selenium.webdriver.common.keys import Keys
import errors
from locators import MainPageLocators
from locators import LoginPageLocators

class Login_Page():
    """
    Place for methods on the login page.
    """
    
    def __init__(self, username, password, driver):
        self.username = username
        self.password = password
        self.driver = driver

    def login(self):
        self.driver.find_element(*LoginPageLocators.USER_NAME_INPUT).send_keys(self.username)
        self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(self.password + Keys.RETURN)

        return self.driver.current_url
    
    def title_correct(self):
        return self.driver.title
    
    def locked_out_error_correct(self):
        err_message = self.driver.find_element(*LoginPageLocators.ERR_MESS_BOX).text
        return err_message

class Main_Page():
    """
    Place for methods on the main page.
    """

    def __init__(self, driver):
        self.driver = driver

    def one_product_to_chart(self):
        self.driver.find_element(*MainPageLocators.ADD_TO_CART_BUTTON).click()
        cart_badge = self.driver.find_element(*MainPageLocators.SHOPPING_CART_BADGE)
        return cart_badge.text
    
    def remove_one_product_from_chart(self):
        self.driver.find_element(*MainPageLocators.REMOVE_BUTTON).click()
        try: add_to_cart_button = self.driver.find_element(*MainPageLocators.ADD_TO_CART_BUTTON)
        except: raise errors.NoSuchButton
        return add_to_cart_button.text

    def pics_can_be_seen(self):
        pics_isplayed = True
        pics = self.driver.find_elements(*MainPageLocators.PICS)

        for p in pics:
            if p.is_displayed() == 0:
                pics_isplayed = False

        return pics_isplayed
    
    def cart_at_position(self):
        cart = self.driver.find_element(*MainPageLocators.SHOPPING_CART)
        cart_height= cart.value_of_css_property('height')
        cart_width= cart.value_of_css_property('width')
        cart_top= cart.value_of_css_property('top')
        cart_right= cart.value_of_css_property('right')
        return [cart_height,cart_width,cart_top,cart_right]
    
class Checkout_Page():
    """
    Place for methods on the checkout page.
    """

    def __init__(self, driver):
        self.driver = driver

class Checkout_OverView_Page():
    """
    Place for methods on the checkout page.
    """

    def __init__(self, driver):
        self.driver = driver
    