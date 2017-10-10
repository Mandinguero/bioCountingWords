
pattern = "ACTAT"
Text = "ACAACTATGCATACTATCGGGAACTATCCT"
count = 0
name = raw_input("Enter your name:")

def patternCount():
    print "Counting patterns in a string.."
    i = 0
    if Text[i:i+len(pattern)] == pattern:
        count = count + 1
        print "Found a match!"
    else:
        print "Not a match in " + pattern[i:len(pattern)]

    if len(name) == 4:
        return('Must not enter ' + name + '!')
    elif len(pattern) < len(Text):
        return (pattern + ' is shorter than ' + Text)
    else:
        return "Ahooy!"

print patternCount()

# for loop with range()
hobbies = []
for i in range(2):
    hobby = raw_input("Enter your hobby " + str(i) + ":")
    hobbies.append(hobby)
print hobbies

# print str chars
print "now printing the contents of Text"
for c in Text:
    print c,
print

for char in Text:
    if char.lower() == 'a':
        print 'a',
    else:
        print char,
print

# looping through a list
lista = [4, 7, 12, 24, 36]
print "This list contains: "
for num in lista:
    print num,
print

# looping through a dictionary
d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}
for key in d:
    if d[key] == 'apple':
        print d[key] + "s are delicious!"
    else:
        print "don't bother with " + d[key]
print

# looping with enumerate
choices = ['pizza', 'pasta', 'salad', 'nachos']
print "Your choices are: "
for index, item in enumerate(choices):
    if index == 1:
        print index+1, item + ' (best item!)'
    else:
        print index + 1, item
print

# looping through multiple lists
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]
for a, b in zip(list_a, list_b):
    if a >= b:
        print a
    else:
        print b
print

# Using FOR/ELSE
# Else is executed only if FOR ends normally
# Else not executed if for ends with a 'break'
print "Pattern is: " + pattern
print "Text is: " + Text
for i in range(len(Text)-len(pattern)+1):
    currentPiece = Text[i:(i+len(pattern))]
    # print "Looking at: " + currentPiece
    if pattern == currentPiece:
        count = count +1
        print "found pattern " + pattern + " at position " + str(i) +"!"

    elif currentPiece == 'AAAAA':
        print "found five A\'s !!!"
        break
else:
    print "Found " + str(count) + " occurrences of pattern " + pattern
print


## Function to find a pattern in a string
def PatternCount(Pattern, Text):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        currentPattern = Text[i:i+len(Pattern)]
        if currentPattern == Pattern:
            count = count+1
    return count

print PatternCount(pattern, Text)
print


## Functions for tax and tip
def tax(bill):
    """Adds 8% tax to a rest bill"""
    bill *= 1.08
    print "With tax: %.2f" % bill
    return bill

def tip(bill):
    """Adds 15% tip to a rest bill"""
    bill *= 1.15
    print "With tip: %.2f" % bill
    return bill

while True:
    try:
        meal_cost = float(raw_input("Enter the meal cost: "))
    except ValueError:
        print("Not a valid number!")
        continue
    else:
        break
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)



def cube(number):
    return number**3

def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False

print by_three(27)





