import time
import pytest
from locators import LOCATORS
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("driver", "base_url", "capture_dir")
def test_happy_login(driver, base_url, capture_dir):
    """
    Verificar que un usuario con credenciales válidas pueda loguearse
    con éxito.

    **Pasos**:
        1) Ir a /auth/login.php.
        2) Localizar campo "usuario" y escribir usuario válido de prueba.
        3) Localizar campo "contraseña" y escribir la contraseña válida.
        4) Hacer clic en "Ingresar".
        5) Esperar a que la URL cambie a /home.php.
        6) Verificar que exista un elemento "Logout" en la página.
        7) Captura de pantalla.
    """

    # 1)
    driver.get(f"{base_url}/auth/login.php")
    time.sleep(1)
    driver.save_screenshot(f"{capture_dir}/step1_open_login.png")

    # 2)
    user_field = driver.find_element(By.CSS_SELECTOR, LOCATORS["login_user_field"])
    user_field.clear()
    user_field.send_keys("student")

    # 3)
    pass_field = driver.find_element(By.CSS_SELECTOR, LOCATORS["login_pass_field"])
    pass_field.clear()
    pass_field.send_keys("tarea4")

    # 4)
    driver.save_screenshot(f"{capture_dir}/step4_click_login.png")
    login_button = driver.find_element(By.CSS_SELECTOR, LOCATORS["login_button"])
    login_button.click()

    # 5)
    pytest.raises(AssertionError)
    assert "/home.php" in driver.current_url

    # 6)
    logout_elem = driver.find_element(By.CSS_SELECTOR, LOCATORS["logout_button"])
    assert logout_elem.is_displayed()

    # 7)
    driver.save_screenshot(f"{capture_dir}/step7_successful_login.png")
