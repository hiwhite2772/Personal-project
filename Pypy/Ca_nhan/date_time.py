from datetime import datetime, date

now = datetime.now()
today = date.today()

print(f"Today: {today}")
print(f"Now: {now}")
print(f"Date: {today:%d/%m/%Y}")
print(f"Time: {now:%H:%M:%S}")

print(f"Time point: {now:%d thang %m nam %Y, %H:%M}")

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thurday", "Friday", "Saturday", "Sunday"]
day = days_of_week[today.weekday()]
print(f"Today is {day}")