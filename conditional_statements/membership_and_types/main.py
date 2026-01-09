# Product details
description = "Imported honey, raw and unfiltered"
price = "5.99"
count = 120

contains_raw = "raw" in description
contains_Imported = "Imported" in description

price_is_float_type = type(price) == float
count_is_int_type = type(count) == float

print("Contains 'raw': ", contains_raw)
print("Contains 'Imported': ", contains_Imported)
print("Is price a float
