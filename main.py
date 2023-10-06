import pandas as pd
import PyPDF2 
import re
from openpyxl import load_workbook

# abrindo arquivo em modo leitura e lendo o binário
pdfArquivo = open(r'C:\Users\ramon\OneDrive\Documentos\GitHub\leitoPDF\RelatóriosUFSCmessetembro.pdf','rb')
#dadosPDF recebe os dados em binário do
dadosPDF = PyPDF2.PdfReader(pdfArquivo)

numeroPaginas = len(dadosPDF.pages)
print('O relatório enviado possui: ' + str(numeroPaginas) + ' páginas\n')

for pagina in range(0, 59): 
    numeroPagina = pagina                                   #define o numero da pagina a ser lida
    paginaLida = dadosPDF.pages[pagina]                     #armazena a pagina da itereção em paginaLida no formato
    textoPagina = paginaLida.extract_text()                 #extrai todo o texto da pagina
    padrao_data = r'\d{2}/\d{2}/\d{4}'                      #
    resultado = re.search(padrao_data, textoPagina)
    data = resultado.group(0)                               # retorna apenas a data
    print(data + "\n")


#print(textoPagina)







#print(resultado)

pdfArquivo.close()

wb = load_workbook('controleManutencao.xlsx')
wb.active

abaControle = wb['controle']

abaControle.cell(row=4, column=4,value=str(data))
wb.save('controleManutencao.xlsx')