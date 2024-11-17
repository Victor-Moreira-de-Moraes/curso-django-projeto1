@echo off
SET DATE=%DATE:/=-%
SET BACKUP_DIR=C:\Users\MoraeVic\Documents\estudo\curso-django-projeto1\backup_folder
SET MYSQL_USER=root
SET MYSQL_PASSWORD=#Fbrql823
SET MYSQL_DB=recipes_db

REM Criacao do backup com mysqldump
"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysqldump.exe" -u %MYSQL_USER% -p%MYSQL_PASSWORD% %MYSQL_DB% > "%BACKUP_DIR%\%MYSQL_DB%-%DATE%.sql"

REM Excluindo backups mais antigos que 7 dias
forfiles /p "%BACKUP_DIR%" /s /m *.sql /D -7 /C "cmd /c del @path"
