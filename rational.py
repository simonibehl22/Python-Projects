#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 11:38:34 2024

@author: simoni
"""

""" Defining a Rational number class
Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Simoni Behl """

class Rational:
    """ The Rational class allows us to implement rational numbers with exact precision, 
    without the approximations/errors used in binary representations """
     
    def __init__(self, iNum, iDen):
        """ Constructs a new Rational object with value iNum/iDen stored in hidden __numerator 
        and __denominator variables.  Calls reduce() to put the fraction in lowest term """
        self.__numerator = iNum
        self.__denominator = iDen
        self.reduce()
    
    
    def getNumerator(self):
        ''' accessor for the __numerator instance variable'''
        
        return self.__numerator
        
    
    def getDenominator(self):
        ''' accessor for the __denominator instance variable'''
        
        return self.__denominator
        
    
    def setNumerator(self, n):
        ''' 
        This function is a mutator that sets the numerator instance variable
        '''
        
        self. __numerator = n
        self.reduce()
        
            
    def setDenominator(self, d):
        ''' 
        This function is a mutator that sets the denominator instance variable
        '''
        
        self.__denominator = d
        self.reduce()
        
        
    def isValid(self):
        ''' 
        This function returns a boolean based on whether the fraction is valid,
        by checking the denominator is not 0
        '''
        
        if self.__denominator == 0 or None:
            return False

        return True
    
    
    def reciprocal(self):
        ''' 
        This function takes the fraction and updates the numerator and
        denominator with its reciprocal value
        '''
        
        self.__numerator, self.__denominator = self.__denominator, self.__numerator
        self.reduce()
        
    
    def add(self, num2):
        '''
        This function adds two fractions together and updates the numerator and
        denominator to their new values
        '''
        commonDenominator = self.__denominator * num2.getDenominator()
        newNumerator = self.__numerator * num2.getDenominator()
        Num2Numerator = num2.getNumerator() * self.__denominator
        
        self.__numerator = newNumerator + Num2Numerator
        self.__denominator = commonDenominator
        
        self.reduce()

  	
    def sub(self, num2):
        '''
        This function subtracts two fractions and updates the numerator and
        denominator to their new values
        '''
        commonDenominator = self.__denominator * num2.getDenominator()
        newNumerator = self.__numerator * num2.getDenominator()
        num2Numerator = num2.getNumerator() * self.__denominator
        
        self.__numerator = newNumerator - num2Numerator
        self.__denominator = commonDenominator
        
        self.reduce()
        
             
    def mult(self, num2):
        '''
        This function multiplies two fractions and updates the numerator and
        denominator to their new values
        '''
        self.__numerator = self.__numerator * num2.getNumerator()
        self.__denominator = self.__denominator * num2.getDenominator()
        
        self.reduce()
        
    def div(self, num2):
        '''
        This function divides two fractions and updates the numerator and
        denominator to their new values
        '''
        self.__numerator = self.__numerator * num2.getDenominator()
        self.__denominator = self.__denominator *num2.getNumerator()
        
        self.reduce()
    
    
    ################################
    #    HELPER FUNCTIONS BELOW    #
    ################################
    def reduce(self):
        """ Reduces the Rational to lowest terms
        - Checks if both the numerator and denominator are negative; if so, makes both positive
        - Calls gcf() to find the greatest common factor between the numerator and denominator, and
            continues to divide by that gcf until the greatest common factor is 1 """
        if self.__numerator < 0 and self.__denominator < 0:
            self.__numerator = -self.__numerator
            self.__denominator = -self.__denominator
        common = 0
        while (common != 1):
            common = self.gcf()
            self.__numerator /= common
            self.__denominator /= common
    
    def gcf(self):
        """ Determines the greatest common factor between the numerator and denominator
        - Starts checking numbers counting downward from the smaller of the numerator,denominator pair
        - When it finds a number divisble by both, it breaks the loop and returns that number
        - The smallest number that can be returned is 1 """
        common_factor = 1
        for i in range(min(abs(int(self.__numerator)), abs(int(self.__denominator))), 1, -1):
            if self.__numerator % i == 0 and self.__denominator % i == 0:
                 common_factor = i
                 break
        return common_factor
    
    def __str__(self):
        """ Returns a string representation of the Rational, e.g. "1/8" """
        return str(int(self.__numerator)) + "/" + str(int(self.__denominator))
    
    def __eq__(self, r2):
        """ Determines if two Rationals are exactly equal to each other 
        (same numerator and same denominator, no consideration of reducing the numbers) """
        return self.__numerator == r2.__numerator and self.__denominator == r2.__denominator
    
    ################################
    #     END HELPER FUNCTIONS     #
    ################################    
    

def main():
    """ This main should only start rationalTest's unit tests.  
    Do NOT implement your tests here.  WebCAT wants them in rationalTest.py """
    import unittest
    unittest.main("rationalTest")
    
    
if __name__ == "__main__":
    main()
    