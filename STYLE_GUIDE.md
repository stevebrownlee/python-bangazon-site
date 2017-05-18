# Style Guide for Trashy Armadillos

## Indentation
Indent using spaces.
Use 4 spaces per indentation level.

## Naming Conventions

**Variables**, **methods** and **functions** should be snake_case:

```
def cool_function(arg):
    cool_new_variable = arg * 2
```

Module names snake_case.

```
import module_with_longname
```


**Classes** are **CamelCase**

``` 
    class TrashyArmadillo():
        class stuff...
```
    

## Maximum line length
Limit all lines to a maximum of 80 characters.
This makes our code more readable...except when it doesn't.

Use common sense. If there's no logical place to break the the line,
let it go. 

When you decide to break lines, the convention is to wrap them in parentheses. See the example below...

## Binary Operators
There should be a space before and after operators on one line.
exception: named arguments
example:

```
def function(agr1=None, arg2=None):
    return stuff
```

Multi-line: Operators should be used after line breaks. 
Example:

```
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)
```

## Blank lines
Surround top-level function and class definitions with two blank lines.
Method definitions inside a class are surrounded by a single blank line.

## Comments
Comments that contradict the code are worse than no comments. Always make a priority of keeping the comments up-to-date when the code changes!

Comments should be complete sentences. If a comment is a phrase or sentence, its first word should be capitalized, unless it is an identifier that begins with a lower case letter (never alter the case of identifiers!).

Sometimes comments get in the way of otherwise self-documenting code:

```
#this function adds two numbers.
def add_two_numbers(num1, num2):
    """this function adds two numbers"""  
        return num1 + num2
```

Good comments express the intent of the code and/or provide context.

If the code is clear, don't clutter it.

But when things get tricky, please, please, please, clarify.

## Docstrings
Docstrings should be written with double quotes. 
Quotes are on their own lines.
Write docstrings for all public modules, functions, classes, and methods. Docstrings are not necessary for non-public methods, but you should have a comment that describes what the method does. 
This comment should appear after the def line.

Example Doctstrings:
```
"""
purpose: creates a new order for a customer
author: Casey Dailey
args: (integer) customer_id
returns: (integer) id of order created
"""    
```

If a method calls on several others, please list those.

```
"""
purpose: allow user to add a product to an open order
author: Casey Dailey
args: n/a
returns: n/a
helpers:
    ---------------
    get_active_customer
    get_customer_open_order
    create_order
    read_inventory
    add_product_to_customer_order
    ---------------
"""
```

If a method returns a data structure that may need some explanation, 
please include an example.

```
   """
    purpose: 
    author: Aaron Barfoot
    args: customer_id -- (integer) Id of customer whose payment types we need to list
    returns: (list of tuples) 
        ex: [(2, 'visa', 1234567890123456, 1)] 
        where the above values represent:
        [(payment_type_id (integer), payment_type_name (string), account_number (integer), customer_id (integer))] 
    """
```

## Imports
Imports should usually be on separate lines, e.g.:

```
Yes: import os
     import sys

No:  import sys, os
```

It's okay to say this though:

```
from subprocess import Popen, PIPE
```

Imports are always put at the top of the file, just after any module comments and docstrings, and before module globals and constants.

Imports should be grouped in the following order:
```
standard library imports
related third party imports
local application/library specific imports
You should put a blank line between each group of imports.
```

DO NOT 'import *'
This "pollutes the namespace".
Instead do one of these: 

everything:
```
import module 
```

get what you need:
```
from module import Class or method
```

call it what you want:
```
import super.deep.module_with_a_long_name as mod 

```

