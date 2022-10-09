sec = int(input())
min = 60
hour = 3600
day = 86400
if sec >= day:
    print(sec // day, "дней")
else:
    print("0 дней")
if sec >= hour:
    print(sec // hour, "часов")
else:
    print("0 часов")
if sec >= min:
    print(sec // min, "минут")
else:
    print("0 минут")

