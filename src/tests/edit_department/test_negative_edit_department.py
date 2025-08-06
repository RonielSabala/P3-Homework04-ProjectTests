import time
import pytest
from tests.utils import login
from locators import LOCATORS
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("driver", "base_url", "capture_dir")
def test_negative_edit_department(driver, base_url, capture_dir):
    """
    Editar el nombre de departamento con un nombre de otro ya existente.

    Pasos:
        1) Loguearse con usuario y contraseña válidos.
        2) Ir a /departments/home.php.
        3) Hacer clic en el botón de editar del último departamento en la lista.
        4) Poner "Dept Test Mod" en "Dept. Name".
        5) Hacer clic en "Update".
        6) Verificar mensaje "Ya existe un departamento con ese nombre!".
        7) Captura de pantalla.
    """

    # 1)
    login(driver, base_url)

    # 2)
    driver.get(f"{base_url}/departments/home.php")
    time.sleep(1)

    # 3)
    driver.save_screenshot(f"{capture_dir}/step3_before_click.png")
    edit_buttons = driver.find_elements(By.CSS_SELECTOR, LOCATORS["edit_buttons"])
    edit_buttons[-1].click()
    time.sleep(1)

    # 4)
    name_field = driver.find_element(By.CSS_SELECTOR, LOCATORS["dept_name_field"])
    name_field.clear()
    name_field.send_keys("Computer Science")

    # 5)
    driver.find_element(By.CSS_SELECTOR, LOCATORS["update_button"]).click()
    time.sleep(1)

    # 6)
    error_elem = driver.find_element(By.CSS_SELECTOR, LOCATORS["error_msg"])
    assert "Ya existe un departamento con ese nombre!" in error_elem.text

    # 7)
    driver.save_screenshot(f"{capture_dir}/step7_name_conflict.png")
