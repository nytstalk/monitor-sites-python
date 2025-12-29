@echo off
cd /d "%~dp0"

echo ==========================================
echo   CORRIGINDO INSTALACOES (Isso pode demorar um pouco)
echo ==========================================
echo.

echo [1/2] Instalando Cloudscraper no Python atual...
python -m pip install cloudscraper

echo [2/2] Instalando BeautifulSoup no Python atual...
python -m pip install beautifulsoup4

echo.
echo ==========================================
echo   INICIANDO O MONITOR
echo ==========================================
echo.

python main.py

echo.
echo O programa fechou. Se houve erro, leia acima.
pause