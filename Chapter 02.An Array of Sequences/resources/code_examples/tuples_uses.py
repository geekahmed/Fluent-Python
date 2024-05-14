# Tuples as records
lax_cords = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32_450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)
for country, _ in traveler_ids:
    print(country)


# Tuples as Immutable Lists
"""
Be aware that the immutability of a tuple only applies to the references contained in it.
References in a tuple cannot be deleted or replaced.
But if one of those references points to a mutable object, and that object is changed, then the value of the tuple changes.

"""
a = 10
c = 8

class B:
    def __init__(self, value) -> None:
        self._value = value
    def set_value(self, new_value):
        self._value = new_value
    def __str__(self) -> str:
        return f'Value of object is: {self._value}'


b = B(value=9)


t = (a, b)

print('%s %s' % t)

t[1].set_value(5)
print('%s %s' % t)


# Check if a tuple is hashable (contains items that are hashable)

def fixed(o):
    try:
        hash(o)
    except TypeError:
        return False
    return True

fixed_tuple = (10, 's', (10, 12))
mutable_content_tuple = (10, 's', [4, 5])

print(f'Is fixed tuple is hashable? {fixed(fixed_tuple)}')
print(f"Is mutable content tuple is hashable? {fixed(mutable_content_tuple)}")
