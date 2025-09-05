import camelot

tb = camelot.read_pdf("foo.pdf" , pages="1", flavor="stream")
print(tb)

tb.export("human.csv", f="csv", compress=True)  # json, excel, html
tb[0].to_csv("humans.csv")