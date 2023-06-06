from datetime import datetime

date = datetime.today()
print(f'Seconds since January 1, 1970: {date.timestamp():,.4f}', end='')
print(f' or {f"{date.timestamp():.2E}".lower()} in scientific notation')
print(date.strftime('%b %d %Y'))
