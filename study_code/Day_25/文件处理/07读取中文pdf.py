import urllib.request  # 打开网页
import pdfminer.pdfinterp  # 管理PDF资源
import pdfminer.converter  # 文本转换
import pdfminer.layout  # 处理pdf布局
import pdfminer.pdfparser
import io  # 输入输出

path = r"D:\Resources\Python\Python3开发实践真正完整版 尹成大神主讲 代码 + 课件\day25-2 Python文件格式与服务器入侵\安装docx库.pdf"
file = open(path, "rb")  # 打开文件
pdffile = pdfminer.pdfparser.PDFParser(file)  # 解析pdf文本
doc = pdfminer.pdfparser.PDFDocument()  # 创建pdf文档
pdffile.set_document(doc)  # 解析工具链接pdf文档
doc.set_parser(pdffile)
doc.initialize()  # 初始化  为空没有密码， 有密码"12233"
rsmgr = pdfminer.pdfinterp.PDFResourceManager()  # 资源管理器
lap = pdfminer.layout.LAParams()  # 处理布局
device = pdfminer.converter.PDFPageAggregator(rsmgr, laparams=lap)  # 转换
interpreter = pdfminer.pdfinterp.PDFPageInterpreter(rsmgr, device)  # 抓页数
if not doc.is_extractable:
    pass
else:
    for page in doc.get_pages():  # 遍历每一个页面
        interpreter.process_page(page)  # 抓取每一页
        layout = device.get_result()
        for x in layout:
            text = x.get_text()
            print(text)
