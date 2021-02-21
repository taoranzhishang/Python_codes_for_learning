# pip  install   PDFMiner3K

import urllib.request  # 打开网页
import pdfminer.pdfinterp  # 管理PDF资源
import pdfminer.converter  # 文本转换
import pdfminer.layout  # 处理pdf布局
import io  # 输入输出


def readpdf(pdffile):
    rsmgr = pdfminer.pdfinterp.PDFResourceManager()  # 资源管理器
    retstr = io.StringIO()  # 文本输出
    lap = pdfminer.layout.LAParams()  # 处理布局
    device = pdfminer.converter.TextConverter(rsmgr, retstr, laparams=lap)  # 文本提取工具
    pdfminer.pdfinterp.process_pdf(rsmgr, device, pdffile)  # 根据文件进行解析
    device.close()  # 关闭设备
    content = retstr.getvalue()  # 抓取文本
    retstr.close()  # 关闭文本输出
    return content  # 返回文本


# 打开一个网络文件
pdffile = urllib.request.urlopen("http://pythonscraping.com/pages/warandpeace/chapter1.pdf")
outputstring = readpdf(pdffile)  # 处理文本
print(outputstring)  # 输出文本
