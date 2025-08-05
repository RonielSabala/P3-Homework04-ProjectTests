import time
import pytest
from selenium.webdriver.common.by import By
from locators import LOCATORS
from tests.utils import login


@pytest.mark.usefixtures("driver", "base_url", "capture_dir")
def test_happy_delete_department(driver, base_url, capture_dir):
    """
    Eliminar un departamento.

    **Pasos**:
        1) Loguearse con usuario y contraseña válidos.
        2) Ir a /departments/home.php.
        3) Hacer clic en el botón de eliminar del último departamento en la lista.
        4) Esperar redirección a /departments/delete.php?id=X.
        5) Hacer clic en "Delete".
        6) Esperar redirección a /departments/home.php.
        7) Verificar ausencia del departamento eliminado.
        8) Captura de pantalla.
    """

    # 1)
    login(driver, base_url)

    # 2)
    driver.get(f"{base_url}/departments/home.php")
    time.sleep(1)

    # 3)
    driver.save_screenshot(f"{capture_dir}/step3_before_click.png")
    delete_buttons = driver.find_elements(By.CSS_SELECTOR, LOCATORS["delete_buttons"])
    delete_buttons[-1].click()
    time.sleep(1)

    # 4)
    assert "/departments/delete.php?id=" in driver.current_url
    driver.save_screenshot(f"{capture_dir}/step4_before_delete.png")

    # 5)
    driver.find_element(By.CSS_SELECTOR, LOCATORS["delete_button"]).click()
    time.sleep(1)

    # 6)
    assert "/departments/home.php" in driver.current_url

    # 7)
    rows = driver.find_elements(By.XPATH, "//table//td[text()='Dept Test Mod']")
    assert len(rows) == 0

    # 8)
    driver.save_screenshot(f"{capture_dir}/step8_delete_success.png")
