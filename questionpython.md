# Python Placement Question Bank

**90 Python coding questions for technical-round practice**

## Overview

| Level | Questions | Focus |
|---|---:|---|
| Basic | 50 | Core syntax, loops, lists, strings, dictionaries, simple functions |
| Intermediate | 30 | Problem solving, reusable logic, hashing, sliding-window ideas |
| Advanced | 10 | Algorithms, complexity, data structures, Python-specific concepts |

## How to Use This Sheet

1. Solve the **Basic** section first. Write code yourself before checking any solution.
2. For list/array problems, first use simple loops; then try to reduce time complexity.
3. For Bubble Sort practice, record both **comparisons** and **swaps** on paper for at least 3 test cases.
4. In technical rounds, explain your **approach, edge cases, and time/space complexity** after coding.

## Progress

| Level | Completed | Revised |
|---|---|---|
| Basic | ____ / 50 | ____ / 50 |
| Intermediate | ____ / 30 | ____ / 30 |
| Advanced | ____ / 10 | ____ / 10 |

## Topic Mix

| Section | Lists / Arrays | Strings | Dictionaries | Loops / Number Logic | Functions / Mixed |
|---|---:|---:|---:|---:|---:|
| Basic | 13 | 10 | 10 | 10 | 7 |
| Intermediate | 7 | 6 | 6 | 5 | 6 |
| Advanced | 2 | 2 | 2 | 2 | 2 |

### Suggested Order

**1. Lists / Arrays → 2. Loops / Number Logic → 3. Strings → 4. Dictionaries → 5. Functions / Mixed**

Your target areas are covered heavily, and **Bubble Sort**, **comparison count**, **swap count**, **second-largest**, and **second-smallest** problems are included explicitly.

> **Interview habit:** After every solution, be ready to answer: *Why does it work? What happens for an empty list? What about duplicates? What is the time complexity?*

> **Practice rule:** Try without `sort()`, `sorted()`, `max()`, `min()`, or shortcuts first when the question specifically asks you not to use them.

---

# BASIC - 50 QUESTIONS

**Questions 1-50 | Start here. Focus on clean logic, loops, lists, dictionaries, and simple functions.**

## Lists / Arrays

1. **Find the sum of all numbers in a list** without using `sum()`.
2. **Find the largest element in a list** without using `max()`.
3. **Find the smallest element in a list** without using `min()`.
4. **Reverse a list** without using `reverse()` or slicing.
5. **Count how many even and odd numbers** are present in a list.
6. **Find the second largest distinct number** in a list.
7. **Find the second smallest distinct number** in a list.
8. **Remove duplicates from a list** while keeping the original order.
9. Given numbers from `1` to `n` with one number missing, **find the missing number**.
10. Perform a **linear search** and return the index of a target value; return `-1` when it is absent.
11. **Implement Bubble Sort** in ascending order without using `sort()` or `sorted()`.
12. In **Bubble Sort, count the total number of comparisons and swaps** made for a given list.
13. **Merge two already sorted lists** into one sorted list without calling a sorting function.

## Strings

14. **Count the number of characters in a string** without using `len()`.
15. **Reverse a string** using a loop.
16. **Check whether a string is a palindrome.**
17. **Count vowels and consonants** in a string.
18. **Remove all spaces** from a string.
19. **Find the first non-repeating character** in a string.
20. **Build a character-frequency dictionary** for a string.
21. **Check whether two strings are anagrams** of each other.
22. **Find the longest word** in a sentence.
23. **Count how many digits** are present in a string.

## Dictionaries

24. Create a dictionary that stores the **frequency of each number** in a list.
25. Given a dictionary, **safely access a key** and print a default value when the key is missing.
26. **Merge two dictionaries** into one dictionary.
27. **Find the key that has the maximum value** in a dictionary.
28. **Invert a dictionary** (value becomes key) when all values are unique.
29. **Count the frequency of each word** in a sentence using a dictionary.
30. Remove dictionary entries whose **values are duplicated**, keeping only the first occurrence of each value.
31. **Group a list of words by their first character** using a dictionary.
32. **Sort a dictionary by its values in descending order.**
33. Given a nested dictionary of students and marks, **calculate each student's average.**

## Loops / Number Logic

34. **Print numbers from 1 to n** using a loop.
35. **Find the sum of numbers from 1 to n** using a loop.
36. **Find the factorial of a number** using a loop.
37. **Print all prime numbers between 1 and n.**
38. **Generate the first n Fibonacci numbers** using a loop.
39. **Find the sum of digits** of an integer.
40. **Check whether an integer is a palindrome.**
41. **Check whether a number is an Armstrong number.**
42. **Reverse an integer** without converting it to a string.
43. **Print the multiplication table** of a given number.

## Functions / Mixed

