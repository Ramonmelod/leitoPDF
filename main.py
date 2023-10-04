import pandas as pd
import PyPDF2 

# abrindo arquivo em modo leitura e lendo o binário
pdfArquivo = open(r'C:\Users\ramon\OneDrive\Documentos\GitHub\leitoPDF\RelatóriosUFSCmessetembro.pdf','rb')
#dadosPDF recebe os dados em binário do
dadosPDF = PyPDF2.PdfReader(pdfArquivo)

numeroPaginas = len(dadosPDF.pages)
print('O relatório enviado possui: ' + str(numeroPaginas) + ' páginas\n')

numeroPagina = 0
paginaLida = dadosPDF.pages[numeroPagina]

textoPagina = paginaLida.extract_text()

print(textoPagina)

pdfArquivo.close()