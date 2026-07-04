import random
carcater = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
contraseña = int(input("introduce la longitud de tu contraseña: "))
password = ""
for i in range(contraseña):
    contraseña = random.choice(carcater)
    password += contraseña
print(password)