from tkinter import *



app = App('Entry fields')
Entry('Masukkan uangmu:', 'print(self.var.get())')
Entry('Password:', 'print(self.var.get())', show='*')
Entry('Enter expression', 'App.res["text"] = eval(self.var.get())')
App.res = Label('Result')
app.run()

app.run()