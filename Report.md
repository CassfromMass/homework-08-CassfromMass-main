# Report


1. What is the difference between a file and a directory?

Files contain information/content and directories provide structure that organizes information/content.

2. What is the difference between a relative and absolute path?

An absolute path begins its reference at the root directory. The relative path begins its reference with your current location.

1. What is the difference between a text file and a binary file?

A binary file is all 0s and 1s; meant to be read computers. A text file is Unicode or ASCII characters. It is plain text without formatting or decoration. It is meant to be read by humans.

2. When looking at program arguments, which is the first argument (sys.argv[0]) in the list for all python files?

The name of the script. The name of the script (or file name) is rarely something that you're interested in unless you want to print the file name.

3. List three python exceptions or errors, and what their purpose. For example, a ValueError represents an error when a value has the right type but inappropriate value. You can find a list here: https://docs.python.org/3/library/exceptions.html. Ideally, pick ones you have seen before! 

SyntaxError triggers when there is a syntactical error in the code.
IndentationError triggers when a line of code is incorrected indented (does not trigger if incorrectly nested for your intention)
TypeError triggers when a return item is not the expected type (eg. '5' or 'five' instead of 5).

## Deeper Thinking

In this assignment, your capability to analyze and represent data greatly increased
because you are now able to handle files. Files hold the "state" of information (data)
in a computer, and because of them, we can save our state and return to a certain state between computer runs. 

However, for file types to make sense, there needs to be specifications. A specification
is an agreed upon format for how to represent data. For example, the .csv file format
is a specification for how to represent data in a comma separated value file. Many groups are formed to create specifications, and they are often open source. One  well known one is the [W3C](https://www.w3.org/), which creates specifications for the web with the [HTML](https://html.spec.whatwg.org/) standard being the most well known.

Task: Write a small paragraph (3-5 sentences) about how you think specifications are created, and why they are important. You can use the W3C and HTML as an example, or any other specification you find interesting. If you look at HTML bonus if you create small webpage in HTML to show off your knowledge! (You can upload the .html repo with your submission)
_________________________________________________
Specifications are created by teams at various levels of industry in order to make programs more readable, adaptable, and inter-operable with other programs. Living languages (including program languages) have stylistic differences unintentionally (or intentionally) develop by the people using the language. Creating an agreed upon list of "rules" allows different groups to communicate without being thwarted by their stylistic differences.

W3 writes the specifications for html language on which the internet is based. It is currently on the 5th version of specifications for the language - responding to changing needs and uses over time.



