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
###      DATA TYPES      ###
############################

# Core data types: str[ing], int[eger], float[ing point]

def strings():
    quote = "When you base your expectations only on what you see, you blind yourself to the possibilities."
    print(len(quote))                   # Get length, e.g. 94
    print(quote[19:31])                 # Format: [start?:end?:step?]
    print(quote[:52])
    print(quote[-40:])                  # Reverse indexing
    print("Spirit World"[::-1])
    print(f'"{quote}" -Zaheer')         # Formatted string, :s (string) default
    print(f'Cabbage Corp. Loan: ${27500000:,.2f} | interest rate={.0387498:.3%}')


def arrays():
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

# ----------------------------------
# -------      EXECUTE       -------
# ----------------------------------

# basics()
# strings()
# arrays()
# for_loop()
