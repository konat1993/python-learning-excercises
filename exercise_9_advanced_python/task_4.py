# Task 4: Create a list where numbers from 1 to 10 are doubled
# if even and tripled if odd, using list comprehension.


# duplicate_when_even_triple_when_odd = [
#     num for num in range(1, 11)
#     for _ in (
#         range(2) if num % 2 == 0
#         else range(3)
#     )
# ]

multiply_even_triple_odd = [
    num**2 if num %
    2 == 0 else num**3 for num in range(1, 11)]


# print(duplicate_when_even_triple_when_odd)
print(multiply_even_triple_odd)
