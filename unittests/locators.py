from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    """All login page locators are here."""

    LOGIN_BUTTON = (By.ID, "Login")
    USER_NAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    ERR_MESS_BOX = (By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')

class MainPageLocators(object):
    """All main page locators are here."""

    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    REMOVE_BUTTON = (By.ID, "remove-sauce-labs-backpack")
    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    SHOPPING_CART = (By.XPATH, '//*[@id="shopping_cart_container"]')
    SHOPPING_CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    PICS = (By.CLASS_NAME, "inventory_item")

class CartLocators(object):
    CHECKOUT_BUTTON = (By.ID, "checkout")

class Check_out_informationLocators():
    """All check out infrormation page locators are here."""

    FIRST_NAME_FIELD = (By.ID, "first-name")
    LAST_NAME_FIELD = (By.ID, "last-name")
    POSTAL_CODE_FIELD = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
