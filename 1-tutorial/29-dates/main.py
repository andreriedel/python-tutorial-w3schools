import datetime as dt

x = dt.datetime.now()

print(x)
print(x.year)
print(x.strftime("%A"))

# ---------------------------------------------------------------------------- #

x = dt.datetime(2000, 6, 12)
print(x)

print(x.strftime('%d de %B de %Y'))
