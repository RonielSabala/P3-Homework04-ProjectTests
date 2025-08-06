import time
import pytest
from tests.utils import login
from locators import LOCATORS
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("driver", "base_url", "capture_dir")
def test_negative_delete_department(driver, base_url, capture_dir):
    """
    Verificar error con ID ausente o inválido.

    Pasos:
        1) Loguearse con usuario y contraseña válidos.
        2) Ir a /departments/delete.php.
        3) Verificar mensaje "No se especificó el departamento.".
        4) Captura de pantalla.
        5) Ir a /departments/delete.php?id=9999
        6) Verificar mensaje "No se encontró el departamento.".
        7) Captura de pantalla.
    """

    # 1)
    login(driver, base_url)

    # 2)
    driver.get(f"{base_url}/departments/delete.php")
    time.sleep(1)

    # 3)
    error_elem = driver.find_element(By.CSS_SELECTOR, LOCATORS["error_msg"])
    assert "No se especificó el departamento." in error_elem.text

    # 4)
    driver.save_screenshot(f"{capture_dir}/step4_no_id.png")

    # 5)
    driver.get(f"{base_url}/departments/delete.php?id=9999")
    time.sleep(1)

    # 6)
    error_elem = driver.find_element(By.CSS_SELECTOR, LOCATORS["error_msg"])
    assert "No se encontró el departamento." in error_elem.text

    # 7)
    driver.save_screenshot(f"{capture_dir}/step7_invalid_id.png")
