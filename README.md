# Append watermark / header to PDF 

Currently supported sizes are A4L, A4, A3L, A3.


## Requirements

python 3.9 required.
only test on Windows environment.
MS Gothic font required.

To change header text, you need change code.



## Try to use sample batch.


### Windows

#### Copy codes to your computer.

Clone or download and extract this repo.


#### Create venv 

Open command prompt and move to 
top directory of this repo (on your computer you cloned or extracted previous step).

run thease command.
```
py -3 -m venv venv 
venv\scripts\activate
```

If it's seem to be error, check your environment and retry from first.

#### Install required python packages.

install packages to `(venv)`.

```
pip install -r requirements.txt
```

You can close command prompt.


#### create header template.

In the `sample_batchfiles` folder, run `create_template.bat` from command prompt or double click.

You'll find some pdf files in `sample_batchfiles\header_template`.

note: If the `venv` directory exists in the correct location from batch file, the virtual environment will be activated automatically.

#### apply header to your pdf

Drag and drop pdf you want add header to `header_append_XX.bat`.

Use the batch file with the same name as the paper size.

You can find new pdf file in your pdf folder.
If your pdf filename is 'abc.pdf', the pdf filename, that is applied header, will be 'abc_with_header'. 

note: If the `venv` directory exists in the correct location from batch file, the virtual environment will be activated automatically.



## dev note

* command sample to create header templates.
```
py -m py-add-pdfheader.create_template
```

* command sample to apply header.
```
py -m py-add-pdfheader target.pdf A4
```

second arg is one of template paper size ("A3", "A3L", "A4", "A4L").
