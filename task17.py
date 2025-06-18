#  Baholash tizimi
# Vazifa: Foydalanuvchidan ball (0-100) so'rang va bahoni chiqaring:

# 90-100: "A (A'lo)"
# 80-89: "B (Yaxshi)"
# 70-79: "C (Qoniqarli)"
# 60-69: "D (Qoniqarsiz)"
# 0-59: "F (Rad)"
# Agar 0-100 oralig'idan tashqari son kiritilsa, "Ball 0-100 oralig'ida bo'lishi kerak!" deb chiqaring.

score = int(input("Ballingizni kirting: "))

if score >= 90 and score <= 100:
    print("A (A'lo)")

elif score >= 80 and score <= 89:
    print("B (Yaxshi)")

elif score >= 70 and score <= 79:
    print("C (Qoniqarli)")

elif score >= 60 and score <= 69:
    print("D (Qoniqarsiz)")

elif score >= 0 and score <= 59:
    print("F (Rad)")

else:
    print("Ball 0-100 oralig'ida bo'lishi kerak!")