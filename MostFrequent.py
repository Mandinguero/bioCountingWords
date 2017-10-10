## Frequent Words Problem: Find the most frequent k-mers in a string
#     Input: A string Text and an integer k.
#     Output: All most frequent k-mers in Text.

import Replication

Text = "ACAACTATGCATACTATCGGGAACTATCCT"
MaxPatternSize = len(Text)

## Read size of pattern
while True:
    try:
        msg = "Enter Pattern Size [2-" + str(MaxPatternSize) +"]: "
        PatternSize = int(raw_input(msg))
    except ValueError:
        print("Not a valid number! Please enter again")
        continue
    else:
        break

print "Searching for patterns of size " + str(PatternSize)

PatternDict = {}
print "Current Dictionary: " + str(PatternDict.values())

for i in range(len(Text)-PatternSize+1):
    Pattern = Text[i:i+PatternSize]
    # print "Pattern is " + Pattern
    # Search dictionary for pattern.
    print PatternDict.get(Pattern)
    # If not found, add entry to dictionary.
    # If found, increment the number of occurrences.


