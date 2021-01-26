# Crossword Assistant


## Overview
The crossword assistant is essentially a regular expression generator to help you with your fill, or to help you solve crosswords if you want. It has a command-line interface with a simple syntax. If you have a five letter word whose second letter is 'g' and fifth is 'h', you can enter:

```
py cw_main.py 5 2g 5h
```

and you will receive a list of matching words. The basic syntax (which is unordered, by the way) is:

```
[length] [#a] ... [#z]
```

You can enclose expressions in parentheses, enabling you to match or exclude groups of letters. For example, suppose we suspect the above word start with a vowel.

```
5 "1([aeiou])" 2g 5h
```

Remember to quote or escape expressions, or else the shell may try to evaluate parts of your expression before sending it to the program. A common example is the 'or' operator, which the shell will read as a pipe. You can look for a 4-letter word that ends with 's' and starts with either 'a' or 'b'.

```
4s "1(a|b)" 4
```

This example also illustrates how the arguments are unordered.

### Upcoming Changes
This was an afternoon project, and I'm not planning on expanding it much. Some interesting ideas, though:

- Make a crossword generator.
- More word lists
- If a query returns nothing, evaluate which letter combination is hampering results. You might count the number of results when each argument is removed, or when the size of the word is changed.



---
Charlie Gallagher, 2021
