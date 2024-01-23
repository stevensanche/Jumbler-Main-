# Jumbler HOWTO

## Preface: HOWTO documents and Markdown format

This HOWTO document provides step-by-step directions for completing
a programming project in CS 210  (aka CS 161 in Oregon colleges and
universities). The document is written in a notation called Markdown.
Although the Markdown notation is somewhat readable, it is designed
to be read with an application interprets and formats the Markdown.
The text editors in PyCharm and VSCode are among applications with
Markdown "preview" support. There are many others.

If you are using a Markdown-aware application in preview mode, this
document should look like this:

![A formatted Markdown document](img/HOWTO-formatted.png)

and not like this:

![Markdown document source](img/HOWTO-src.png)

## Objectives

This is a "getting started" project that introduces a few key ideas:

* Think first, then code. We start by understanding the problem,
  and *then* we develop a strategy for solving the problem, and only
  *then* we start writing Python code to solve the problem.  
  Sometimes we might write tiny snippets of Python code to check the
  feasibility of an idea, but the real programming doesn't start
  until we have a solution strategy mapped out.

* Code a little, test a little. Even when we have the whole
  solution strategy mapped out, we don't write the whole program at
  once. We write a little bit, test it, and then move on. The
  order in which we write parts of the program is often determined
  by a good order for testing.

* Code for humans, not just for computers. Our code must be clear
  and understandable. It not only needs to be correct, but it
  needs to be _clearly_ correct, i.e., a programmer reading our code
  should understand the approach and be able to assess its
  correctness. Beautiful, clear code tends to be recycled into new
  programs. Tangled, obscure, unnecessarily complicated code has a
  short path to the trash heap.

In addition it introduces two common patterns for computational
problem solving:

* Scanning a collection. In our case, the "collection" will be a
  list of dictionary words. We will read each word, check it,
  and then move on to the next.

* Using canonical forms. A "canonical" form is a unique
  representative of a collection of possible forms. Often, if we
  want to know whether some object A and another object B belong to
  the same group of items, we can transform A and B each to a
  canonical form that represents the whole group. They belong to
  the same group if they have the same canonical representation. In
  our case, the "group of items" will be "words that can be formed
  from a given set of letters, in some order". The canonical
  form will be a list of letters in alphabetical order.

  "Canonical form" is also called "normal form", and
  "canonicalization" is also called "normalization". Since
  "normalize" is easier to pronounce than "canonicalize", and since
  it is very hard to remember things we cannot pronounce, we will
  prefer to call it "normalization".

## Solving a Jumble

"The Daily Jumble" is an anagram puzzle distributed
by Tribune Content Agency, LLC, and published in a
number of
newspapers. It is often titled
"That scrambled word game."  
Here is an example, copyright
Tribune Content Agency and used here
under fair use provisions of U.S.
Copyright Law for educational purposes:

![Daily Jumble (example). (c) 2022 Tribune Content Agency](img/jumble.png)

You will construct a program to solve one of the anagrams in a Jumble.
For example, the first anagram in the puzzle illustrated
above is _KAWEA_. You will find that the letters can be
rearranged to make _AWAKE_.

## Strategy

We need a good problem-solving strategy before
we even think about how to express it as a
Python program. But while we don't want to think
too soon about the details of the Python code, it
helps to have some idea of the tools we have to
work with. In particular, it will be helpful to
know that

* We can read a whole dictionary of some tens of thousands of words
  in under a second. So, if we know what we are looking for, it is
  quite practical for us to search the whole dictionary to find it.
* We can treat the string of characters in a word as a list that can
  be manipulated in various ways. In particular, we can ask whether
  two strings or lists of characters are the same  (so if we were
  looking for a particular word in the dictionary, we could check
  each word in the dictionary to see if it matched).

### The catch

So we can search the whole dictionary, but there's a problem:  We
aren't looking for a word that is the same as the anagram. We're
searching for a word that the anagram can be rearranged into. For
example, we wouldn't find _KAWEA_ in the dictionary; we want to find
_AWAKE_ because the letters in _KAWEA_ can be reordered to make
_AWAKE_. But if we knew how to rearrange them properly, we wouldn't
even need to look in the dictionary!

