# File: Pokemon.py
# Description: Given 2 team rosters of Pokemon, remove duplicate matchups
#       Follow heuristics so that the resulting teams have strong Pokemon
#       Ensure resulting rosters are still the same size.
# Student Name: 
# Student UT EID: 
# Course Name: 
# Unique Number: 

import sys

# DO NO EDIT THIS CLASS DEFINITION
class Pokemon(object):
    kind = ""
    strength = 0

    def __init__(self, kind, strength):
        self.kind = kind
        self.strength = strength

    def __str__(self):
        return "{" + self.kind + ", " + str(self.strength) + "}"


# Input: two lists a, b of Pokemon which are guaranteed to be the same length
# Output: nothing is returned. a, b are edited so that there are no Pokemon of
#  the same kind in the same index, and so that both have the same length.
#  Further rules are followed according to T1: Pokemon documentation.
def updateTeams(a, b):
    # YOUR CODE GOES HERE
    dict_a= {a[i]: a[i + 1] for i in range(0, len(a), 2)}
    dict_b= {b[i]: b[i + 1] for i in range(0, len(b), 2)}
    #remove lowest value with a duplicate key from a
    for key, value in dict_a.items():
        #remove duplicate key with lowest value
        if key in dict_a:
            if value < a[key]:
                dict_a.pop(key)
    #remove lowest value with a duplicate key from b
    for key, value in dict_b.items():
        #remove duplicate key with lowest value
        if key in dict_b:
            if value < dict_b[key]:
                dict_b.pop(key)
    #sort by highest value in a
    dict_a = sorted(a.items(), key=lambda x: x[1], reverse=True)
    #sort by highest value in b
    dict_b = sorted(b.items(), key=lambda x: x[1], reverse=True)
    if len(dict_a)>len(dict_b):
        #remove first key in a
        a.pop(0)
    if len(dict_b)>len(dict_a):
        #remove first key in b
        dict_b.pop(0)
        
    #if key a[i] is in b[i] remove both keys
    for i in range(len(dict_a)):
        for j in range(len(dict_b)):
            if dict_a[i] == dict_b[j]:
                dict_a.pop(i)
                dict_b.pop(j)
    return(dict_a,dict_b)
    # Feel free to add helper functions as needed
    print("Missing Code in updateTeams")


# BE CAREFUL EDITING ANYTHING BELOW THIS LINE

# Input: list [string1, string2] representing kind, strength of a Pokemon respectively
# Precondition: string2 should be convertable to int
# Output: Pokemon initialized with the indicated kind and strength
def buildPokemon(t):
    return Pokemon(t[0], int(t[1]))

def main():
    # read in team size
    k = int(sys.stdin.readline().strip())

    # read in each team, convert to Pokemon
    # note that Pokemon kind may not include whitespace
    teamA = [buildPokemon(sys.stdin.readline().strip().split()) for i in range(k)]
    teamB = [buildPokemon(sys.stdin.readline().strip().split()) for j in range(k)]
    
    # update rosters according to given rules
    updateTeams(teamA, teamB)

    # output updated roster
    print("Team A Updated Roster:")
    for p in teamA:
        print(str(p))
    print("Team B Updated Roster:")
    for p in teamB:
        print(str(p))

if __name__ == "__main__":
    main()

      
