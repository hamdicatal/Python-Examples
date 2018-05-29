def AsalMi(num):
    if num == 2:
        return True

    if num > 2:
        for i in range(2, num):
            if(num % i == 0):
                return False
        return True

num = -1
count = 0

while num != 0:
    num = input("Sayi girin: ")
    if AsalMi(num):
        count += 1

print count, " adet asal sayi girdiniz"
