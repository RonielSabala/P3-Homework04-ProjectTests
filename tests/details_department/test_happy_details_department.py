import time
import pytest
from selenium.webdriver.common.by import By
from locators import LOCATORS
from tests.utils import login


@pytest.mark.usefixtures("driver", "base_url", "capture_dir")
def test_happy_details_department(driver, base_url, capture_dir):
    """
    Mostrar datos correctos de un departamento existente.

    **Pasos**:
        1) Loguearse con usuario y contraseña válidos.
        2) Ir a /departments/home.php.
        3) Hacer clic en el botón de detalles del último departamento en la lista.
        4) Esperar redirección a /departments/details.php?id=X.
        5) Captura de pantalla.
    """

    # 1)
    login(driver, base_url)

    # 2)
    driver.get(f"{base_url}/departments/home.php")
    time.sleep(1)

    # 3)
    driver.save_screenshot(f"{capture_dir}/step3_before_click.png")
    buttons = driver.find_elements(By.CSS_SELECTOR, LOCATORS["details_buttons"])
    buttons[-1].click()
    time.sleep(1)

    # 4)
    assert "/departments/details.php?id=" in driver.current_url

    # 5)
    driver.save_screenshot(f"{capture_dir}/step5_view_details.png")
