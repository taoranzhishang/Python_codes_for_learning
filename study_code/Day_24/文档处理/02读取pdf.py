import PyPDF2

pdffile = open(r"C:\Users\Tsinghua-yincheng\Desktop\day24down\谢宇进.pdf", "rb")
pdfreader = PyPDF2.PdfFileReader(pdffile)  # 读取pdf文件
print(pdfreader.numPages)  # 显示8页
for i in range(pdfreader.numPages):
    page = pdfreader.getPage(i)  # 抓取第i页
    print(page.extractText())