### The trick

There is a trick that we can use:  If we rearrange the letters in
the anagram in a predictable way, and rearrange the letters in a
dictionary in the same predictable way, then we can ask whether the
*rearranged* versions are the same. For example, we can put the
letters into alphabetical order by _sorting_ them. Try these lines
in Python, using the IDLE Python shell or another Python console.

```python
sorted("KAWEA")
sorted("AWAKE")
```

If you execute those two lines in IDLE, you should see something
like this:

![Sorted strings in Python](img/sorted-strings.png)

It looks a little strange ... maybe we expected the output of
`sorted("KAWEA")` to be `"AAEKW"`, but instead of a string of
text we got a list of characters, `['A', 'A', 'E', 'K', 'W']`.
But the important thing is that when we sorted `"AWAKE"` we got
the same list `['A', 'A', 'E', 'K', 'W']`. Good enough!  We can
compare these lists and determine whether they are equal:

```python
sorted("KAWEA") == sorted("AWAKE")
```

Try it in IDLE. You should see this:

![Checking equality of sorted strings](img/sorted-compare.png)

So now we have a good strategy:

* Sort the letters in anagram.
* Compare to _a sorted version of_ each word in the dictionary.
* If they are equal, we will produce the original, unsorted version
  of the dictionary word.

Easy peasy!  But still, we won't do it all at once. We always,
always, always want to build programs little bit by little bit,
testing as we go.

### A problem solving pattern

The tactic we are using here has a name: _normalization_. 
When we want to compare two things without regard to some
details that we deem insignificant, we can _normalize_ them
before comparing.  If such a _normal form_ is unique for a whole set 
of elements that we want to consider equivalent, we call that
unique representative _canonical_.   

You do not need to memorize
these terms, although you will encounter them again as you progress 
in your development as a programmer.  You should, however, be 
accumulating and generalizing problem solving patterns that you can 
apply to many problems.  This is one such pattern:  
_To compare things while 
ignoring some details, first convert them to a normal form_.  


## Breaking it down

It helps to make a list of small pieces of the problem. These will
be steps in building our application, but we don't necessarily know
yet what order we will take those steps in. (We are not talking
about the order in which the steps will be executed, but the rather
the order in which we, human programmers, will develop those steps.)

Here are some possible small parts of our puzzle solving program:

* We will need to obtain the anagram word. We might prompt the user
  to type it in.
* We will need to get the normalized (sorted) version of the anagram.
* We will need to read the dictionary, line by line.
* We will need to get the normalized (sorted) version of each word 
  in the dictionary.
* We will need to compare the normalized anagram with the normalized
  dictionary word.
* We will need to output the original dictionary word if the normalized
  versions match.

Note again that these steps are not in any particular order. In what
order should we develop them? Our mantra is:  Code a little, test a
little. What is the smallest part that we could meaningfully test, to
gain some confidence that we are on the right track? We've already
tried sorting a string, and comparing the resulting list of
characters to the result of sorting another string. Getting the
input puzzle also seems simple enough that it isn't clear what we
could test.

What about reading each word from the dictionary? That seems like a
good place to start.

## Step 0:  Start with a good header

Create a new program file. Call it `jumbler.py`. The first thing
we will add to that file is not for the computer, but rather for our
fellow human beings, especially other programmers. We start with a
_docstring comment_ that describes the file. Most software
development organizations, whether in industry or research, have
some standard content and format for such header comments. The
standard we will use looks like this:

```python
"""jumbler:  List dictionary words that match an anagram.
2022-06-25 by Your Name Here

Credits: 
A. Nother Student, And Another:  Sketched pseudocode together
Our Friend:  Helped debug
"""
```

Initially the "Credits" section is empty. This is where you make a
note of other students (not instructors, teaching assistants, or
learning assistants) who helped you in some way. Crediting your
collaborators and helpers is crucial!   See the course policy on
collaboration and credit to be sure you are doing this correctly and
are not in danger of committing academic dishonesty.

Next, let's write a very simple program that just reads each entry
of the dictionary. If we look at the file `dict.txt`, we can see
that each line is a single word. We can use the Python `open`
function to prepare the file for reading.

