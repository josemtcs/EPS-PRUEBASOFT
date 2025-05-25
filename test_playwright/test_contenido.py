from playwright.sync_api import sync_playwright

def test_contenido_index():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto('http://127.0.0.1:8000/')

        assert "IPS Salud y Vida" in page.content()

        assert "Bienvenido a IPS Salud y Vida, tu aliado confiable en la gestión integral de historias clínicas electrónicas." in page.content()

        browser.close()
    print(" Prueba pasada correctamente.")

if __name__ == "__main__":
    test_contenido_index()