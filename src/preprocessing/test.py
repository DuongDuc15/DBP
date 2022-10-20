import py_vncorenlp

toolkit_path = r"C:\Users\Admin\Documents\Learning\DBP\code\coding\src\preprocessing\toolkit"

model = py_vncorenlp.VnCoreNLP(annotators=["wseg"], save_dir=toolkit_path)
text = "Ông Nguyễn Khắc Chúc đang làm việc tại Đại học Quốc gia Hà Nội."#.
text = "Bà Lan, vợ ông Chúc, cũng làm việc tại đây."
text = 'Cái thằng con này, anh ta liền vơ một chiếc móc quần áo chạy ra ngoài đánh cho đứa con trai đang ngồi chơi một trận.'
output = model.word_segment(text)
print(output)


# model.print_out(model.annotate_text("Ông Nguyễn Khắc Chúc  đang làm việc tại Đại học Quốc gia Hà Nội. Bà Lan, vợ ông Chúc, cũng làm việc tại đây."))