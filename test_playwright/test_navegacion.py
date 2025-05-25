from playwright.sync_api import sync_playwright


def test_navegacion():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless= True)
        page = browser.new_page()

        base_url = "http://127.0.0.1:8000"
        page.goto(f"{base_url}")

        page.click("text=Pacientes")

        assert "/pacientes" in page.url

        add_button = page.locator(".add-button")
        assert add_button.is_visible()


        with page.expect_navigation():
            add_button.click()

        assert "/crear_paciente" in page.url or "/agregar_paciente" in page.url
        print("✓ Navegación a 'Agregar paciente' completada con éxito")

        page.click("text=Servicios Salud")

        assert "/servicios" in page.url

        add_button = page.locator(".add-button")
        assert add_button.is_visible()

        with page.expect_navigation():
            add_button.click()

        assert "/crear_servicio" in page.url or "/agregar_servicio" in page.url
        print("✓ Navegación a 'Agregar servicio' completada con éxito")

        page.go_back()
        assert "/servicios" in page.url

        page.click(".logoNav")
        assert page.url == f"{base_url}/" or page.url == f"{base_url}"
        browser.close()
        print("✓ Prueba de navegación principal completada con éxito")

if __name__ == "__main__":
    test_navegacion()