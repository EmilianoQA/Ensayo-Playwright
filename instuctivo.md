# Navega a un directorio donde quieras crear el proyecto (ajusta la ruta si es necesario)
cd ~/Documents/Testing/Ensayos/

# Crea la carpeta del proyecto y entra en ella
mkdir Playwright-Pytest
cd Playwright-Pytest

# Crea y activa el entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instala las librerías
pip install pytest pytest-playwright

# Instala los navegadores de Playwright
playwright install

# Crea el archivo del test y escribe el código
cat > test_login.py <<EOF
import pytest
from playwright.sync_api import Page, expect

def test_successful_login(page: Page):
    # Navega a la URL de login
    page.goto("https://the-internet.herokuapp.com/login")
    # Rellena el campo de usuario
    page.fill("#username", "tomsmith")
    # Rellena el campo de contraseña
    page.fill("#password", "SuperSecretPassword!")
    # Hace clic en el botón de login
    page.click("button[type='submit']")
    # Verifica que el login fue exitoso
    expect(page.locator("#flash.success")).to_be_visible()
    expect(page.locator("#flash")).to_contain_text("You logged into a secure area!")
    expect(page.get_by_role("link", name="Logout")).to_be_visible()
EOF

# Ejecuta la prueba para ver el navegador
pytest --headed

Tienes razón, mi error. El último instructivo no estaba completo.

Aquí está el documento final, consolidado con todos los pasos que hemos discutido.

Playwright + Pytest: Guía Completa
1. Configuración del Entorno
Paso 1: Crear la carpeta del proyecto
Crea un directorio para tu proyecto y navega hacia él.

Bash

mkdir mi-proyecto-playwright
cd mi-proyecto-playwright
Paso 2: Crear y activar un entorno virtual
Crea un entorno aislado para las dependencias y actívalo.

Bash

python3 -m venv venv
source venv/bin/activate
Paso 3: Instalar las librerías necesarias
Instala pytest (el framework de testing) y pytest-playwright (la integración con Playwright).

Bash

pip install pytest pytest-playwright
Paso 4: Instalar los navegadores de Playwright
Descarga los navegadores (Chromium, Firefox, WebKit) que Playwright necesita.

Bash

playwright install
2. Creación del Test
Paso 5: Crear el archivo de prueba
Crea un archivo llamado test_login.py para escribir tu test.

Bash

touch test_login.py
Paso 6: Escribir el código del test
Copia y pega este código en el archivo test_login.py.

Python

import pytest
from playwright.sync_api import Page, expect

def test_successful_login(page: Page):
    """
    Test de login exitoso.
    """
    # Navega a la URL de login
    page.goto("https://the-internet.herokuapp.com/login")
    # Rellena el campo de usuario
    page.fill("#username", "tomsmith")
    # Rellena el campo de contraseña
    page.fill("#password", "SuperSecretPassword!")
    # Hace clic en el botón de login
    page.click("button[type='submit']")
    # Verifica que el login fue exitoso comprobando la visibilidad de un elemento
    expect(page.locator("#flash.success")).to_be_visible()
    # Verifica que el mensaje de éxito es el correcto
    expect(page.locator("#flash")).to_contain_text("You logged into a secure area!")
    # Verifica que el botón de "Logout" esté visible
    expect(page.get_by_role("link", name="Logout")).to_be_visible()
3. Ejecución del Test y Depuración
Paso 7: Ejecutar la prueba
Corre el test usando pytest. El flag --headed hace que el navegador se abra y puedas ver la ejecución.

Bash

pytest --headed
Paso 8: Abrir el Inspector de Playwright

Opción 1: Para generar código y depurar un sitio
Usa el inspector para generar selectores y código de manera interactiva.
playwright codegen <URL_DE_LA_PAGINA>

Ejemplo: playwright codegen https://the-internet.herokuapp.com/login

Opción 2: Para depurar una prueba existente paso a paso
Ejecuta tu prueba con la variable PWDEBUG para que se detenga y puedas inspeccionar cada paso.
PWDEBUG=1 pytest