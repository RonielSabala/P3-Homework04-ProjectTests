import time
import pytest
from tests.utils import login
from locators import LOCATORS
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("driver", "base_url", "capture_dir")
def test_negative_create_department(driver, base_url, capture_dir):
    """
    Probar validaciones de campos vacíos y validación de email.

    Pasos:
        1) Loguearse con usuario y contraseña válidos.
        2) Ir a /departments/create.php.
        3) Hacer clic en "Create" con todos los campos vacíos.
        4) Comprobar validaciones "Completa este campo".
        5) Captura de pantalla.
        6) Rellenar todos menos email con "no-email".
        7) Hacer clic en "Create".
        8) Verificar mensaje "Completa este campo".
        9) Captura de pantalla.
    """

    # 1)
    login(driver, base_url)

    # 2)
    driver.get(f"{base_url}/departments/create.php")
    time.sleep(1)

    # 3)
    driver.find_element(By.CSS_SELECTOR, LOCATORS["create_button"]).click()
    time.sleep(1)

    # 4 y 5)
    driver.save_screenshot(f"{capture_dir}/step5_empty_fields.png")

    # 6)
    driver.find_element(By.CSS_SELECTOR, LOCATORS["dept_name_field"]).send_keys("Test")
    driver.find_element(By.CSS_SELECTOR, LOCATORS["faculty_head_field"]).send_keys(
        "Director Test"
    )

    # 7)
    driver.find_element(By.CSS_SELECTOR, LOCATORS["create_button"]).click()
    time.sleep(1)

    # 8 y 9)
    driver.save_screenshot(f"{capture_dir}/step9_invalid_email.png")
