import time
import pytest
from locators import LOCATORS
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("driver", "base_url", "capture_dir")
def test_negative_login(driver, base_url, capture_dir):
    """
    Intentar acceso con credenciales inválidas.

    **Pasos**:
        1) Ir a /auth/login.php.
        2) Introducir usuario inexistente y contraseña cualquiera.
        3) Hacer clic en "Ingresar".
        4) Verificar mensaje "El usuario proporcionado no existe!".
        5) Captura de pantalla.
        6) Ir a /auth/login.php.
        7) Introducir usuario válido y contraseña incorrecta.
        8) Hacer clic en "Ingresar".
        9) Verificar mensaje "Contraseña incorrecta!".
        10) Captura de pantalla.
    """

    # 1)
    driver.get(f"{base_url}/auth/login.php")
    time.sleep(1)

    # 2)
    user_field = driver.find_element(By.CSS_SELECTOR, LOCATORS["login_user_field"])
    pass_field = driver.find_element(By.CSS_SELECTOR, LOCATORS["login_pass_field"])
    user_field.send_keys("usuario_inexistente")
    pass_field.send_keys("clave_aleatoria")

    # 3)
    login_button = driver.find_element(By.CSS_SELECTOR, LOCATORS["login_button"])
    login_button.click()
    time.sleep(1)

    # 4)
    error_elem = driver.find_element(By.CSS_SELECTOR, LOCATORS.get("error_msg"))
    assert "El usuario proporcionado no existe!" in error_elem.text

    # 5)
    driver.save_screenshot(f"{capture_dir}/step5_user_not_found.png")

    # 6)
    driver.get(f"{base_url}/auth/login.php")
    time.sleep(1)

    # 7)
    user_field = driver.find_element(By.CSS_SELECTOR, LOCATORS["login_user_field"])
    pass_field = driver.find_element(By.CSS_SELECTOR, LOCATORS["login_pass_field"])
    user_field.send_keys("student")
    pass_field.send_keys("clave_incorrecta")

    # 8)
    login_button = driver.find_element(By.CSS_SELECTOR, LOCATORS["login_button"])
    login_button.click()
    time.sleep(1)

    # 9)
    error_elem = driver.find_element(By.CSS_SELECTOR, LOCATORS.get("error_msg"))
    assert "Contraseña incorrecta!" in error_elem.text

    # 10)
    driver.save_screenshot(f"{capture_dir}/step10_wrong_password.png")
