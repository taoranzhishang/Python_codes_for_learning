import PyPDF2  # pypdf库不完善

pdffile = open(r"D:\Resources\1.Linux基础lab-基础命令行操作.pdf", "rb")
pdfreader = PyPDF2.PdfFileReader(pdffile)  # 读取pdf文件
print(pdfreader.numPages)  # 显示8页
for i in range(pdfreader.numPages):
    page = pdfreader.getPage(i)  # 抓取第i页
    print(page.extractText())
