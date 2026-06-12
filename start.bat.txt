@echo off
REM --------------------------------------------
REM Este archivo inicia tu servidor local en Windows
REM --------------------------------------------

REM Cambia al directorio donde está tu proyecto
cd C:\Users\Josee\OneDrive\Documentos\Proyectos\AppWeb\ServidorAppWeb

REM Ejecuta el comando para levantar el servidor .NET
dotnet run

REM Abre automáticamente el navegador en la URL del servidor
start http://localhost:5000/main.html

REM Mantiene la ventana abierta al final para ver mensajes o errores
pause