```python
dict_file = open("dict.txt")
```

`open` is a built-in Python function. A function takes in zero or more
arguments and produces zero or more results. In this case the input is
a text string, `"dict.txt"`. The result is a file object. But what if
the argument was not the name of a file in the current folder? Try this
in the
Python shell:

```python
dict_file = open("words.txt")
```

We don't have a file called "words.txt" in the current folder, so we
should
get an error message.

Note that in addition to file `dict.txt`, we have a much shorter
file `shortdict.txt`. If we need to debug our program (and we most
likely will), it may be much easier to debug with a small word list
than a very large word list. So let's make the choice between the
full dictionary and the shorter version very obvious and easy to
change.

```python
DICT = "shortdict.txt"    # Short version for testing & debugging
# DICT = "dict.txt"       # Full dictionary word list

dict_file = open(DICT, "r")
```

In the code above, we say that the second assignment to `DICT` is
_commented out_. Now it is very easy to switch between short and 
full versions.  

## Global constants 

Note the convention of using ALL CAPS to indicate
that some variable name like `DICT` is a global 
constant.  This means a value that is set in one place,
and may be used (but not changed) elsewhere in the program code.

Global variables should be used very sparingly, because they can 
make programs more difficult to read, debug, and modify.  They 
are not a good way to communicate values between functions.  When we 
do use global variables, they are usually either well-known 
constants like _pi_ (π) or _e_, or at least variables that are 
"constant" in the sense that we will not alter them during program 
execution. 

Global constant declarations should be placed as early in the
code as possible (but after the header docstring), where they are 
easy to find. They should
generally be accompanied by a comment explaining their purpose. 

We have not capitalized `dict_file` in the same way, and we will not 
leave it here for long.  We will instead put it close to where it is 
used, in a more limited scope.

### We write for other programmers

Programs are written for other programmers, not just for the computer. 
Readability, understandability, and 
maintainability are key to many
of our programming decisions.   Many software development 
organizations, including all the big companies you are familiar with,
have well-established processes of _code review_ in which the code 
written by one programmer must be read and approved by others. 
Sometimes code review finds bugs (errors) to be corrected, but the 
most common reason for revising programs after code review is to 
make it clearer and easier to maintain. 

## Scanning the file

In Python the easiest way to read each line of text from a file is
with a `for` loop, like this:

```python
dict_file = open(DICT, "r")
for line in dict_file:
    pass
```
Although technically the "head" of the loop is 
`for line in dict_file:`, we 
think of the line with `open` as almost part of the loop.  
There is no point in opening the file unless we intend to read the 
file, and it is not possible to loop through the file without 
opening it.    We therefore want to keep these lines of code 
together, rather than placing the `open` function earlier in the 
program. 

The indented line is the _body_ of the loop. Initially I have
used `pass` in the body as a placeholder. We can replace `pass` with one
or more lines that
do whatever we want with one line of text from the file. Let's print
each line.

```python
dict_file = open(DICT, "r")
for line in DICT_FILE:
    print(line)
```

The value of having a short word list should be apparent now. We can
look at the output and compare it to the content of `shortdict.txt`.

![Our first attempt at scanning and printing the word list](img/scan-file-1.png)

Something isn't right. We are reading and printing each line, but we
seem to be getting a blank line between each line of text
from `shortdict.txt`. Why is that?

A text file is really one long sequence of characters. Some of those
characters are visible, like "a" and "p". Some are "control characters",
including a character called "newline" that indicates the end of one
line of text and the beginning of another.

![Our file `shortdict.txt` is really a sequence of characters, including newlines](img/text-file-format.png)

When we read a whole line of text in our loop, the string we get
includes the newline character:

![First line from `shortdict.txt`](img/text-file-line.png)

The extra blank lines are because of those newline characters. They also
indicate a problem we will have if we try to compare this set of
characters
to an anagram:  Our anagram does not contain a newline character. We
need
to discard it.

Fortunately Python provides a built-in tool for discarding control
characters at the beginning and end of a string. Try this in the Python
shell:

```python
("  \n word \n").strip()
```

In this example we have indicated the newline characters 
with `\n`.  We can also embed them literally in a triple-quoted 
Python string, like this:

