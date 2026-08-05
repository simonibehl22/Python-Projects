#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Functions about word reductions

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Simoni
'''
__version__ = 1

def loadWords():
    '''
    This function opens the words_alpha.txt file, reads it
    line-by-line, and adds each word into a list.  It returns
    the list containing all words in the file.
    '''
    with open('words_alpha.txt') as wordFile:
        wordList = []
        
        for line in wordFile:
            wordList.append(line.rstrip('\n'))

    return wordList

def reduceOne(firstString, secondString, wordList):
    ''' 
    This function will take two strings in wordList and determine if the 
    second string can be reduced from the first string, returning True
    if valid and False if not
    '''
    
    if firstString in wordList and secondString in wordList:
        if len(secondString) == len(firstString) - 1:
            for i in range(len(firstString)):
                if firstString[: i] + firstString[i + 1 :] == secondString:
                    return True
    return False


def reduceAll(word, wordList):
    ''' 
    This function will take a provided string and list, and create a 
    collection of strings that can be reduced from the string, word, by taking
    away one letter and it will check to see if the words in the list are in 
    wordList
    '''
    
    reduceList = []
    
    for i in range(len(word)):
        new = word[: i] + word[i + 1 :]
        
        if new in wordList:
            reduceList.append(new)
            
    return reduceList
        
        
def reduceTwoAll(word, wordList):
    ''' 
    This function will take a provided string and list, and create a 
    collection of strings that can be reduced from the string, word, by taking
    two letters away and check to see if the words in the new list are in 
    wordList
    ''' 
    
    reduceOnce = reduceAll(word)
    reduceTwice = []
    
    for s in reduceOnce:
        reduceTwice += reduceAll(s, wordList) 

    return reduceTwice


def validateReduction(reduction, wordList):
    '''
    This function will take an input list, reduction, and confirm whether or 
    not it represents a valid sequence of reductions. It will take two lists 
    and return a Boolean based on if the words in recduction are in wordList
    '''
    
    if len(reduction) == 1:
        return reduction[0] in wordList
        
    for l in range(len(reduction) - 1):
        if not reduceOne(reduction[l], reduction[l + 1], wordList):
            return False
        
    return True


def main():
    # Here is where you will call your test cases
    wordList = loadWords()
    testRO(wordList)
    testRA(wordList)
    testRTA(wordList)
    testVR(wordList)
    
    print("All tests passed...")



###############################################################

# Here is where you will write your test case functions
    
# Below are the tests for reduceOne()
def testRO(wordList):
    # Test 1: tests if both strings are in wordList
    assert reduceOne("boats", "oats", wordList) == True, \
        "Both strings are in wordList"
    # Test 2: tests for neither strings being in wordList
    assert reduceOne("flabber", "flabbe", wordList) == False, \
        "Neither string is in wordList"
    # Test 3: tests to see if either string is in wordList
    assert reduceOne("flab", "fla", wordList) == False, \
        "secondString is not in wordList"
    # Test 4: test to see if the reduction is correct
    assert reduceOne("boats", "hats", wordList) == False, \
        "secondString is not reduced from firstString correctly"
        
# Below are the tests for reduceAll()
def testRA(wordList):
    # Test 1: test to see when the reduced version is correct and in wordList
    assert reduceAll("boats", wordList) == ["oats", "bats", "bots", "boas","boat"], \
        "Test failed, expected: ['oats', 'bats', 'bots', 'boas', 'boat'']"
    # Test 2: test to see when the reduced version is not in wordList
    assert reduceAll("e", wordList) == [], \
        "Test failed, no word left after reduction"
    # Test 3: test to see if the word is not in wordList
    assert reduceAll("xyz", wordList) == [], \
        "Test failed, 'xyz' not in wordList"
    # Test 4: test to see if the reduced list has the correct versions 
    assert set(reduceAll("rate", wordList)) == {"rat", "ate"}, \
        "Test failed, expected: ['rat', 'ate']"

# Below are the tests for reduceTwoAll()
def testRTA(wordList):
   # Test 1: test to see if the result list is correct
   assert set(reduceTwoAll("eerie", wordList)) == {"rie", "eer", "ere"}, \
       "Test failed, expected: ['rie', 'eer', 'ere']"
   # Test 2: test to see when the reduced version is not in wordList
   assert reduceTwoAll("eerie", wordList) == [], \
       "Test failed, 'eie' is not in wordList"
   # Test 3: test to see if the reduced list has the correct words
   assert set(reduceTwoAll("stare", wordList)) == {"tar", "are", "bat"}, \
       "Test failed, 'bat' not correct reduction"
   # Test 4: test to see when the reduced version is not in wordList
   assert reduceTwoAll("xyz", wordList) == [], \
       "Test failed, 'xyz' not in wordList"
    
# Below are the tests for validateReduction()
def testVR(wordList):
    # Test 1: test to see if only one valid word in wordList is valid
    oneValid = ["affidavit"]
    assert validateReduction(oneValid, wordList) == True, "Should be valid"
    # Test 2: test to see if the proper reductions are added to the list
    validSeq = ["oats", "bats", "bots", "boas", "boat"]
    assert validateReduction(validSeq, wordList) == True, "Should be valid"
    # Test 3: test to see if an incorrect addition to the list is invalid
    invalidSeq = ["oats", "nats", "bots", "boas"]
    assert validateReduction(invalidSeq, wordList) == False, \
        "Should be invalid, 'nats' not correct reduction"
    # Test 4: test to see if a word not in wordList is invalid
    oneInvalid = ["xyz"]
    assert validateReduction(oneInvalid, wordList) == False, \
        "Should be invalid, 'xyz' not in list"
    
    
###############################################################    
    
if __name__ == "__main__":
    main()    