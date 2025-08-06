import time
import pytest
from tests.utils import login
from locators import LOCATORS
from selenium.webdriver.common.by import By


def get_elements(driver):
    dept_name_filed = driver.find_element(By.CSS_SELECTOR, LOCATORS["dept_name_field"])
    faculty_head_field = driver.find_element(
        By.CSS_SELECTOR, LOCATORS["faculty_head_field"]
    )

    email_field = driver.find_element(By.CSS_SELECTOR, LOCATORS["email_field"])
    update_button = driver.find_element(By.CSS_SELECTOR, LOCATORS["update_button"])

    return dept_name_filed, faculty_head_field, email_field, update_button


def get_error_text(driver):
    return driver.find_element(By.CSS_SELECTOR, LOCATORS["error_msg"]).text


@pytest.mark.usefixtures("driver", "base_url", "capture_dir")
def test_boundary_edit_department(driver, base_url, capture_dir):
    """
    Probar longitud máxima en cada campo.

    Pasos:
        1) Loguearse con usuario y contraseña válidos.
        2) Ir a /departments/home.php.
        3) Hacer clic en el botón de editar del último departamento en la lista.
        4) Poner 51 caracteres en "Dept. Name".
        5) Poner datos válidos en los demás campos.
        6) Hacer clic en "Update".
        7) Verificar mensaje "El nombre del departamento no puede tener más de 50 caracteres!" y que el input conserve el valor de 51 caracteres.
        8) Captura de pantalla.
        9) Repetir para "Faculty Head" y "Email".
    """

    # 1)
    login(driver, base_url)

    # 2)
    driver.get(f"{base_url}/departments/home.php")
    time.sleep(1)

    # 3)
    edit_buttons = driver.find_elements(By.CSS_SELECTOR, LOCATORS["edit_buttons"])
    edit_buttons[-1].click()
    time.sleep(1)

    # 4)
    dept_name_filed, faculty_head_field, email_field, update_button = get_elements(
        driver
    )

    dept_name_filed.clear()
    dept_name_filed.send_keys("N" * 51)

    # 5)
    update_button.click()
    time.sleep(1)

    # 6)
    assert (
        "El nombre del departamento no puede tener más de 50 caracteres!"
        in get_error_text(driver)
    )

    # 7)
    driver.save_screenshot(f"{capture_dir}/step7_name_too_long_retained.png")

    # 8) Faculty Head

    dept_name_filed, faculty_head_field, _, update_button = get_elements(driver)

    dept_name_filed.clear()
    faculty_head_field.clear()

    dept_name_filed.send_keys("Departamento Test")
    faculty_head_field.send_keys("H" * 51)

    update_button.click()
    time.sleep(1)
    assert (
        "El nombre del jefe de facultad no puede tener más de 50 caracteres!"
        in get_error_text(driver)
    )

    driver.save_screenshot(f"{capture_dir}/step8_head_too_long_retained.png")

    # 9) Email

    _, faculty_head_field, email_field, update_button = get_elements(driver)

    faculty_head_field.clear()
    email_field.clear()

    faculty_head_field.send_keys("Dr. Test")
    email_field.send_keys(("e" * 41) + "@gmail.com")

    update_button.click()
    time.sleep(1)
    assert "El email no puede tener más de 50 caracteres!" in get_error_text(driver)
    driver.save_screenshot(f"{capture_dir}/step9_email_too_long_retained.png")
