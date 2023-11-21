#  a program that works out whether if a given year is a leap year.
# A normal year has 365 days, leap years have 366, with an extra day in February.
# The reason why we have leap years is really fascinating, this video does it more justice.
# Which year do you want to check?

year = int(input())

if year & 4 == 0:
  if year & 100 == 0:
        # Not a leap year, unless special case
    if year & 400 == 0:
      print("leep year")
    else:
      print("Not leep year")
  else:
    print("Leep year")
else:
  print("not leep year")

