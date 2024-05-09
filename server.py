
import json
 
calculation = 0 
# JSON file
f = open ('barang.json') 
 

data = json.loads(f.read())

 
print("1.Fortune       : 15000")
print("2.Indomie       : 5000")
print("3.Beras         : 20000")
print("4.Gula Kristal  : 15000")
print("5.Tepung Terigu : 8000")

for i in range(2):

    choice = int(input("Enter number the stuff do you want buy :"   ))
    
calculation += choice(data['barang_harga'])
try :
    print(data[calculation.upper()])
except:
    print('Invalid Number')