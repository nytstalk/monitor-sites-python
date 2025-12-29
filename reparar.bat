@echo off
echo ==========================================
echo   REPARANDO INSTALACAO (NOVO PYTHON)
echo ==========================================
echo.

echo 1. Verificando versao do Python (Deve ser 3.10, 3.11 ou 3.12)...
python --version
echo.

echo 2. Instalando as bibliotecas que faltam...
python -m pip install undetected-chromedriver selenium
echo.

echo ==========================================
echo   TUDO PRONTO! INICIANDO MONITOR...
echo ==========================================
echo.
python main.py

pause