```python
"""       

      word
    
""".strip()
```

Either way we write the string with newline characters, you can see 
that the result is just the word in the 
middle, with the
leading spaces and newline characters removed. 

### Calling _methods_ vs calling _functions_

The way we call `strip()` is a little confusing. Why is it
`" something ".strip()` and not `strip("something")`? This is because
`strip` is a special kind of function called a "method". We can't apply
it to every kind of data, but only to strings. In fact, we call it a
"method" of the string (`str`) data type. When we type `"xxx".strip()`,
Python determines that "xxx" is a string, and it looks inside the string
"class" to find a "method" called "strip". A different type of data
might
have a completely different method called "strip", or none at all. If
we try to call "strip" on an integer, for example, Python will complain
that
the `int` type doesn't have a "strip" method. Try this in the Python
shell:

```python
(42).strip()
```

You should get an error message that looks something like this:

```commandline
AttributeError: 'int' object has no attribute 'strip'
```

Now that we know we need to "strip" the whitespace from each line of
the dictionary file, let's modify our loop to print each word with just
the parts we want to keep:

```python
dict_file = open(DICT, "r")
for line in dict_file:
    word = line.strip()
    print(word)
```

Now we should get what we expected:

![Second attempt at scanning and printing `shortdict.txt`](img/scan-file-2.png)

## Check for Matches

Now that we can scan a dictionary word list, it's time to add
checking logic. But remember:  Code a little, test a little.   
While our final strategy is to compare a _normalized_ (and in fact 
_canonical_) version of the
anagram to a _canonical_ version of the dictionary word, we can
start with a simpler version:  We'll check for an exact match. For
example, if we look for the word "gamma", our program should print
"gamma", but if we look for "nosuchword", our program
should print nothing.

We could "hard code" a single word to look for, but finding a single 
word would not give us much confidence.  It will be better if we 
make the search a _function_ that can be called to find a variety of
different words.

```python
def find(anagram: str):
  """Print words in DICT that match word."""
  for line in dict_file:
        word = line.strip()
        if word == anagram:
            print(word)
```

### Test it! 

We don't have a complete program yet, but we can already start
writing test cases.  We'll use a facility called "doctest" to 
include basic test cases right in the docstring comment for
the function.  A line that starts with ">>>" will indicate an
example that can serve as a test case. 

```python
def find(anagram: str):
  """Print words in DICT that match anagram.
  
  >>> find("gamma")
  gamma
  
  >>> find("nosuchword")
  
  """
  dict_file = open(DICT, "r")
  for line in dict_file:
        word = line.strip()
        if word == anagram:
            print(word)
```

