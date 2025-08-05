import time
import pytest
from selenium.webdriver.common.by import By
from locators import LOCATORS
from tests.utils import login


@pytest.mark.usefixtures("driver", "base_url", "capture_dir")
def test_happy_edit_department(driver, base_url, capture_dir):
    """
    Editar un departamento con datos válidos.

    **Pasos**:
        1) Loguearse con usuario y contraseña válidos.
        2) Ir a /departments/home.php.
        3) Hacer clic en el botón de editar del último departamento en la lista.
        4) Poner "Dept Test Mod" en "Dept. Name".
        5) Hacer clic en "Update".
        6) Esperar redirección a /departments/home.php.
        7) Verificar que "Dept Test Mod" aparece en la lista.
        8) Captura de pantalla.
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
    name_field.send_keys("Dept Test Mod")

    # 5)
    driver.save_screenshot(f"{capture_dir}/step5_before_update.png")
    driver.find_element(By.CSS_SELECTOR, LOCATORS["update_button"]).click()
    time.sleep(1)

    # 6)
    assert "/departments/home.php" in driver.current_url

    # 7)
    row = driver.find_element(By.XPATH, "//table//td[text()='Dept Test Mod']")
    assert row.is_displayed()

    # 8)
    driver.save_screenshot(f"{capture_dir}/step8_edit_success.png")
