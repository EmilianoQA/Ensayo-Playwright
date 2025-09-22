# Playwright + Pytest Demo

Proyecto de demostración para automatización web con Playwright y pytest.

## 🛠️ Tecnologías
- **Python 3.11+**
- **Playwright** - Automatización web
- **Pytest** - Framework de testing
- **GitHub Actions** - CI/CD

## 🚀 Instalación
```bash
# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install pytest playwright pytest-playwright
playwright install chromium

# Ejecutar todos los tests
pytest -v

# Con navegador visible
pytest -v --headed --slowmo 1000

# Generar reporte HTML
pytest -v --html=reporte.html --self-contained-html

🤖 CI/CD
Los tests se ejecutan automáticamente con GitHub Actions en cada push y pull request.