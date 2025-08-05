import time
from selenium.webdriver.common.by import By
from locators import LOCATORS


def login(driver, base_url):
    """
    Función para rehusar el código de loguearse.

    Pasos:
        1) Ir a /auth/login.php.
        2) Ingresar usuario y contraseña.
        3) Clic en Ingresar y esperar home.
    """

    driver.get(f"{base_url}/auth/login.php")
    time.sleep(1)

    user_field = driver.find_element(By.CSS_SELECTOR, LOCATORS["login_user_field"])
    pass_field = driver.find_element(By.CSS_SELECTOR, LOCATORS["login_pass_field"])
    user_field.send_keys("student")
    pass_field.send_keys("tarea4")

    driver.find_element(By.CSS_SELECTOR, LOCATORS["login_button"]).click()
    time.sleep(1)
