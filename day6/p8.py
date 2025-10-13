# from datetime import datetime,timezone, timedelta
# dt = datetime.utcnow()
# print("Current UTC datetime:", dt)

# local_dt = dt.replace(tzinfo=timezone.utc).astimezone(tz=None)
# print("Current local datetime:", local_dt)

# frankfurt_time = timezone(timedelta(hours=2))  # UTC+2
# frankfurt_dt = dt.replace(tzinfo=timezone.utc).astimezone(frankfurt_time)
# print("Frankfurt datetime:", frankfurt_dt)
# print("Frankfurt datetime:", frankfurt_dt)

from datetime import date, datetime, time
new_year = datetime(2026, 1, 1)
print("New Year 2026:", new_year)
now = datetime.now()
diff = new_year - now
print("Days until New Year 2026:", diff.days)