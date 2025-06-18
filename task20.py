# To'g'ri javob kiritilmaguncha davom et
# Dastur foydalanuvchidan “O'zbekiston poytaxti nima?” deb so'raydi. “Toshkent” deb to'g'ri javob berguncha so'rashda davom etadi.

while True:
    javob = input("O'zbekiston poytaxti nima? ")
    if javob.strip().lower() == "toshkent":
        print("To'g'ri javob!")
        break
    else:
        print("Noto'g'ri. Qayta urinib ko'ring.")
