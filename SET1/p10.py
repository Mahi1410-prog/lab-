
def convert_base(number, from_base, to_base):
    # Convert the number from the given base to base 10
    base_10_number = int(number, from_base)

    # Convert the base 10 number to the desired base
    if to_base == 10:
        return str(base_10_number)

    digits = "0123456789ABCDEF"
    result = ""
    while base_10_number > 0:
        remainder = base_10_number % to_base
        result = digits[remainder] + result
        base_10_number = base_10_number // to_base

    return result



number = "1010"
from_base = 2
to_base = 16
converted_number = convert_base(number, from_base, to_base)
print(f"The number {number} in base {from_base} is {converted_number} in base {to_base}.")