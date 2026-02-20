@echo off
color 0A
echo ==========================================
echo    COMPILADOR ROBÔ - AUTOMATIZADO
echo ==========================================
echo.
echo [1/3] Limpando arquivos de compilacoes anteriores...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist *.spec del /q *.spec
echo Limpeza concluida.
echo.
echo [2/3] Gerando novo executavel blindado (Isso pode levar 2 minutos)...
pyinstaller --noconsole --onefile --add-data "robo.py;." painel.py
echo.
echo [3/3] Compilacao finalizada com sucesso! 
echo.
echo O seu arquivo "painel.exe" esta pronto dentro da pasta "dist".
echo.
pause