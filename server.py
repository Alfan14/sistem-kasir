import json
 
calculation = 0 
total_harga = 0
user_kembalian = 0

# JSON file
f = open ('barang.json') 
 

data = json.loads(f.read())
user_uang = int(input("masukkan uangmu"))
for index, item in enumerate(data, start=1):
    print(f"{index}. {item['barang_name']} : {item['barang_harga']}")

for i in range(2):
    try :
        choice = int(input("Enter number the stuff do you want buy :"))
        if choice < 1 or choice > len(data):
            raise ValueError ("Angka yang diinput tidak valid!")

        calculation = int(data[choice - 1]['barang_harga'])
        total_harga += calculation
        user_kembalian = user_uang-total_harga
        
    except ValueError as e:
        print('Invalid Number : {e}')
        continue
    print(f"Kembalian: {user_kembalian}")
    print(f"Total harga: {total_harga}")
    