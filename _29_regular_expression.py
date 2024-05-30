# Regular expression in Python

# Regular expressions, or regex for short are a powerful tool for working with string and text data in python. They allow you to match and manipulate strings based on patterns, making it easy to perform complex string operations with just a few lines of code.

'''
Here is a list of common metacharacters and their meanings:

. (Dot)

Matches any character except a newline.
E.g.:
import re
re.search(r".", "abc")  # Matches 'a'
^ (Caret)

Matches the start of a string.
E.g.:
re.search(r"^a", "abc")  # Matches 'a' at the start
$ (Dollar)

Matches the end of a string.
E.g.:
re.search(r"c$", "abc")  # Matches 'c' at the end
* (Asterisk)

Matches 0 or more repetitions of the preceding element.
E.g.:
re.search(r"ab*", "abbb")  # Matches 'abbb'
+ (Plus)

Matches 1 or more repetitions of the preceding element.
E.g.:
re.search(r"ab+", "abbb")  # Matches 'abbb'
? (Question Mark)

Matches 0 or 1 repetition of the preceding element (makes it optional).
E.g.:
re.search(r"ab?", "a")  # Matches 'a'
{} (Braces)

Matches a specified number of repetitions of the preceding element.
E.g.:
re.search(r"ab{2}", "abb")  # Matches 'abb'
re.search(r"ab{2,3}", "abbb")  # Matches 'abbb'
[] (Square Brackets)

Matches any one of the characters inside the brackets.
E.g.:
re.search(r"[abc]", "a")  # Matches 'a'
re.search(r"[a-z]", "m")  # Matches 'm'
| (Pipe)

Acts as an OR operator.
E.g.:
re.search(r"a|b", "a")  # Matches 'a'
re.search(r"a|b", "b")  # Matches 'b'
() (Parentheses)

Groups patterns and captures the matched text.
E.g.:
re.search(r"(abc)", "abc")  # Matches 'abc'
\ (Backslash)

Escapes a metacharacter or denotes a special sequence.
E.g.:
re.search(r"\.", "a.b")  # Matches '.'
re.search(r"\d", "123")  # Matches '1'
Special Sequences:

\d: Matches any digit (equivalent to [0-9]).
\D: Matches any non-digit.
\s: Matches any whitespace character.
\S: Matches any non-whitespace character.
\w: Matches any alphanumeric character (equivalent to [a-zA-Z0-9_]).
\W: Matches any non-alphanumeric character.
Examples:

E.g.:
re.search(r"\d+", "123abc")  # Matches '123'
re.search(r"\w+", "abc123")  # Matches 'abc123'
Anchors:

\b: Matches a word boundary.
\B: Matches a non-word boundary.
Examples:

E.g.:
re.search(r"\bword\b", "word boundary")  # Matches 'word'
re.search(r"\Bword\B", "swordsmanship")  # Matches 'word' in 'swordsmanship'
'''

import re

word = "Namaste everyone. This is Ram. Aaba bhat kham. Ani sutna jam."

pattern = r"[A-Za-z]am"

# match = re.search(pattern,word)
# print(match)

matches = re.finditer(pattern,word)
for corr in matches:
    print(corr)