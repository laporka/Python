vpn = input("Enter 1 if vpn used:")
traType = input("Enter transaction type A, B or C:")
suma = input("Enter sum of transaction:")
traPerHour = input("Enter transaction per hour:")
shahrai = 0

if int(suma) > 600 and int(traPerHour) > 3 and int(vpn) == 1 :
    shahrai = 1
elif int(suma) <= 600 and int(traPerHour) <= 3 and int(vpn) == 1 :
    shahrai = 0

print(shahrai)
 