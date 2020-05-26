import PyPDF2
import re
import glob

# criando array para os arquivos
pdfFiles = []
# identifica arquivos pdf e joga no array
pdfFiles = glob.glob('*.pdf')
# pega o numero de arquivos contidos no array
numOfFiles = len(pdfFiles)
# 
# print(numOfFiles)

def findText(word):
    # open the pdf file
    # object = PyPDF2.PdfFileReader("redes.pdf")
    # get number of pages
    # NumPages = object.getNumPages()
    # 
    print(numOfFiles)
    for i in numOfFiles:
        # object = PyPDF2.PdfFileReader(pdfFiles[i])
        # NumPages = object.getNumPages()
    # matchs = []
        matchs = []
        # for j in range(0, NumPages):
        #     PageObj = object.getPage(j)
        #     print("this is page " + str(j))
        #     Text = PageObj.extractText()
        #     # print(Text)
        #     ResSearch = re.search(word, Text)
        #     print(ResSearch)
        #     if ResSearch != None:
        #         matchs.append(j+1)
            
            # fileName = pdfFiles[i]
            # data = dict()
            # if "redes" not in data.keys():
            #     data['redes'] = dict()
            #     data['redes']['pages'] = []
            # print(data)
            
            # return 
    
    return matchs