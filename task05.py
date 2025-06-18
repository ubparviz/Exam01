# Foydalanuvchi yoshini aniqlash (2025-yilga nisbatan)

birth_year = int(input("Tug'ilgan yilizni kirting: "))
age = 2025 - birth_year

if age < 18:
    print(f"Yoshingiz {age} yoshda ekan. Siz hali balog'atga yetmagansiz! Kelajak hayotizda omad tilayman")
elif age >= 18 and age <= 35:
    print(f"Yoshingiz {age} yoshda ekan. Hayotizni ajoyib lahzasini o'tkaziyapsiz")
else:
    print(f"Yoshingiz {age} yoshda ekan. Sizdan ko'p narsani o'rgansa bo'ladi") 


