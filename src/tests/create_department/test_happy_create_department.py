import time
import pytest
from tests.utils import login
from locators import LOCATORS
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("driver", "base_url", "capture_dir")
def test_happy_create_department(driver, base_url, capture_dir):
    """
    Registrar un departamento con datos válidos.

    Pasos:
        1) Loguearse con usuario y contraseña válidos.
        2) Ir a /departments/create.php.
        3) Rellenar "Dept. Name" con "Departamento Test".
        4) Rellenar "Faculty Head" con "Dr. Juan Pérez".
        5) Rellenar "Email" con "test@universidad.edu".
        6) Hacer clic en "Create".
        7) Esperar redirección a /departments/home.php.
        8) Verificar que "Departamento Test" aparece en la lista.
        9) Captura de pantalla.
    """

    # 1)
    login(driver, base_url)

    # 2)
    driver.get(f"{base_url}/departments/create.php")
    time.sleep(1)
    driver.save_screenshot(f"{capture_dir}/step2_open_create_page.png")

    # 3)
    name_field = driver.find_element(By.CSS_SELECTOR, LOCATORS["dept_name_field"])
    name_field.send_keys("Departamento Test")

    # 4)
    head_field = driver.find_element(By.CSS_SELECTOR, LOCATORS["faculty_head_field"])
    head_field.send_keys("Dr. Juan Pérez")

    # 5)
    email_field = driver.find_element(By.CSS_SELECTOR, LOCATORS["email_field"])
    email_field.send_keys("test@universidad.edu")

    # 6)
    driver.save_screenshot(f"{capture_dir}/step6_after_click_create.png")
    driver.find_element(By.CSS_SELECTOR, LOCATORS["create_button"]).click()

    # 7)
    time.sleep(1)
    assert "/departments/home.php" in driver.current_url

    # 8)
    row = driver.find_element(By.XPATH, "//table//td[text()='Departamento Test']")
    assert row.is_displayed()

    # 9)
    driver.save_screenshot(f"{capture_dir}/step9_department_listed.png")
