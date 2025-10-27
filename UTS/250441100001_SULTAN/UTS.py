motor_matic = 50000
motor_trail = 100000
motor_sport =  75000
diskon = 0.1
voucher = 0.05
motor_matic
motor_trail
motor_sport


motor = input("motor apa?:")
hari = int(input("berapa hari sewa motor: "))
voucher = int(input("apakah memiliki voucher? (ya/tidak): "))
    
if "matic":
        print("harga motor: ", motor_matic )
        if voucher == "ya":
            matic = motor_matic / voucher
            print("harga pakai voucher: ", matic)

        
elif "trail":
        if voucher == "ya":
             trail = motor_trail / voucher  
             print("harga motor: ", trail)
        
elif "sport":
        if voucher == "ya":
               sport = motor_sport / voucher
               print("harga motor: ", motor_sport)
        else:
               print
else:
        print("masukkan pilihan motor")
            
