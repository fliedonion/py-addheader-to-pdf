IF "%CURDIR%" == "" (
    echo "ERROR: batch : CURDIR is not defined."
)
else (
    set PYTHONPATH=%CURDIR%\..\src\

    if not exist header_template (
        mkdir header_template
    )

    call "%CURDIR%\..\venv\scripts\activate"
)
