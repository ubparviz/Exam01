# Foydalanuvchidan matn oling. for yordamida nechta unli harf (a, e, i, o, u) borligini aniqlang.

matn = input("Matn kiriting: ")

unlilar = "aeiou"
numbers_unlilar = 0

for harf in matn.lower():
    if harf in unlilar:
        numbers_unlilar += 1

print("Unli harflar soni:", numbers_unlilar)

