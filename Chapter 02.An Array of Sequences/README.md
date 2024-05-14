# Chapter 02. An Array of Sequences

**Key Points About Python Sequences**

* **Unified Interface:** Python offers a consistent way to work with various sequence types (strings, lists, byte sequences, etc.). This is a powerful legacy from the ABC language that influenced Python's design.

* **Benefits of Uniformity:**
    * **Less Reinvention:** You can leverage a rich set of built-in operations (iteration, slicing, sorting, etc.) across different sequence types.
    * **API Design Inspiration:** This encourages creating libraries and APIs that work seamlessly with diverse sequences.

* **Sequence Types Covered:**
    * **General:**  Concepts that apply to all sequences (e.g., iteration, slicing).
    * **Specific:** Deep dives into lists, tuples, arrays, and queues.
    * **Not Covered:** In-depth details on strings and byte sequences (found in Chapter 4) and creating your own sequence types (covered in Chapter 12).

**Core Topics of the Chapter**

* **List Comprehensions & Generators:** Concise ways to create lists and iterators.
* **Tuples:** Understanding their dual roles as immutable lists and data records.
* **Sequence Unpacking:**  Assigning multiple values at once from a sequence.
* **Slicing:** Reading/writing to portions of sequences efficiently.
* **Specialized Sequences:** Using arrays for efficient numeric storage and queues for data processing.


## Table of Contents
* [Overview of Built-In Sequences](#overview-of-built-in-sequences)
* [List Comprehensions and Generator Expressions](#list-comprehensions-and-generator-expressions)
* [Tuples Are Not Just Immutable Lists](#tuples-are-not-just-immutable-lists)
* [Unpacking Sequences and Iterables](#unpacking-sequences-and-iterables)


### Overview of Built-In Sequences
<p align="center">
  <img src="./resources/images/Simplified memory diagrams for a tuple and an array.png" alt="Simplified memory diagrams for a tuple and an array"/>
</p>

**Sequence Types**

* **Container Sequences:**
    * Can hold items of varying types, even other containers.
    * Examples: `list`, `tuple`, `collections.deque`
* **Flat Sequences:**
    * Store values directly in their own memory, more compact but limited to holding simple types (numbers, bytes).
    * Examples: `str`, `bytes`, `array.array`

**Mutability**

* **Mutable Sequences:**
    * Can be modified in place after creation.
    * Examples: `list`, `bytearray`, `array.array`, `collections.deque`
* **Immutable Sequences:**
    * Cannot be changed once created.
    * Examples: `tuple`, `str`, `bytes`

**Key Relationships**

* **Inheritance:** Mutable sequences inherit all methods from immutable sequences and add their own mutation-specific methods.
* **Abstract Base Classes (ABCs):** Though not direct subclasses, built-in sequence types behave like they inherit from `Sequence` (immutable) and `MutableSequence` (mutable).

### List Comprehensions and Generator Expressions
**List Comprehensions (listcomps) & Generator Expressions (genexps)**

* **Powerful and Concise:**  These tools offer efficient ways to create sequences in Python, enhancing code readability and often boosting performance.
* **List Comprehensions:**
    * **Purpose:** Build lists from existing iterables (sequences, sets, etc.).
    * **Syntax:** `[expression for item in iterable if condition]` (brackets `[]`)
    * **Focus:** Explicitly creates a new list.
    * **Best Practices:** Keep them short and avoid using them solely for side effects.
* **Generator Expressions:**
    * **Purpose:** Create iterators that generate values on the fly (lazy evaluation). Ideal for large datasets or when memory is a concern.
    * **Syntax:** `(expression for item in iterable if condition)` (parentheses `()`)
    * **Advantages:**  Memory efficient as it doesn't create the entire sequence upfront.
* **Key Differences:**
    * **Output:** Listcomps produce lists, genexps produce iterators.
    * **Memory:** Genexps are more memory-efficient for large datasets.
    * **Usage:** Listcomps when you need the whole list, genexps for efficient iteration.
* **Cartesian Products:** Both listcomps and genexps can create Cartesian products (combinations of items from multiple iterables).
    * **Listcomps:** Create a list of all combinations, potentially memory-intensive.
    * **Genexps:** Generate combinations one at a time, saving memory.

### Tuples Are Not Just Immutable Lists
**Tuples: More Than Immutable Lists**

* **Dual Roles:**
    * **Records:**  Store related data elements with meaning derived from their position (e.g., coordinates, city data).
    * **Immutable Lists:**  Similar to lists, but cannot be changed once created.

**Tuples as Records**

* **Meaning in Position:**  The order of items in a tuple matters when it represents a record.
* **Benefits:** 
    * **Clarity:**  Easy to understand the structure and meaning of data.
    * **Unpacking:**  Easily assign tuple elements to separate variables (e.g., `city, year, pop = ('Tokyo', 2003, 32450)`).
    * **No Need for Named Fields:** Often, tuples are simpler than custom classes for representing records.

**Tuples as Immutable Lists**

* **Advantages:**
    * **Clarity:**  Length is guaranteed to be fixed.
    * **Performance:** Typically more memory-efficient and faster than lists.
* **Caveat:** Immutability only applies to the references themselves. If a tuple holds references to mutable objects (like lists), those objects can be modified.
* **Hashing:** Mutable tuples cannot be used as dictionary keys or set elements because they are not hashable.
<p align="center">
  <img src="./resources/images/The content of the tuple itself is immutable.png" alt="The content of the tuple itself is immutable"/>
</p>

**Comparing Tuples and Lists**

* **Methods:**  Tuples support most of the same methods as lists, except those that modify the sequence (e.g., `append`, `insert`).
* **Suitability:** Use tuples for fixed collections and records; use lists for dynamic collections.

### Unpacking Sequences and Iterables
**Unpacking Sequences and Iterables**

* **What is Unpacking?**  Assigning elements from an iterable (e.g., tuple, list, iterator) to individual variables.
* **Benefits:**
    * Avoids using indexes to access elements.
    * Works with any iterable, even those without index support.
* **Parallel Assignment:**
    * Assigns each element to a corresponding variable.
    * Example: `latitude, longitude = (33.9425, -118.408056)`
* **Swapping Variables:**
    * Concise way to swap values: `b, a = a, b`
* **Function Calls with `*`:**
    * Unpack an iterable to provide arguments to a function.
    * Example: `divmod(*t)`  (where `t` is a tuple)
* **Using `*` to Grab Excess Items:**
    * Assign remaining items to a list.
    * Can appear in any position.
    * Example: `a, b, *rest = range(5)` (rest will be `[2, 3, 4]`)
* **Unpacking with `*` in Function Calls and Sequence Literals (Python 3.5+):**
    * Use `*` multiple times in function calls and sequence literals.
    * Example: `[*range(4), 4]` (creates a list `[0, 1, 2, 3, 4]`)
* **Nested Unpacking:**
    * Unpack nested structures with corresponding nested targets.
    * Example: `for name, _, _, (lat, lon) in metro_areas:` 
* **Unpacking with Lists:**
    * Can be used with lists, but less common.
    * Useful for handling single-record database query results.
