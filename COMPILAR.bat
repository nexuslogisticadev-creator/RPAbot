@echo off
REM COMPILAR.bat - Limpa build/dist e compila painel.py com PyInstaller

echo Limpando pastas antigas (build, dist, *.spec)...
rmdir /s /q build 2>nul
rmdir /s /q dist 2>nul
del /q painel.spec 2>nul

REM Se houver virtualenv local em env\Scripts, ativa automaticamente
if exist env\Scripts\activate.bat (
    echo Ativando virtualenv em env\n
    call env\Scripts\activate.bat
)

echo Rodando PyInstaller... (isso pode levar alguns minutos)
pyinstaller --noconsole --onefile --add-data "robo.py;." painel.py

if %ERRORLEVEL% neq 0 (
    echo Erro: o PyInstaller retornou codigo %ERRORLEVEL%.
    echo Verifique a saida acima para detalhes.
    pause
    exit /b %ERRORLEVEL%
)

echo Build concluido. Arquivo gerado em dist\painel.exe
pause
