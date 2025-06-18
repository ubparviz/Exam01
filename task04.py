# Bo‘linmadan qoldiqni topish

print("\n===Hohlgan siz kiritgan sonni 4 ga bo'linadimi yo'qmi aniqlab beraman :)===")

number = int(input("Son kiriting: "))

if number % 4 != 0:
    print(f"{number} soni 4 ga bo'linmas ekan. Qoldiq: {number%4}")

else:
    print(f"{number} soni 4 ga bo'linadi. Javob: {number/4}")