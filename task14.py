# Fayl nomi .pdf, .docx, yoki .txt bilan tugashini tekshiring

file = input("Fayl kiriting: ").strip()

if file.endswith(".pdf") or file.endswith(".docx") or file.endswith(".txt"):
    print(True)
else:
    print(False)