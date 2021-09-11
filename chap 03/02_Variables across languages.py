# ----------------------------------------------------------------------------
# The more relaxed languages tend to be more flexible and result in less code
# The rules of python :-
# 1- Names contain letters, numbers, and underscores
# 2- The name shouldn't start with a number as (3Mohammed)
# 3- Spaces are not allowed as (Mohammed Hassan > right : Mohammed_Hassan)
# 4- The capital name is not the same as the small name as (Mohammed != mohammed)
# 5- Variables cannot be keywords as (print, and, try)
# ----------------------------------------------------------------------------
import keyword
print(keyword.kwlist)

Name = "Mohammed"
print(Name)
print(type(Name))

age = 21
print(age)
print(type(age))

cookies = "true"
print(cookies)
