# -*- coding: utf-8 -*-
"""
Created on Tue May  3 14:02:59 2016
centertextInASCII
Desc: Centers text in ASCII

This was created when I was first learning Python. It is sloppy, and has
been hackishly massaged into a module for < 30 min dev time!

@author: Mike
"""

import sys
import argparse

############################ Function Declarations ############################

def isOdd(number):
    # Returns 1 if odd
    # Returns 0 if even
    return number % 2
    
def charProcessor(text, num_chars_total, spaces, cen):
    # Input text to be centered, total num of chars in line, num spaces on each
    # side, and centering.  Returns number of chars on left of the text, and 
    # number of chars on right of the text

    # Check to make sure centering are not equal but are either 0 or 1
    if (cen[0] == cen[1]) or ((cen[0] != 0 and cen[0] != 1) or \
            (cen[1] != 0 and cen[1] != 1)):
        sys.exit('Bad input. Read directions and fix.')
    
    len_text = len(text)
    
    # Simply for readibility:
    num_chars_base = (num_chars_total - len_text - 2*spaces)/2
    
    # TWO MAIN CASES: EVEN num_chars_total, ODD num_chars_total
    # CASE: Even num chars in a line
    if isOdd(num_chars_total) == 0:
        # SUBCASE: Even num chars in word
        if isOdd(len_text) == 0:
            num_chars_left = num_chars_base
            num_chars_right = num_chars_left
        # SUBCASE: Odd num chars in a word
        elif isOdd(len_text) == 1:
            num_chars_left = num_chars_base - .5*cen[0] + .5*cen[1]
            num_chars_right = num_chars_left + cen[0] - cen[1]
    # CASE: Odd num chars in a line   
    elif isOdd(num_chars_total) == 1:
        # SUBCASE: Even num chars in word
        if isOdd(len_text) == 0:
            num_chars_left = num_chars_base  - .5*cen[0] + .5*cen[1]
            num_chars_right = num_chars_left + cen[0] - cen[1]
        # SUBCASE: O
        elif isOdd(len_text) == 1:
            num_chars_left = num_chars_base
            num_chars_right = num_chars_left
            
    return num_chars_left, num_chars_right

def strBuilder(text, num_chars_total, num_chars_left, num_chars_right, line_char, spaces, do_filler):
    filler_string = ''    
    new_string = ''
    for char in range(int(num_chars_left)):
        new_string += line_char
        
    for char in range(int(spaces)):
        new_string += ' '
        
    for char in range(len(text)):
        new_string += text[char]
        
    for char in range(int(spaces)):
        new_string += ' '
        
    for char in range(int(num_chars_right)):
        new_string += line_char
    
    if do_filler == 1:    
        for char in range(num_chars_total):
            filler_string += line_char
    return new_string, filler_string

###############################################################################
############################## Begin User Input ###############################
###############################################################################
def block(text, num_chars_total=79, line_char='#', spaces=1, do_filler=1):
    
    ''' keeping old code as docstring 
    
#    # Num chars to make up one line
#    num_chars_total = 79
#    
#    # Char to make line with:
#    line_char = '#'
#    
#    # Text to insert:
#    text = 'Data imported, time data in \'timeline\''
#    
#    # How many spaces on each side?
#    spaces = 1
#    
#    # Print with surrounding filler lines?
#    do_filler = 1
#    
#    # [OPTIONAL] which side to default text shift to when cannot be perfectly cen?
#    # Pick one or the other (not supported rn)
#    # [(L), R]
    
    This is blockv1, for making text blocks from a module imported into your
    environment. v2 was designed to be a standalone. Eventually they should
    be merged, once it is known how to do this in an elegant, Pythonic manner.
    '''
    cen = [1, 0]

    num_L, num_R = charProcessor(text, num_chars_total, spaces, cen)
    
    new_string, filler_string = strBuilder(text, num_chars_total, num_L, num_R, line_char, spaces, do_filler)
    
    print(filler_string + '\n' + new_string + '\n' + filler_string)    

################################ Scratch Work #################################

# Cases for odd total, odd text (ok)
# even total, even text (really ok)
# odd total or text, need to modify first fillerchars -1

'''
test case of 9 chars for line
#########
for oddnumchars and odd words, just delete amount and insert
ex: poo
## poo ##

for oddnumchars and even words, have to shift. default is left.
# shit ##


testcase of 10 chars for line
##########
for evennumchars and odd words, have to shift. default is left.
## poo ###

for evennumchars and even words, just delete amount and insert.
## shit ##
'''