44. Write a function that **returns the largest of three numbers**.
45. Write a function `is_prime(n)` that **returns `True` or `False`**.
46. Write a function `factorial(n)` that **returns the factorial** of `n`.
47. Write a function `bubble_sort(arr)` that **returns the sorted list**.
48. Write a function that **counts vowels** in a string.
49. Write a function that **returns the second largest distinct element** in a list.
50. Write a **simple calculator function** that accepts two numbers and an operator (`+`, `-`, `*`, `/`).

---

# INTERMEDIATE - 30 QUESTIONS

**Questions 51-80 | Use these after you can solve the basic set without copying a solution.**

## Lists / Arrays

51. **Rotate a list to the right by `k` positions** without using a library rotation function.
52. **Find the intersection of two lists**, returning each common value only once.
53. **Find the union of two lists** without using `set()`.
54. **Move all zeros to the end of a list** while keeping the relative order of non-zero elements.
55. **Find the majority element:** the value that occurs more than `n/2` times, if it exists.
56. **Find all pairs in a list** whose sum equals a given target value.
57. **Find the longest contiguous increasing subarray** in a list.

## Strings

58. **Find the length of the longest substring without repeating characters.**
59. **Compress a string using run-length encoding.** Example: `aaabbc -> a3b2c1`.
60. **Find the first repeating character** in a string and its first index.
61. **Check whether one string is a rotation of another string.**
62. **Count word frequency in a sentence** while ignoring case and punctuation.
63. **Find the most frequent character** in a string; define how you handle ties.

## Dictionaries

64. **Create a dictionary from two lists:** one containing keys and one containing values.
65. Given nested sales data for several products, **calculate the total sales for each product**.
66. **Merge two dictionaries by adding values** for keys that appear in both.
67. **Sort a dictionary of student records** by a chosen field such as marks.
68. **Group a list of words into anagram groups** using a dictionary.
69. **Invert a dictionary when multiple keys can share the same value**; store those keys in a list.

## Loops / Number Logic

70. **Find the prime factorization** of a positive integer using loops.
71. **Find the GCD and LCM** of two numbers using loops and basic arithmetic.
72. **Check whether a number is a perfect number.**
73. **Convert a decimal number to binary** without using `bin()`.
74. **Convert a binary string to decimal** without using `int(binary, 2)`.

## Functions / Mixed

75. Write a reusable function that **returns both the Bubble Sort comparison count and swap count**.
76. Write one function that **returns the second largest and second smallest distinct values** in a list.
77. Write a function that **removes duplicates from a list while preserving order**.
78. **Implement factorial twice** - once iteratively and once recursively - and compare the approaches.
79. Write a function that **returns a frequency dictionary** for either a list or a string.
80. Write a **password-validation function** using helper functions for length, digit, uppercase, lowercase, and special character checks.

---

# ADVANCED - 10 QUESTIONS

**Questions 81-90 | Placement-level problem solving with complexity, data structures, and Python-specific thinking.**

## Lists / Arrays

81. **Implement Quick Sort from scratch** and explain the best, average, and worst-case time complexity.
82. **Implement Merge Sort from scratch** and modify it to count the number of inversions in the list.

## Strings

83. **Find the longest substring with at most `k` distinct characters** using a sliding-window technique.
84. **Find the minimum number of deletions needed** to make two strings anagrams of each other.

## Dictionaries / Hashing

85. **Find a continuous subarray whose sum equals `k`** using a dictionary/prefix-sum approach; return its indices.
86. **Find the top `k` most frequent elements** using a frequency dictionary and a suitable data structure.

## Loops / Problem Solving

87. **Find the longest consecutive sequence** in an unsorted list with near `O(n)` average time.
88. Given overlapping intervals, **merge them into a minimal set of non-overlapping intervals.**

## Functions / Python

89. Write a **decorator that measures and prints the execution time** of any function.
90. Build a function that **reads a text file, counts word frequencies with a dictionary, and prints the top 10 words** while ignoring punctuation and case.

---

# Suggested Practice Tracking

| Q. Range | Status | Notes |
|---|---|---|
| 1-10 | ☐ | ______________________________ |
| 11-20 | ☐ | ______________________________ |
| 21-30 | ☐ | ______________________________ |
| 31-40 | ☐ | ______________________________ |
| 41-50 | ☐ | ______________________________ |
| 51-60 | ☐ | ______________________________ |
| 61-70 | ☐ | ______________________________ |
| 71-80 | ☐ | ______________________________ |
| 81-90 | ☐ | ______________________________ |

## Technical-Round Checklist

For each problem, practice explaining:

- **Approach:** What is the idea?
- **Edge cases:** Empty input? One element? Duplicates?
- **Complexity:** Time complexity and space complexity.
- **Python choice:** Why did you use this loop, data structure, or function?
