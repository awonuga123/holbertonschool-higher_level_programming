# 0x04. Python - More Data Structures: Set, Dictionary

In this project, I learned about sets and dictionaries in Python. I practiced using them with the `lambda`, `map`, `filter`, and `reduce` methods.

## Function Prototypes
Prototypes for functions written in this project:

| File                           | Prototype                                          |
| ------------------------------ | -------------------------------------------------- |
| `0-square_matrix_simple.py`    | `def square_matrix_simple(matrix=[]):`             |
| `1-search_replace.py`          | `def search_replace(my_list, search, replace):`    |
| `2-uniq_add.py`                | `def uniq_add(my_list=[]):`                        |
| `3-common_elements.py`         | `def common_elements(set_1, set_2):`               |
| `4-only_diff_elements.py`      | `def only_diff_elements(set_1, set_2):`            |
| `5-number_keys.py`             | `def number_keys(a_dictionary):`                   |
| `6-print_sorted_dictionary.py` | `def print_sorted_dictionary(a_dictionary):`       |
| `7-update_dictionary.py`       | `def update_dictionary(a_dictionary, key, value):` |
| `8-simple_delete.py`           | `def simple_delete(a_dictionary, key=""):`         |
| `9-multiply_by_2.py`           | `def multiply_by_2(a_dictionary):`                 |
| `10-best_score.py`             | `def best_score(a_dictionary):`                    |
| `11-mutiply_list_map.py`       | `def mutiply_list_map(my_list=[], number=0):`      |
| `12-roman_to_int.py`           | `def roman_to_int(roman_string):`                  |

## Tasks
* **Squared simple**
  * `0-square_matrix_simple.py`: Python function that computes the square value of all integers of a matrix.
  * The parameter `matrix` is a two-dimensional array.
  * Returns a matrix of the same size as `matrix` where each value is the square of the input value.
  * The initial matrix is not modified.
  * Without importing modules.

* **Search and replace**
  * `1-search_replace.py`: Python function that replaces all occurences of an element by another in a new list.
  * The parameter `my_list` is the initial list.
  * The parameter `search` is the element to replace in the list.
  * The parameter `replace` is the new element.
  * Without importing modules.

* **Unique addition**
  * `2-uniq_add.py`: Python function that adds all unique integers in a list (once for each integer).
  * Without importing modules.

* **Present in both**
  * `3-common_elements.py`: Python function that returns a set of common elements in two sets.
  * Without importing modules.

* **Only differents**
  * `4-only_diff_elements.py`: Python function that returns a set of all elements present in only one set.
  * Without importing modules.

* **Number of keys**
  * `5-number_keys.py`: Python function that returns the number of keys in a dictionary.
  * Without importing modules.

* **Print sorted dictionary**
  * `6-print_sorted_dictionary.py`: Python function that prints a dictionary by ordered keys.
  * The function assumes all keys are strings.
  * Keys are printed in alphabetic order.
  * Keys are only sorted on the first level.
  * Dictionary values can have any type.
  * Without importing modules.

* **Update dictionary**
  * `7-update_dictionary.py`: Python function that replaces or adds key/value pairs in a dictionary.
  * The parameter `key` is always a string.
  * The parameter `value` is any type.
  * If a key exists in the dictionary, the value is replaced.
  * If a key does not exist in the dictionary, it is created.
  * Without importing modules.

* **Simple delete by key**
  * `8-simple_delete.py`: Python function that deletes a key in a dictionary.
  * The paramter `key` is always a string.
  * If the key does not exist, the dictionary does not change.
  * Without importing modules.

* **Multiply by 2**
  * `9-multiply_by_2.py`: Python function that returns a new dictionary with all values multiplied by 2.
  * The function assumes all values are integers.
  * Without importing modules.

* **Best score**
  * `10-best_score.py`: Python function that returns a key value with the biggest integer value.
  * The function assumes all values are integers.
  * The function assumes all students have a different score.
  * If no score is found, the functino returns `None`.
  * Without importing modules.

* **Multiply by using map**
  * `11-mutiply_list_map.py`: Python function that returns a list with all values multiplied by a number using `map`.
  * Returns a new length of the same length has `my_list` with each value multiplied by `number`.
  * The initial list is not modified.
  * Without using loops or importing modules.

* **Roman to Integer**
  * `12-roman_to_int.py`: Python function that converts a roman numeral to an integer.
  * The function assumes the number will be between 1-3999.
  * If the parameter `roman_string` is not a string or `None`, the function returns `0`.