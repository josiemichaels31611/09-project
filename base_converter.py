num = int(input("Enter a number: "))
base = int(input("Enter a base: "))
def convert_b10_to_other(num, base):
    newnum = []
    while num > 0:
        newnum.append(str(num%base))
        num = num//base
    return "".join(newnum[::-1])
print(convert_b10_to_other(num, base))
num2 = int(input("Enter a number that's not in base 10: "))
base2 = int(input("Enter what base it is in: "))
def convert_other_to_b10(num2, base2):
    #num3 = num2[::-1]        
    og_num = 0
    str_num2 = str(num2)
    for digit in range(len(str_num2)):
        num3 = str_num2[-1 - digit]
        og_num += int(base2) ** int(digit) * int(num3)
    return(og_num)
print(convert_other_to_b10(num2, base2))