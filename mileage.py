print("would you like to convert from miles (m) or kilometers (k)?")
distance_format = input()
print(f"how many {distance_format} would you like to convert?")
units = input()
if distance_format == "k":
  converted_units = float(units)/1.61
  converted_format = "miles"
else:
  converted_units = float(units)*1.61
  converted_format = "kilometers"
converted_units = round(converted_units,2)
print(f"ok that equals {converted_units} {converted_format}")