The `doctest` module is described at
[https://docs.python.org/3/library/doctest.html](https://docs.python.org/3/library/doctest.html)
It prescribes a way to invoke doctests at the end of the source file. 
We will follow that example, adding a print statement that lets us 
know the tests have been run. 

```python
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("Doctests complete!")

```

Try putting these parts together, and execute the file in Idle. We 
should see something like this: 

```commandline
===== RESTART: /Users/michal/Dropbox/22F-210/projects/01-Jumbler/jumbler.py ====
Doctests complete!
```

How do we know that these test cases are actually testing the 
functionality of our code?  Let's add test cases that will should 
fail for now, but pass when our program is complete.  

```python
  """Print words in DICT that match anagram.
  
  >>> find("gamma")
  gamma
  
  >>> find("nosuchword")

  >>> find("MAGAM")
  gamma

  >>> find("KAWEA")
  awake
  
  """
```

The first of these two test cases ("MAGAM") should pass whether we 
use the short dictionary or the full word list, if our program is 
otherwise complete.  The second should only pass if we are using the 
full word list.  For now neither of them passes: 

```commandline
===== RESTART: /Users/michal/Dropbox/22F-210/projects/01-Jumbler/jumbler.py ====
**********************************************************************
File "/Users/michal/Dropbox/22F-210/projects/01-Jumbler/jumbler.py", line 19, in __main__.find
Failed example:
    find("MAGAM")
Expected:
    gamma
Got nothing
**********************************************************************
File "/Users/michal/Dropbox/22F-210/projects/01-Jumbler/jumbler.py", line 22, in __main__.find
Failed example:
    find("KAWEA")
Expected:
    awake
Got nothing
**********************************************************************
1 items had failures:
   2 of   4 in __main__.find
***Test Failed*** 2 failures.
Doctests complete!
```

## Test driven development (TDD)

We could have run these test cases _once_ more easily by typing a 
command for each test case in the Idle 
shell, Python console, or at the command line of our operating system.
We have gone to the extra trouble of including them as doctests in
the function header because we want to execute them again and again
as we develop the program.   The purpose of test automation, with 
doctests or any of several other testing frameworks, is to automate 
this process of repeating the testing each time we modify the 
program code.  

One common practice is to write test cases _before_ we write the 
code that will make those test cases pass.  That is what we have 
done with the two new test cases:  "magam" and "KAWEA" will not be 
found yet, but they should let us find "gamma" and "awake" after our 
next steps.   This is called "test driven development", often 
abbreviated TDD.  


## Normalize!

It's time for us to normalize the anagram and the dictionary word, 
converting each to a canonical form, so that we can compare them.
We don't want to write (almost) the
same code twice, so this is a good candidate for defining a _function_.
We will call the function `normalize`, because that is easier to
pronounce than `canonicalize`. The input argument for `normalize`
will be a string (type `str`), and the result of `normalize` will
be a list of one-character strings, so we will write the _function 
header_ this way:

```python
def normalize(word: str) -> list[str]:
```

Note that the result type uses square braces. We pronounce
`list[str]` as "list of strings".

### Results vs effects

Do not confuse the _result_ of a function with an _effect_.  
Earlier we wrote a function _find_ that had the _effect_ of printing 
words it found in a file.  That function had no _result_, or to be 
more precise its result was always `None`.  Our new function 
`normalize` will have no _effect_, but will instead return a 
_result_, which will be a list of strings.  Most functions we write 
will be like this, returning a result, because a function that 
returns a result with no side effects is generally more versatile,
i.e., it is generally easier to use them in multiple ways and places. 

### Normalizing case

We have already noted that we will need to sort the letters in a 
word so that we can ignore the difference between "magam" and 
"gamma". But that's not quite enough --- we also need to ignore the 
difference between lower case and capital letters.  

We could 
normalize case by making all the letters lower case, or by making 
them all upper case; it really doesn't matter as long as we are 
consistent. Fortunately Python provides built-in methods for both. 
Like the method `strip` that we used before, `upper` and `lower` are 
_methods_ of the `str` data type.  

```commandline
>>> "aMixedUpMess".upper()
'AMIXEDUPMESS'
```

### Test cases for `normalize`

Again following the methodology of test driven development (TDD), we 
will write some test cases for `normalize` before we write the code 
to implement it.  Rather than specify exactly what the resulting 
lists should look like, let's specify the one thing we really care 
about, which is that it will return _equal_ results for strings that 
are anagrams of each other. 
```python
def normalize(word: str) -> list[str]:
    """Returns a list of characters that is canonical for anagrams.
    
    >>> normalize("gamma") == normalize("magam")
    True
    
    >>> normalize("MAGAM") == normalize("gamma")
    True
    
    >>> normalize("KAWEA") == normalize("awake")
    True
    
    >>> normalize("KAWEA") == normalize("gamma")
    False
    """
```

I will leave implementation of `normalize` to you.  It should have 
the following steps:

- Get an upper or lower case version of word, using the method 
  `upper` or the method `lower`.  Store that in a local variable. 
- Use the `sorted` function to obtain a list of the letters in 
  alphabetical order. 
- Return that list

When you have completed this (and perhaps after some debugging --- 
that is normal!) the result of running your program should look like 
this: 

```commandline
===== RESTART: /Users/michal/Dropbox/22F-210/projects/01-Jumbler/jumbler.py ====
**********************************************************************
File "/Users/michal/Dropbox/22F-210/projects/01-Jumbler/jumbler.py", line 19, in __main__.find
Failed example:
    find("MAGAM")
Expected:
    gamma
Got nothing
**********************************************************************
File "/Users/michal/Dropbox/22F-210/projects/01-Jumbler/jumbler.py", line 22, in __main__.find
Failed example:
    find("KAWEA")
Expected:
    awake
Got nothing
**********************************************************************
1 items had failures:
   2 of   4 in __main__.find
***Test Failed*** 2 failures.
Doctests complete!
```

Note that we are still failing some test cases in `find`.  We will 
fix those next. 

## Finding an anagram

Now that we can normalize strings, we can make use of `normalize` in 
our function _find_.  The line that we need to change is 

```python
        if word == anagram:
```

Instead of comparing them directly, we can compare a normalized 
version of each.  Try that.  After you change that line, execute the 
module again.  Initially you should still have one test failure: 

```commandline
===== RESTART: /Users/michal/Dropbox/22F-210/projects/01-Jumbler/jumbler.py ====
**********************************************************************
File "/Users/michal/Dropbox/22F-210/projects/01-Jumbler/jumbler.py", line 22, in __main__.find
Failed example:
    find("KAWEA")
Expected:
    awake
Got nothing
**********************************************************************
1 items had failures:
   1 of   4 in __main__.find
***Test Failed*** 1 failures.
Doctests complete!
```

This is because we are still using `shortdict.txt` rather than the 
complete word list, `dict.txt`.   Comment out the assignment of 
`shortdict.txt` to `DICT`, and uncomment the assignment of `dict.
txt`, so that your program will search the whole word list.   

```python
# DICT = "shortdict.txt"    # Short version for testing & debugging
DICT = "dict.txt"       # Full dictionary word list
```

Execute again.  What happens?  You may find that you still have a 
test case failure, but not because you failed to find a word ... 
rather it is because you found another anagram for "magam". It would 
be nice to replace it with a test case that works for both 
`shortdict.txt` and `dict.txt`.  Anagrams of "beta" don't help ... 
they turn up "abet", "bate", and "beat" in addition to "beta".  
Anagrams of "omega" and "alpha" seem to be unique, so our final set 
of doctests for `find` can be 

```python
  """Print words in DICT that match anagram.
  
  >>> find("AgEmo")
  omega
  
  >>> find("nosuchword")

  >>> find("alpha")
  alpha

  >>> find("KAWEA")
  awake
  
  """
```

## Interaction

We now essentially have a solution to the problem we set out to 
solve, but it is not usable:  Our program just runs a set of test 
cases.  One of the items on our initial list of things we would need 
to do was to obtain an anagram to solve.  That's easy in Python, 
with a line like this: 

```python
anagram = input("Anagram to find> ")
```
But where should this go?  Let's create a "main" function for the 
overall program: 

```python
def main(): 
    anagram = input("Anagram to find> ")
    find(anagram)
```
In addition we will comment out the testing and add a call to `main` 
at the end of our source file: 

```python
if __name__ == "__main__":
    main()
    # import doctest
    # doctest.testmod()
    # print("Doctests complete!")
```

Now we have a program that prompts for an anagram, and prints the 
matching words.  We can rerun it in the Idle shell by 
typing `main()`.  

Let's try it for each of the jumbles from the Daily Jumble example 
above: 

```commandline
===== RESTART: /Users/michal/Dropbox/22F-210/projects/01-Jumbler/jumbler.py ====
Anagram to find> AKEAW
awake

main()
Anagram to find> CHIRB
birch

main()
Anagram to find> PINTAC
catnip

main()
Anagram to find> NSYAWK
swanky
```

Find another Jumble puzzle online and try it on that, too.  

## A little bit faster

At this point you have a working anagram solver.  You could turn it 
in as it stands.  If you have time, though, you can make it slightly 
more efficient.  When we changed one line to compare a normalized
version of the anagram to a normalized version of a word from the 
word list, we wrote it so that the anagram is normalized again and 
again, once for each word of the word list.  The result of 
normalizing the anagram could be done just once, before the loop 
that searches the file, if we save the result in a variable.  You 
will hardly notice the difference, because `jumbler` already 
executes in a fraction of a second, and we will not require you to 
make this improvement.  However, an experienced software developer 
would almost certainly make it, so why not get in the habit of 
making your code faster when you can do so without making it less 
readable.   














