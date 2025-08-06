import time
import pytest
from tests.utils import login
from locators import LOCATORS
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("driver", "base_url", "capture_dir")
def test_boundary_create_department(driver, base_url, capture_dir):
    """
    Probar longitud máxima en cada campo.

    Pasos:
        1) Loguearse con usuario y contraseña válidos.
        2) Ir a /departments/create.php.
        3) Poner 51 caracteres en “Dept. Name”.
        4) Poner datos válidos en los demás campos.
        5) Hacer clic en “Create”.
        6) Verificar mensaje “El nombre del departamento no puede tener más de 50 caracteres!”.
        7) Captura de pantalla.
        8) Repetir para “Faculty Head” y “Email”.
    """

    # 1)
    login(driver, base_url)

    # 2)
    driver.get(f"{base_url}/departments/create.php")
    time.sleep(1)

    # 3)
    long_name = "N" * 51
    driver.find_element(By.CSS_SELECTOR, LOCATORS["dept_name_field"]).send_keys(
        long_name
    )
    driver.find_element(By.CSS_SELECTOR, LOCATORS["faculty_head_field"]).send_keys(
        "Dr. Test"
    )
    driver.find_element(By.CSS_SELECTOR, LOCATORS["email_field"]).send_keys(
        "test@universidad.edu"
    )

    # 4 y 5)
    driver.find_element(By.CSS_SELECTOR, LOCATORS["create_button"]).click()
    time.sleep(1)

    # 6)
    error_name = driver.find_element(By.CSS_SELECTOR, LOCATORS["error_msg"])
    assert (
        "El nombre del departamento no puede tener más de 50 caracteres!"
        in error_name.text
    )

    # 7)
    driver.save_screenshot(f"{capture_dir}/step7_name_too_long.png")

    # 8) Faculty Head
    driver.get(f"{base_url}/departments/create.php")
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, LOCATORS["dept_name_field"]).send_keys(
        "Departamento Test"
    )
    long_head = "H" * 51
    driver.find_element(By.CSS_SELECTOR, LOCATORS["faculty_head_field"]).send_keys(
        long_head
    )
    driver.find_element(By.CSS_SELECTOR, LOCATORS["email_field"]).send_keys(
        "test@universidad.edu"
    )
    driver.find_element(By.CSS_SELECTOR, LOCATORS["create_button"]).click()
    time.sleep(1)
    error_head = driver.find_element(By.CSS_SELECTOR, LOCATORS["error_msg"])
    assert (
        "El nombre del jefe de facultad no puede tener más de 50 caracteres!"
        in error_head.text
    )
    driver.save_screenshot(f"{capture_dir}/step8_head_too_long.png")

    # 8) Email
    driver.get(f"{base_url}/departments/create.php")
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, LOCATORS["dept_name_field"]).send_keys(
        "Departamento Test"
    )
    driver.find_element(By.CSS_SELECTOR, LOCATORS["faculty_head_field"]).send_keys(
        "Dr. Test"
    )

    long_email = ("e" * 51) + "@gmail.com"
    driver.find_element(By.CSS_SELECTOR, LOCATORS["email_field"]).send_keys(long_email)
    driver.find_element(By.CSS_SELECTOR, LOCATORS["create_button"]).click()
    time.sleep(1)
    error_email = driver.find_element(By.CSS_SELECTOR, LOCATORS["error_msg"])
    assert "El email no puede tener más de 50 caracteres!" in error_email.text
    driver.save_screenshot(f"{capture_dir}/step8_email_too_long.png")
