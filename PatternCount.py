# Input:  Strings Pattern and Text
# Output: The number of times Pattern appears in Text
def PatternCount(Pattern, Text):
    count = 0 # output variable
    for i in range(len(Text)-len(Pattern)+1):
        currentPattern = Text[i:i+len(Pattern)]
        if currentPattern == Pattern:
            count = count+1
    return count
