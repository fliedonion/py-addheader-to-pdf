cd /d %~dp0
set CURDIR=%~dp0
set target=%1
set pdftitle=%~n1

set PAPER=A4L

if not exist header_template (
    echo "Please create header templates first."
    exit /b 1
)

if "%target%" == "" (
    echo "Please set pdf as command line arg (or drag and drop to this batch)."
    exit /b 2
)

call _common.bat

echo apply headers to '%target%'
py -m py-add-pdfheader %target% "%PAPER%"

echo "Please check your pdf file folder. %pdftitle%_with_header.pdf is there."

pause
