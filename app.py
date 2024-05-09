import os
import json

f = open('barang.json')
data = json.load(f)

user_barang = []
user_uang = []
sum = 0
user_kembalian = []

def getData () :
    for i in range(2):
        user_barang = int(input("Masukkan Barang :"))
        user_uang = int(input("Masukkan Uang Customer :"))
        os.system('cls')
        user_kembalian = user_uang-user_barang
    sum += user_barang+user_kembalian
def showData ():
    for i in range(len(user_barang)):
          print(user_barang)
          print(user_uang)
          print(user_kembalian)
          print(sum)
    f.close()
getData()
showData()
