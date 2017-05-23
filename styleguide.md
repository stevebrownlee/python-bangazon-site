# Style Guide for Educated Camels
###### by James Tonkin

## Indentation
Use 4 spaces per indentation level.

## Maximum line length
Limit all lines to a maximum of 79 characters.

For flowing long blocks of text with fewer structural restrictions (docstrings or comments), the line length should be limited to 72 characters.

## Binary Operators
There should be a space before and after operators on one line.

Multi-line: Operators should be used after line breaks. Example:

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

## Docstrings
Docstrings should be written with double quotes. Quotes are on their own lines.Write docstrings for all public modules, functions, classes, and methods. Docstrings are not necessary for non-public methods, but you should have a comment that describes what the method does. This comment should appear after the def line.

Example Doctstrings:
```
"""
purpose: creates a new order for a customer
author: James Tonkin
args: (integer) customer_id
returns: (integer) id of order created
"""    
```
```
"""
purpose: allow user to add a product to an open order
author: James Tonkin
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

standard library imports
related third party imports
local application/library specific imports
You should put a blank line between each group of imports.
