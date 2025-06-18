# Foydalanuvchi kiritgan kod faqat raqamlardan iboratligini tekshirish

parol = input("Parol kirting: ").strip()

if parol.isdigit():
    print("Parol qabul qilindi")
else:
    print("Parol faqat raqamdan iborat bo'lsin")