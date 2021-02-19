from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open
import codecs


# pip install  PDFMiner3K
def readPDF(pdfFile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)

    process_pdf(rsrcmgr, device, pdfFile)
    device.close()

    content = retstr.getvalue()
    retstr.close()
    return content


pdfFile = urlopen("http://pythonscraping.com/pages/warandpeace/chapter1.pdf")
# pdfFile=codecs.open("C:\\Users\\Tsinghua-yincheng\\Desktop\\day24down\\谢宇进.pdf","rb","gbk","ignore")
outputString = readPDF(pdfFile)
print(outputString)
pdfFile.close()
