from win32com import client as wc

word = wc.Dispatch('Word.Application')
doc = word.Documents.Open(r'C:\Users\Tsinghua-yincheng\Desktop\day24down\doc\1.doc')
doc.SaveAs('C:\\Users\\Tsinghua-yincheng\\Desktop\\day24down\\doc\\test.text', 2)
doc.Close()
word.Quit()
