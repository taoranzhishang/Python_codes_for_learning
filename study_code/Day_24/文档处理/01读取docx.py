import docx  # 只能处理docx文件


def getText(filepath):
    doc = docx.Document(filepath)  # 打开文档
    fulltext = []
    for para in doc.paragraphs:  # 遍历每一个段落
        fulltext.append(para.text)
    return fulltext


data = getText(r"C:\Users\taora\Desktop\中国高校产学研创新基金新一代信息技术创新项目申报指南.docx")
for line in data:
    print(line)
