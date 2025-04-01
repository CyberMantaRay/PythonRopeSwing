# Author @AndorLight


############################
###    SYNTAX & PRINT    ###
############################

def basics():
    letter_A = ord('A')
    fire_emoji = ord('🔥')
    print(f"{chr(letter_A)} → {letter_A}, {chr(fire_emoji)} → {fire_emoji}")
    print("{} → {:b}, {} → {:X}".format(
        letter_A, letter_A, fire_emoji, fire_emoji))
    print("%d → %s, %d → %s" %(letter_A, bin(letter_A), fire_emoji, hex(fire_emoji)))

    # Note: Text UTF-8 encoded by default
    # Summary: ord(), chr(), bin(), hex()

############################
###      DATA TYPES      ###            # Check for type: 
############################            #   • isinstance(ele, str)    • type(ele) == str

### CORE: bool, str, int, float

def strings():                          # A=65, Z=90, a=97, z=122
    quote = "When you base your expectations only on what you see, you blind yourself to the possibilities."
    print(len(quote))                   # Get length, e.g. 94
    print(quote[19:31])                 # Format: [start?:end?:step?]
    print(quote[:52])
    print(quote[-40:])                  # Reverse indexing
    print("Spirit World"[::-1])
    print(f'"{quote}" -Zaheer')         # Formatted string, :s (string) default
    print(f'Cabbage Corp. Loan: ${27500000:,.2f} | interest rate={.0387498:.3%}')


### COLLECTIONS: list, set, dict

def lists():                                        # Equiv. to arrays
    avatars = ["Wan", "Yangchen", "Kuruk", "Kyoshi", "Roku"]
    print("Arr length: %d" %(len(avatars)))
    print("1st avatar: %s" %(avatars[0]))           # Collections are 0 indexed
    avatars.append("Aang")
    avatars.append("Korra")
    avatars.append("Raava")
    avatars.pop()                                   # Removes last element unless index specified
    for ele in avatars:
        print(ele, end=" ")                         # end param. replaces def. newline w/ custom string, e.g. space
    
    # Think about our position in STDOUT after the above loop/print statements execute, i.e.
    # will our next print() start on the next line as usual?

def list_comprehensions():                          # arr = [expr. for item in iterable if condition == True]
    arr = [x for x in range(1,12) if x%2 == 0]                      # Acts as filter
    print(arr)
    arr = [x if x%3 == 0 else 'x' for x in range(1,16)]             # Acts as alt. value (if-else)
    print(arr)
    arr = [(x, y) for x in range(3) for y in range(7,9)]            # List of tuple coordinates
    print(arr)
    nested = [[1,2,3], [4,5], [6,7,8,9]]
    flattened = [num for sublist in nested for num in sublist]
    print(flattened)
    mult_table = [[x*y for y in range(1,7)] for x in range(1,10)]
    print(mult_table)
    arr = [[x for x in range(3)] for _ in range(5)]
    print(arr)

def dictionaries():
    avatars = {1: "wan", 78: "yangchen", 79: "kuruk", 80: "kyoshi", 81: "roku", 82: "aang", 83: "korra"}
    avatars[80] += " (earth)"

    for k,v in avatars.items():         # .keys(), .values()
        print("%d : %s" %(k,v))
    
    x = {39:42, 38:9, 46:10, 41:19, 1:17, 7:25, 20:16}

    # Sorting dictionaries
    print(dict(sorted(x.items())))                                     # Sort by keys
    print(dict(sorted(x.items(), key=lambda entry: entry[1])))         # Sort by values


##########################
###    CONTROL FLOW    ###
##########################

# TODO!

#######################
###      LOOPS      ###
#######################

# Loops can have else clause, only executes on normal termination, i.e. not after breaks

def for_loop():    
    nations = ["water", "earth", "fire", "air"]

    for i in range(3):
        print(nations[i], end=" ")
    print()

    for i in range(1,4,2):
        print(nations[i], end=" ")
    print()

    for i in range(-1,-4,-1):
        print(nations[i], end=" ")
    print()

    for element in nations:
        print(element, end=" ")
    else:
        print()


############################
###      USER INPUT      ###
############################

# TODO!


##########################
###      FILE I/O      ###
##########################

# Interaction modes: r/w/a (read/write/append)
# File exist modes: + (must exist), x (create if no exist)
# Other modes: b (binary), t (text, for r/w)

def file_io():
    avatars = [("Aang", 82, "Air"),
               ("Kyoshi", 80, "Earth"),
               ("Korra", 83, "Water")]
    
    with open('avatars.csv', 'a') as file:                           # Old: file.close()
        for avatar, no, nation in avatars:
            file.write("%s,%d,%s\n" %(avatar, no, nation))
            print(file.tell())                                       # tell() - curr. ptr position


# ----------------------------------
# -------      EXECUTE       -------
# ----------------------------------

# basics()
# strings()
# lists()
list_comprehensions()
# dictionaries()
# for_loop()
# file_io()
