username = input("أدخل اسم المستخدم: ").strip().lower()

if username == "roba":
    print("مرحباً روبا")
elif username == "admin":
    print("مرحباً أيها المدير")
else:
    print("المستخدم غير معروف")