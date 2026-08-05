#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 14:31:52 2024

@author: simoni

"I have neither given nor received unauthorized help on this assignment."
author: Simoni Behl 
"""

import unittest
import string



def createTable(phrase):
    ''' Given an input string, create a lowercase playfair table.  The
    table should include no spaces, no punctuation, no numbers, and 
    no Qs -- just the letters [a-p]+[r-z] in some order.  Note that 
    the input phrase may contain uppercase characters which should 
    be converted to lowercase.
    
    Input:   string:         a passphrase
    Output:  list of lists:  a ciphertable '''
    
    # Converts the original phrase to a lowercase string with no spaces 
    # puncuation, numbers, or Q's
    phrase = phrase.strip()
    phrase = phrase.replace(" ", "")
    phrase = phrase.replace("q", "")
    phrase = phrase.translate(str.maketrans('', '', string.punctuation))
    
    seen = set()
    result = []
    
    # Adds the letters from the phrase to a list, ending the list with the 
    # rest of the alphabet and no duplicates
    for char in phrase:
        if char not in seen:
            seen.add(char)
            result.append(char)
            
    # The alphabet with no letter q, used to add to the table
    alpha = 'abcdefghijklmnoprstuvwxyz'
    
    letters = [char for char in alpha if char not in result]
    result = ''.join(result) + ''.join(letters)
            
    table = [result[i : i + 5] for i in range(0, 25, 5)]
    return table
        


def splitString(plaintext):
    ''' Splits a string into a list of two-character pairs.  If the string
    has an odd length, append an 'x' as the last character.  As with
    the previous function, the bigrams should contain no spaces, no
    punctuation, no numbers, and no Qs.  Return the list of bigrams,
    each of which should be lowercase.
    
    Input:   string:  plaintext to be encrypted
    Output:  list:    collection of plaintext bigrams '''
    
    # converting the original phrase to a lowercase string with no spaces 
    # puncuation, numbers, or Q's
    plaintext = plaintext.strip()
    plaintext = plaintext.replace(" ", "")
    plaintext = plaintext.replace("q", "")
    plaintext = plaintext.translate(str.maketrans('', '', string.punctuation))
    plaintext = plaintext.lower()
    
    if len(plaintext) % 2 != 0:
        plaintext += "x"
    bigrams = []
    
    for i in range(0, len(plaintext), 2):
        bigrams.append(plaintext[i : i + 2])
        
    return bigrams



def playfairRuleOne(pair):
    ''' If both letters in the pair are the same, replace the second
    letter with 'x' and return; unless the first letter is also
    'x', in which case replace the second letter with 'z'.
    
    You can assume that any input received by this function will 
    be two characters long and already converted to lowercase.
    
    After this function finishes running, no pair should contain two
    of the same character   
    
    Input:   string:  plaintext bigram
    Output:  string:  potentially modified bigram '''
    
    if pair[0] == pair[1]:
        if pair[0] == 'x':
            return pair[0] + 'z'
            
        else:
            return pair[0] +'x'
    else:
        return pair
            


def playfairRuleTwo(pair, table):
    ''' If the letters in the pair appear in the same row of the table, 
    replace them with the letters to their immediate right respectively
    (wrapping around to the left of a row if a letter in the original
    pair was on the right side of the row).  Return the new pair.
    
    You can assume that the pair input received by this function will 
    be two characters long and already converted to lowercase, and
    that the Playfair Table is valid.
    
    Input:   string:         potentially modified bigram
    Input:   list of lists:  ciphertable
    Output:  string:         potentially modified bigram '''
    
    # Assigns indexes for each object in the list of lists based on their row
    for i, row in enumerate(table):
        if pair[0] in row:
            row1, col1 = i, row.index(pair[0])
        if pair[1] in row:
            row2, col2 = i, row.index(pair[1])
            
    if row1 == row2 and row1 != -1:
        col1 = (col1 + 1) % 5
        col2 = (col2 + 1) % 5
        return table[row1][col1] + table[row2][col2]
    else:
        return pair



def playfairRuleThree(pair, table):
    ''' If the letters in the pair appear in the same column of the table, 
    replace them with the letters immediately below respectively
    (wrapping around to the top of a column if a letter in the original
    pair was at the bottom of the column).  Return the new pair.
    
    You can assume that the pair input received by this function will 
    be two characters long and already converted to lowercase, and
    that the Playfair Table is valid.
    
    Input:   string:         potentially modified bigram
    Input:   list of lists:  ciphertable
    Output:  string:         potentially modified bigram '''
    
   # Assigns indexes for each object in the list of lists based on their column
    for j, row in enumerate(table):
        if pair[0] in row:
            row1, col1 = j, row.index(pair[0])
        if pair[1] in row:
            row2, col2 = j, row.index(pair[1])
            
    if col1 ==  col2:
        newRow1 = (row1 + 1) % 5
        newRow2 = (row2 + 1) % 5
        return table[newRow1][col1] + table[newRow2][col2]
    else:
        return pair
    


def playfairRuleFour(pair, table):
    ''' If the letters are not on the same row and not in the same column, 
    replace them with the letters on the same row respectively but in 
    the other pair of corners of the rectangle defined by the original 
    pair.  The order is important -- the first letter of the ciphertext
    pair is the one that lies on the same row as the first letter of 
    the plaintext pair.
    
    You can assume that the pair input received by this function will 
    be two characters long and already converted to lowercase, and
    that the Playfair Table is valid.  
    
    Input:   string:         potentially modified bigram
    Input:   list of lists:  ciphertable
    Output:  string:         potentially modified bigram '''
    
    
    for k, row in enumerate(table):
        if pair[0] in row:
            row1, col1 = k, row.index(pair[0])
        if pair[1] in row:
            row2, col2 = k, row.index(pair[1])
    
    if row1 != row2 and col1 != col2:
        return table[row1][col2] +table[row2][col1]
    
    else:
        return pair
    
    

def encrypt(pair, table):
    ''' Given a character pair, run it through all four rules to yield
    the encrypted version!
    
    Input:   string:         plaintext bigram
    Input:   list of lists:  ciphertable
    Output:  string:         ciphertext bigram '''
    
    # Takes the pair through each set of rules, to modify it
    cipherBigram = playfairRuleOne(pair)
    cipherBigram = playfairRuleTwo(cipherBigram, table)
    cipherBigram = playfairRuleThree(cipherBigram, table)
    cipherBigram = playfairRuleFour(cipherBigram, table)

    return cipherBigram


def joinPairs(pairsList):
    ''' Given a list of many encrypted pairs, join them all into the 
    final ciphertext string (and return that string)
    
    Input:   list:    collection of ciphertext bigrams
    Output:  string:  ciphertext '''
    
    return ''.join(pairsList)



def main():
    ''' Example main() function '''
    unittest.main() # runs your tests in the TestPlayfair class
    print("Done with unit tests!")

    table = createTable("i am entering a pass phrase")
    splitMessage = splitString("this is a test message")
    pairsList = []

    print(table) # printed for debugging purposes 
    for row in table:
        print(row)
           
    for pair in splitMessage:
        # Note: encrypt() should call the four rules
        pairsList.append(encrypt(pair, table))
    cipherText = joinPairs(pairsList)
    
    print(cipherText) #printed as the encrypted output
    #output should be be hjntntirnpginprnpm
    print("Done with main!")


###############################################################

class TestPlayfair(unittest.TestCase):
    # Below are your tests.  Remember structured tests need to named with 'test' in the
    # beginning so that unittest recognizes them and runs them. 

    def createTable(self):

        expectedTable1 = [
            ['i','a','m','e','n'],
            ['t','r','g','p','s'],
            ['h','b','c','d','f'],
            ['j','k','l','o','u'],
            ['v','w','x','y','z']
            ]
        
        phrase1 = "i am entering a pass phrase"
        # This tests if the function returns the right table given the phrase
        self.assertEqual(createTable(phrase1), expectedTable1, 
                         "Test1: Correct Table!")
        
        phrase2 = "i am ENTERING a pass phrase"
        # This tests if the function handles capital letters
        self.assertEqual(createTable(phrase2), expectedTable1, 
                    "Test2: Correct Table! Capital letters were not included.")
        
        phrase3 = "i am entering a pass phrase: 123"
        # This tests if the function appropriately removes numbers and special
        # characters
        self.assertEqual(createTable(phrase3), expectedTable1, 
            "Test3: Correct Table! Numbers/special characters were removed.")
        
        expectedTable2 =[
            ['a','u','i','c','k'],
            ['p','s','h','r','e'],
            ['b','d','f','g','j'],
            ['l','m','n','o','t'],
            ['v','w','x','y','z']
            ]
    
        phrase4 = "a quick pass phrase"
        #This tests if the function removes 'q' and doesn't include it in the 
        # table
        self.assertEqual(createTable(phrase4), expectedTable2,
                         "Test4: Correct Table! q was removed.")

        
    
    def testSplitString(self):
        # This comment explains what test2() is testing for, and is followed by code
        expectedList1 = ['th', 'is', 'is','th','ep','la','in','te','xt']
        
        plaintext1 = "this is the plaintext"
        # This tests that the function returns the proper list of bigrams
        self.assertEqual(splitString(plaintext1), expectedList1,
                         "Test1: The list has the right bigrams!")
         
        plaintext2 = "this is the plaintext!"
        # This tests if the function removes punctuation
        self.assertEqual(splitString(plaintext2), expectedList1,
                         "Test2: The list is right and removes punctuation!")
       
        
        plaintext3 = "This is the PLAINTEXT"
        # This tests if the function handles capital letters properly
        self.assertEqual(splitString(plaintext3), expectedList1,
                         "Test3: The list is right and doesn't include capital letters!")
        
        expectedList2 = ['th', 'is', 'is','my','pl','ai','nt','ex','tx']
        
        plaintext4 = "this is my plaintext" 
        # This tests that an x is added to the end if the plaintext is odd
        self.assertEqual(splitString(plaintext4), expectedList2,
                      "TTest4: The list correctly adds an x to the last bigram!")
     
     
    def testPlayfairRuleOne(self):
        pair1 = "aa"
        expectedBigram1 = "ax"
        # This tests that the double letter pair, correctly replaces the second
        # character with an x
        self.assertEqual(playfairRuleOne(pair1), expectedBigram1,
                         "Test1: The function correctely converts the pair!")
        
        pair2 ="xx"
        expectedBigram2 = "xz"
        # This tests that the double letter pair, correctly replaces the second
        # character with an z, since the first letter is x
        self.assertEqual(playfairRuleOne(pair2), expectedBigram2,
        "Test2: The function correctely converts the pair !")
        
        pair3 = "ab"
        expectedBigram3 = "ab"
        # This tests that pair is not double letters and shouldm't change
        self.assertEqual(playfairRuleOne(pair3), expectedBigram3,
                    "Test3: The function properly doesn't change the pair!")
        
        pair4 ="cx"
        expectedBigram4 ="cx"
        # This tests that pair is not double letters and shouldm't change
        self.assertEqual(playfairRuleOne(pair4), expectedBigram4,
                    "Test4: The function properly doesn't change the pair!" )
        
    def testPlayfairRuleTwo(self):
        expectedTable1 = [
            ['i','a','m','e','n'],
            ['t','r','g','p','s'],
            ['h','b','c','d','f'],
            ['j','k','l','o','u'],
            ['v','w','x','y','z']
            ]
        
        pair1 = "am"
        expectedBigram1 = "me"
        # This function tests that the right bigram is returned with letters in
        # the same row right next to each other
        self.assertEqual(playfairRuleTwo(pair1, expectedTable1), expectedBigram1,
                    "Test1: The function returns the right modified bigram!")
        
        pair2 = "rp"
        expectedBigram2 = "gs"
        # This function tests that the right bigram is returned with letters in
        # the same row
        self.assertEqual(playfairRuleTwo(pair2, expectedTable1), expectedBigram2,
                    "Test2: The function returns the right modified bigram!")
        pair3 = "cf"
        expectedBigram3 = "dh"
        # This function tests that the bigram correctly wraps back to the first
        # index of the row if the letter given is in the last index
        self.assertEqual(playfairRuleTwo(pair3, expectedTable1), expectedBigram3,
                    "Test3: The function returns the right modified bigram!")
        pair4 = "ed"
        expectedBigram4 = "ed"
        # This function tests that the pair stays the same if the letters are 
        # not in the same row
        self.assertEqual(playfairRuleTwo(pair4, expectedTable1), expectedBigram4,
                "Test4: The function recognizes they aren't in the same row!")
        
        
    def testPlayfairRuleThree(self):
        expectedTable1 = [
            ['i','a','m','e','n'],
            ['t','r','g','p','s'],
            ['h','b','c','d','f'],
            ['j','k','l','o','u'],
            ['v','w','x','y','z']
            ]
        
        pair1 = "th"
        expectedBigram1 = "hj"
        # This function tests that the right bigram is returned with letters in
        # the same column right next to each other
        self.assertEqual(playfairRuleThree(pair1, expectedTable1), expectedBigram1,
                    "Test1: The function returns the right modified bigram!")
        
        pair2 = "lg"
        expectedBigram2 = "xc"
        # This function tests that the right bigram is returned with letters in
        # the same column
        self.assertEqual(playfairRuleThree(pair2, expectedTable1), expectedBigram2,
                    "Test2: The function returns the right modified bigram!")
        pair3 = "tv"
        expectedBigram3 = "hi"
        # This function tests that the bigram correctly wraps back to the first
        # index of the column if the letter given is in the last index
        self.assertEqual(playfairRuleThree(pair3, expectedTable1), expectedBigram3,
                    "Test3: The function returns the right modified bigram!")
        pair4 = "ax"
        expectedBigram4 = "ax"
        # This function tests that the pair stays the same if the letters are 
        # not in the same column
        self.assertEqual(playfairRuleThree(pair4, expectedTable1), expectedBigram4,
            "Test4: The function recognizes they aren't in the same column!")
        
        
    def testPlayfairRuleFour(self):
        expectedTable1 = [
            ['i','a','m','e','n'],
            ['t','r','g','p','s'],
            ['h','b','c','d','f'],
            ['j','k','l','o','u'],
            ['v','w','x','y','z']
            ]
        
        pair1 = "as"
        expectedBigram1 = "nr"
        # This function tests that the pair creates a rectangle and returns
        # the bigram as the letters that make up the other corners
        self.assertEqual(playfairRuleThree(pair1, expectedTable1), expectedBigram1,
                     "Test1: The function returns the right modified bigram!")
        
        pair2 = "jw"
        expectedBigram2 = "kv"
        # This function tests that a diagonal pair creates a rectangle and 
        # returns the bigram as the letters that make up the other corners
        self.assertEqual(playfairRuleThree(pair2, expectedTable1), expectedBigram2,
                    "Test2: The function returns the right modified bigram!")
        pair3 = "fm"
        expectedBigram3 = "cn"
        # This function tests that the pair with a letter on the end creates a 
        # rectangle and returns the bigram as the letters that make up the 
        # other corners
        self.assertEqual(playfairRuleThree(pair3, expectedTable1), expectedBigram3,
                    "Test3: The function returns the right modified bigram!")
        pair4 = "do"
        expectedBigram4 = "ed"
        # This function tests that the pair stays the same if the letters are 
        # do not create a rectangle
        self.assertEqual(playfairRuleThree(pair4, expectedTable1), expectedBigram4,
        "Test4: The function recognizes the bigram doesn't create a rectangle!")
        
    def testEncrypt(self):
        expectedTable1 = [
            ['i','a','m','e','n'],
            ['t','r','g','p','s'],
            ['h','b','c','d','f'],
            ['j','k','l','o','u'],
            ['v','w','x','y','z']
            ]
        
        pair1 = "gg"
        expectedBigram1 = "cm"
        # This function tests if rules 1 and 3 are correctly applied
        self.assertEqual(encrypt(pair1, expectedTable1), expectedBigram1,
                    "Test1: The function properly runs through all the rules!")
        
        pair2 = "bd"
        expectedBigram2 = "cf"
        # This function tests if rule 2 is correctly applied
        self.assertEqual(encrypt(pair2, expectedTable1), expectedBigram2,
                    "Test2:T he function properly runs through all the rules!")
        
        pair3 = "xy"
        expectedBigram3 = "yv"
        # This function tests if rules 1 and 2 are correctly applied
        self.assertEqual(encrypt(pair3, expectedTable1), expectedBigram3,
                    "Test3: The function properly runs through all the rules!")
        pair4 = "lp"
        expectedBigram4 = "go"
        # This function tests if rule 4 is corrected applied
        self.assertEqual(encrypt(pair4, expectedTable1), expectedBigram4,
                    "Test4: The function properly runs through all the rules!")
        
    def testJoinPairs(self):
        # 
        pairsList1 = ['ia','me','nt']
        expectedCiphertext1 = 'iament'
        # This function tests if the list is corrected combined
        self.assertEqual(joinPairs(pairsList1), expectedCiphertext1,
                         "Test1: This function returns the right ciphertext!")
        pairsList2 = ['go']
        expectedCiphertext2 = 'go'
        # This function tests that the right string is returned even with just 
        # one word in the list
        self.assertEqual(joinPairs(pairsList2), expectedCiphertext2,
                         "Test 2: This function returns the right ciphertext!")
        pairsList3 = []
        expectedCiphertext3 = ''
        # This function tests that an empty string is returned if the list is 
        # also empty
        self.assertEqual(joinPairs(pairsList3), expectedCiphertext3,
        "Test 3: This function returns an empty string, since the list is empty!")
            
        pairsList4 =['ia','me','nt','er','in','ga','pa','ss','ph','ra','se']
        # This function tests if the string is right with a long list provided
        expectedCiphertext4 = 'iamenteringapassphrase'
        self.assertEqual(joinPairs(pairsList4), expectedCiphertext4,
                         "Test 4: This function returns the right ciphertext!")


###############################################################    

if __name__ == "__main__":
    main()        