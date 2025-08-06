import time
from locators import LOCATORS
from selenium.webdriver.common.by import By


def login(driver, base_url):
    """
    Función que reutiliza el código para hacer login.

    Pasos:
        1) Ir a /auth/login.php.
        2) Ingresar usuario y contraseña.
        3) Hacer clic en Ingresar y esperar home.
    """

    driver.get(f"{base_url}/auth/login.php")
    time.sleep(1)

    user_field = driver.find_element(By.CSS_SELECTOR, LOCATORS["login_user_field"])
    pass_field = driver.find_element(By.CSS_SELECTOR, LOCATORS["login_pass_field"])
    user_field.send_keys("student")
    pass_field.send_keys("tarea4")

    driver.find_element(By.CSS_SELECTOR, LOCATORS["login_button"]).click()
    time.sleep(1)
