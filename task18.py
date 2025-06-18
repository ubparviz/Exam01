# BMI hisoblash va tasnif
# Vazifa: Foydalanuvchidan vazn (kg) va bo'y (m) so'rang. BMI ni hisoblang va tasniflang:

# BMI < 18.5: "Kam vazn"
# 18.5 ≤ BMI < 25: "Normal vazn"
# 25 ≤ BMI < 30: "Ortiqcha vazn"
# BMI ≥ 30: "Semizlik"
# Formula: BMI = vazn / (bo'y)²

# Qo'shimcha tekshiruvlar:

# Vazn va bo'y musbat bo'lishi kerak
# Bo'y 0.5-3.0 m oralig'ida bo'lishi kerak
# Vazn 1-500 kg oralig'ida bo'lishi kerak

# BMI hisoblash va tasnif

import sys


height = float(input("Bo'yingizni kiriting (metrda): "))

if height <= 0:
    print("Bo'y musbat bo'lishi kerak")
    sys.exit()

elif height < 0.5 or height > 3:
    print("Bo'y 0.5-3.0 m oralig'ida bo'lishi kerak")
    sys.exit()

weight = float(input("Vazningizni kiriting (kgda): "))

if weight <= 0:
    print("Vazn musbat bo'lishi kerak")
    sys.exit()

elif weight < 1 or weight > 500:
    print("Vazn 1-500 kg oralig'ida bo'lishi kerak")
    sys.exit()


BMI = weight / pow(height, 2)
print(f"BMI: {round(BMI)}")

if BMI < 18.5:
    print("Holat: Kam Vazn")

elif BMI >= 18.5 and BMI < 25:
    print("Holat: Normal Vazn")

elif BMI >= 25 and BMI <= 30:
    print("Holat: Ortiqcha Vazn")

elif BMI > 30:
    print("Holat: Semizlik")
