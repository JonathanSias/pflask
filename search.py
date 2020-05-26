import PyPDF2
import re
import glob

def findText(word):
    
    # criando array para os arquivos
    pdfFiles = dict()
    # identifica arquivos pdf e joga no array
    pdfNames = glob.glob('*.pdf')

    for name in pdfNames:
        if name not in pdfFiles.keys():
            pdfFiles[name] = dict()
            pdfFiles[name]['pages'] = []


    # percorre as chaves (nome dos arquivos pdf) do dicionario pdfFiles
    for fileName in pdfFiles.keys():
        # open the pdf file
        object = PyPDF2.PdfFileReader(fileName)
        # get number of pages
        NumPages = object.getNumPages()

        for page in range(0, NumPages):
            PageObj = object.getPage(page)
            # print("this is page " + str(page))
            Text = PageObj.extractText()
            # print(Text)
            ResSearch = re.search(word, Text)
            # print(ResSearch)
            if ResSearch != None:
                pdfFiles[fileName]['pages'].append(page+1)
    
    return pdfFiles