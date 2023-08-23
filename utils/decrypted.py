from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader('path')

writer = PdfWriter()

# verificando se há senha
if reader.is_encrypted:
    reader.decrypt('senha')

# adiciona as paginas para escrita
for page in reader.pages:
    writer.add_page(page)


# salvando o novo pdf
with open('faturax.pdf', 'wb') as d:
    writer.write(d)


