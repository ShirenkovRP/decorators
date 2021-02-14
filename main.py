from decorators import log_decor
from countries import CountryGenerator as generator


@log_decor("log.txt")
def sum(a, b):
    return a + b


@log_decor("log.txt")
def my_function(a, b, path):
    return generator(a, b, path)


for i in my_function(5, 8, "countries.json"):
    print(i)

print(sum(2, 3))
