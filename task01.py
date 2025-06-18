# Butun sonning kvadratini topish

while True:
    number = float(input("Son kirting: "))
    if number.isalpha():
        print("Iltimos raqam kirting!")
    
    else:
        result = pow(number, 2)

    print(f"Siz kiritgan sonn ya'ni: {number} ni kvadrati {result}")