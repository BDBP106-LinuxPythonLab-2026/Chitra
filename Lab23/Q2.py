from utils import math_utils, string_utils
a, b = 34, 45
print("Addition:", math_utils.add(a, b))
print("Subtraction:", math_utils.subtract(a, b))
print("Multiplication:", math_utils.multiply(a, b))
print("Division:", math_utils.divide(a, b))
print("Remainder:", math_utils.remainder(a, b))
# String operations using BDBH and 101
s1, s2 = "BDBH", "101"
print("Uppercase:", string_utils.upper_case(s1))
print("Lowercase:", string_utils.lower_case(s1))
print("Concatenation:", string_utils.concatenate(s1, s2))