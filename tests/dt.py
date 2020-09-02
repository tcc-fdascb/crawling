from datetime import datetime as dt

a = int(dt.timestamp(dt.now()))
print(a)

b = dt.fromtimestamp(a)
print(b)
