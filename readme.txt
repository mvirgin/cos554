A program to calculate all possible sums that add to n given a list D of possible
addends. For COS 554 hw1

By Matthew Virgin (matthew.virgin@maine.edu)

25 September 2023
Public Domain

Manifest:
- readme.txt: this file
- hw1.py: file containing all code to complete programming part of hw1
- hw1testing.py: nearly identical to hw1.py, with added code to measure runtime
                    and memory usage
- cos554mvirginhw1.pdf - write-up for answering questions 8 and 9
- in101.txt: sample input to be used with either of the above .py
- out101.txt: sample output corresponding to tst1.txt
- in102.txt: sample input for illegal / strange cases
- out102.txt: output corresponding to in102.txt
- in103.txt: large numbers and odd numbers
- out103.txt: output corresponding to in103.txt
- in104.txt: negatives and large strings
- out104.txt: output corresponding to in104.txt
- in105.txt: samples of the worst cases
- out105.txt: output corresponding to in105.txt
- tst1.txt: large input used to examine runtime with hw1testing.py
- testout1.txt: output corresponding to tst1.txt

Running:
- input python hw1.py into the command line and then provide n and the elements
   of D like so: 5 1 2 3 4 5
- python hw1.py < in101.txt > out.txt should produce the same file as out101.txt

Known bugs and limitations:
- high sums with large lists, specifically lists whose elements are 1 thru n,
    can take a long time to run, the program may time out.

Credits:
Tristan Zippert, Connor Lariviere - helped me to better understand what the questions
    were asking and gave me confidence I was moving in the right direction

https://www.geeksforgeeks.org/combinational-sum/# - helped me understand the 
    algorithm. My code is a similar, simplified version that better suits the 
    assignment.

