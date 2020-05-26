# Python Flask
> Flask.

Documentação.

## Built With

* [Python]()
* [Flask]()
* [VSCode]()

## Flask

> Virtualenv version.

```sh
virtualenv --version
```

> Pip packages.

```sh
pip freeze
```

> Ativando virtual environment.

```sh
source .env2/bin/activate
```

> Rodando aplicação.

```sh
python handlers.py
```

> Desativando virtual environment.

```sh
deactivate
```

## PyPDF2

> Open and Read PDF.

```sh
import PyPDF2
pdf_file = open('filename.pdf')
read_pdf = PyPDF2.PdfFileReader('filename.pdf')
```

> Get number of pages.

```sh
page = read_pdf.getPage(0)
page_number = read_pdf.getPageNumber(page)
print page_number
```
> Extract Text.

```sh
import PyPDF2
pdf_file = open('sample.pdf')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()
page = read_pdf.getPage(0)
page_content = page.extractText()
print page_content
```
> Job Steps.

* Abrir diretório de arquivos
* Identificar arquivos .pdf
* Realizar leitura de cada arquivo
* Printar: Nome do arquivo, página da string encontrada

## Authors

* **Jonathan Sias** 
