import time
import pytest
from locators import LOCATORS
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("driver", "base_url", "capture_dir")
def test_boundary_credentials_login(driver, base_url, capture_dir):
    """
    Probar validaciones de longitud máxima en los campos.

    **Pasos**:
        1) Ir a /auth/login.php.
        2) Ingresar en "usuario" una cadena de 51 caracteres.
        3) Ingresar contraseña válida.
        4) Hacer clic en "Ingresar".
        5) Verificar mensaje "El nombre de usuario no puede tener más de 50 caracteres!".
        6) Captura de pantalla.
        7) Ir a /auth/login.php.
        8) Ingresar usuario válido.
        9) Ingresar contraseña de 51 caracteres.
        10) Hacer clic en "Ingresar".
        11) Verificar mensaje "La contraseña no puede tener más de 50 caracteres!".
        12) Captura de pantalla.
    """

    # 1)
    driver.get(f"{base_url}/auth/login.php")
    time.sleep(1)

    # 2)
    long_user = "u" * 51
    user_field = driver.find_element(By.CSS_SELECTOR, LOCATORS["login_user_field"])
    user_field.clear()
    user_field.send_keys(long_user)

    # 3)
    pass_field = driver.find_element(By.CSS_SELECTOR, LOCATORS["login_pass_field"])
    pass_field.clear()
    pass_field.send_keys("tarea4")

    # 4)
    driver.find_element(By.CSS_SELECTOR, LOCATORS["login_button"]).click()
    time.sleep(1)

    # 5)
    error_elem = driver.find_element(By.CSS_SELECTOR, LOCATORS["error_msg"])
    assert (
        "El nombre de usuario no puede tener más de 50 caracteres!" in error_elem.text
    )

    # 6)
    driver.save_screenshot(f"{capture_dir}/step6_username_too_long.png")

    # 7)
    driver.get(f"{base_url}/auth/login.php")
    time.sleep(1)

    # 8)
    user_field = driver.find_element(By.CSS_SELECTOR, LOCATORS["login_user_field"])
    user_field.clear()
    user_field.send_keys("student")

    # 9)
    long_pass = "p" * 51
    pass_field = driver.find_element(By.CSS_SELECTOR, LOCATORS["login_pass_field"])
    pass_field.clear()
    pass_field.send_keys(long_pass)

    # 10)
    driver.find_element(By.CSS_SELECTOR, LOCATORS["login_button"]).click()
    time.sleep(1)

    # 11)
    error_elem = driver.find_element(By.CSS_SELECTOR, LOCATORS["error_msg"])
    assert "La contraseña no puede tener más de 50 caracteres!" in error_elem.text

    # 12)
    driver.save_screenshot(f"{capture_dir}/step12_password_too_long.png")
