rem Sample batch file to execute and create header template pdf.
rem NOTE: You need create venv in parent directory and install requirements first.
rem NOTE: In this version, you need change company name that hard corded 
rem       in the `src\py-add-pdfheader\create_template\__main__.py`.


cd /d %~dp0
set CURDIR=%~dp0

call _common.bat

echo Creating Templates...
py -m py-add-pdfheader.create_template

pause