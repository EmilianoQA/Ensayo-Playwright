# 🚀 Instructivo Básico: Playwright + Pytest para Entrevista (15 minutos)

## 📁 Paso 1: Crear carpeta del proyecto
```bash
mkdir ensayos
cd ensayos
mkdir Playwright-Pytest
cd Playwright-Pytest
```

## 🐍 Paso 2: Crear entorno virtual
```bash
# Crear entorno virtual
python -m venv venv

# Activar (Windows)
venv\Scripts\activate

# Activar (Mac/Linux)  
source venv/bin/activate
```

## 📦 Paso 3: Instalar lo necesario
```bash
pip install playwright pytest pytest-playwright
playwright install chromium
```

## 🧪 Paso 4: Crear el test básico
Crear archivo `test_demo.py`:

```python
import pytest
from playwright.sync_api import Page, expect

def test_playwright_homepage(page: Page):
    """Test básico navegando a Playwright y verificando elementos"""
    
    # Ir a la página de Playwright
    page.goto("https://playwright.dev")
    
    # Verificar que el título sea correcto
    expect(page).to_have_title("Playwright")
    
    # Verificar que el heading principal sea visible
    heading = page.locator("h1")
    expect(heading).to_be_visible()
    expect(heading).to_contain_text("Playwright")
    
    # Hacer clic en "Get started"
    page.locator("text=Get started").click()
    
    # Verificar que navegamos a la página de instalación
    expect(page).to_have_url("https://playwright.dev/docs/intro")
    expect(page.locator("h1")).to_contain_text("Installation")

def test_playwright_docs_navigation(page: Page):
    """Test navegando por la documentación"""
    
    # Ir a la página principal
    page.goto("https://playwright.dev")
    
    # Hacer clic en "Docs"
    page.locator("text=Docs").first.click()
    
    # Verificar que estamos en la documentación
    expect(page).to_have_url("https://playwright.dev/docs/intro")
    
    # Buscar enlace de "Writing tests" y hacer clic
    page.locator("text=Writing tests").click()
    
    # Verificar que llegamos a la página correcta
    expect(page.locator("h1")).to_contain_text("Writing tests")
```

## ▶️ Paso 5: Ejecutar las pruebas
```bash
# Ejecutar todos los tests
pytest test_demo.py -v

# Ejecutar con navegador visible (más lento pero visual)
pytest test_demo.py -v --headed --slowmo 1000

# Ejecutar un test específico
pytest test_demo.py::test_playwright_homepage -v

# Generar reporte HTML (instalar primero: pip install pytest-html)
pytest test_demo.py -v --html=reporte.html --self-contained-html

# Ejecutar con trace para debugging
pytest test_demo.py --tracing=on

# Ver el trace después del test
playwright show-trace test-results/*/trace.zip

# Comando completo con todo
pytest test_demo.py -v --tb=short --html=reporte.html --self-contained-html --tracing=on
```

## 💬 Qué explicar en la entrevista:

1. **"Creo el entorno virtual para aislar las dependencias"**
2. **"Instalo Playwright y pytest - Playwright para automatización web, pytest como framework de testing"**
3. **"Este test básico verifica la funcionalidad principal de navegación"**
4. **"Uso locators para encontrar elementos y expect para las verificaciones"**
5. **"Playwright maneja automáticamente las esperas, no necesito sleeps"**
6. **"--html genera un reporte visual que puedo compartir con el equipo"**
7. **"--tracing graba todo el test para poder debuggear después"**

## 🎯 Comandos clave para mostrar:
```bash
# Ver las opciones de pytest-playwright
pytest --help

# Ejecutar en diferentes navegadores
pytest test_demo.py --browser firefox
pytest test_demo.py --browser webkit

# Abrir el inspector de Playwright (para debug y crear locators)
playwright codegen https://playwright.dev

# Ver reporte HTML generado
open reporte.html        # Mac
start reporte.html       # Windows

# Ejecutar con debug (abre inspector automáticamente)
pytest test_demo.py --headed --slowmo 1000 --debug
```

## ⏱️ Timeline de 15 minutos:
- **Minutos 1-3**: Crear carpeta, venv, instalar
- **Minutos 4-10**: Mostrar y explicar el código del test
- **Minutos 11-15**: Ejecutar tests y explicar resultados

¡Listo para impresionar! 🚀