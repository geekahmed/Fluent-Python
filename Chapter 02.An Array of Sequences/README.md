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