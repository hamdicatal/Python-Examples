def Faktoriyel(num):
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

sum = 0
num = -1

while num != 0:
    num = input("Enter num: ")
    if num != 0:
        sum += Faktoriyel(num)
        print "Faktoriyel: ", Faktoriyel(num)

print "Toplam: " , sum
