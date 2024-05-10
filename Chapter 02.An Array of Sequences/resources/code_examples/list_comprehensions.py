# Walrus operator in python
"""
**What is the Walrus Operator?**

Introduced in Python 3.8, the walrus operator (`:=`) is also called the "assignment expression operator."  It allows you to:

1. **Assign values to variables within expressions:**  This means you can create and assign variables directly within loops, conditionals, or other complex expressions.
2. **Use the assigned value immediately:** The variable you create can be used right away in the surrounding expression.

**Syntax**

The walrus operator's syntax is simple:

```python
name := expression
```

* `name`: The name of the variable you want to assign a value to.
* `expression`: The expression evaluated, and its result is assigned to the variable `name`.

**Common Use Cases**

* **Simplifying Code:** The walrus operator can reduce repetition in your code, particularly in cases where you calculate a value that you need to use multiple times in an expression.
* **Improved Readability:** In some situations, using the walrus operator can make the intent of your code clearer, especially within loops or conditional statements.

**Examples**

1. **In a `while` loop:**

```python
while (line := file.readline()) != "":  # Assign and check line in one step
    print(line) 
```

2. **In an `if` statement:**

```python
if (match := pattern.search(text)) is not None:
    print("Found match:", match.group())
```

3. **In a list comprehension:**

```python
[y for x in data if (y := x * 2) > 10]  # Filter based on a calculation
```

**Cautions**

* **Readability:** While the walrus operator can be concise, be mindful of overusing it, as it might make your code less readable in complex scenarios.
* **Python Version:** The walrus operator is only available in Python 3.8 and newer.

**Alternative (Pre-Python 3.8)**

Before the walrus operator, you would often have to repeat the calculation or use a temporary variable:

```python
match = pattern.search(text)
if match is not None:  # Checking the value again
    print("Found match:", match.group()) 
```

"""

# The use of list comp VS Map and Filter 

symbols = '$¢£¥€¤'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print("Using List Comp", beyond_ascii)

beyond_ascii_map_filter = list(filter(lambda c: c > 127, map(ord, symbols)))
print("Using List Map Filter", beyond_ascii_map_filter)


# Speed test between using list comp and use the map and filter
import timeit
TIMES = 10000
SETUP = """
symbols = '$¢£¥€¤'
def non_ascii(c):
    return c > 127
"""
def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *(f'{x:.3f}' for x in res))

clock('listcomp        :', '[ord(s) for s in symbols if ord(s) > 127]')
clock('listcomp + func :', '[ord(s) for s in symbols if non_ascii(ord(s))]')
clock('filter + lambda :', 'list(filter(lambda c: c > 127, map(ord, symbols)))')
clock('filter + func   :', 'list(filter(non_ascii, map(ord, symbols)))')

# Cartesian Product using List Comp
# Produce a list of T-shirts available in two colors and three sizes.

colors = ["Black", "White"]
sizes = ["M", "S", "L"]

# Using nested for loop
tshirts_for_loop = []
for color in colors:
    for size in sizes:
        tshirts_for_loop.append((color, size))

print("T-Shirts using the nested for loop: ", tshirts_for_loop)

# Using List Comp.
tshirts = [(color, size) for color in colors for size in sizes]
print("T-Shirts using List Comp.: ", tshirts)


# Using Generator Expressions
for tshirt in (f'{c} {s}' for c in colors for s in sizes): 
     print(tshirt)


# What are the generator expressions in python? How to use them properly? What is the relation with list comprehension?
"""
**What are Generator Expressions?**

* **Lazy Evaluation:** Unlike list comprehensions, which build an entire list in memory, generator expressions create an iterator. This iterator produces values on demand, only when requested. This can be a huge memory saver when working with large datasets.
* **Syntax:**  Generator expressions look almost identical to list comprehensions, but they use parentheses `()` instead of square brackets `[]`.
* **Purpose:** Generator expressions are ideal when you want to iterate over a sequence of values but don't need to store them all at once. 

**How to Use Them**

Here's the basic structure of a generator expression:

```python
(expression for item in iterable if condition)
```

* `expression`: The operation or transformation you apply to each `item`.
* `item`: The variable representing each element in the `iterable`.
* `iterable`: The sequence you're iterating over (list, string, etc.).
* `condition` (optional): A filter to include only certain items.

**Examples**

1. **Squares of numbers:**

```python
squares = (x**2 for x in range(10)) 
for num in squares:
    print(num)
```

2. **Filtering even numbers:**

```python
evens = (x for x in range(20) if x % 2 == 0)
print(list(evens))  # Convert to list to see all values
```

3. **Processing file lines:**

```python
with open('myfile.txt') as f:
    long_lines = (line for line in f if len(line) > 80)
    # Process long_lines
```

**Relation to List Comprehensions**

* **Syntax:** The only syntactic difference is the use of parentheses in generator expressions and square brackets in list comprehensions.
* **Memory Usage:** List comprehensions create a full list, while generator expressions create an iterator, making them much more memory efficient for large data.
* **Usage:** Use list comprehensions when you need the entire list in memory (e.g., for random access or repeated operations). Use generator expressions when you want to iterate over values lazily (e.g., when processing data streams or filtering large datasets).

**Key Benefits**

* **Memory Efficiency:** Generator expressions save memory, especially when dealing with massive data sets.
* **Performance:** Lazy evaluation can lead to faster execution in certain scenarios.
* **Cleaner Code:** They offer a concise and elegant syntax for creating iterators.

**Caveats**

* **One-Time Use:** Generator expressions are single-use iterators. You can only iterate over them once.
* **Limited Operations:** You can't perform random access or slicing on a generator expression like you can with a list.

"""