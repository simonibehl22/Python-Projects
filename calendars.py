# -*- coding: utf-8 -*-
"""
"I have neither given nor received help on this assignment."
author: Simoni Behl

This file takes years as inputs and informs if the year is a leap year
according to two different calendars, gregorian and milankovic. It also tells
how many years are leap years between two provided years, for both calendar 
types. Lastly, it also converts years from middle age format to how we refer
to them today and vice versa.

Then there is unittesting to ensure all our functions run smoothly.
"""


def gregorian(year):
    '''This function will take a year as an input and will return a Boolean to 
    inform if that year is a leap year or not under the Gregorian calendar'''
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else: 
                return False
        else: 
            return True
    else:
        return False
        
def milankovic(year):
    '''This function will take a year as an input and will return a 
    Boolean to inform if that year is a leap year or not under the
    Milankovic calendar'''
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 900 == 200 or year % 900 == 600:
                return True
            else: 
                return False   
        else:
            return True
    else: 
        return False


def gregorian_count(year1, year2):
    '''This function will take two years as input and will return the number 
    of leap days between the years inputed on the Gregorian calendar.It is 
    assumed that the year provided represents January 1st of that year.'''
    leap_years = 0
    for year in range(year1, year2):
        if gregorian(year) == True:
            leap_years += 1
    return leap_years
    

def milankovic_count(year1, year2):
    '''This function will take two years as input and will return the number 
    of leap days between the years inputed on the Milankovic calendar. It is 
    assumed that the year provided represents January 1st of that year.'''
    Leap_Years = 0
    for year in range(year1, year2):
        if milankovic(year) == True:
            Leap_Years += 1
    return Leap_Years


def fromMiddle(age, year):
    '''This function will convert a Middle Earth age and year into our modern
    year and returns that year. The Middle Earth age is guaranteed to be between 1 and 7 
    (inclusive).  It is acceptable for our modern year to be negative, we will 
    just consider that to be BC time.'''

    age_lengths = [None, 590, 3441, 3021, 2000, 2000, 2000]
    start = 1971
    years_prior = 0
 
    years_prior = sum(age_lengths[1 : age])
    modern_year = start - years_prior - year
    return modern_year
    

def toMiddle(year):
    '''This function will convert a modern year that is inputed into a Middle 
    Earth age and year, respectively, and it should return a tuple of two 
    integers. There cannot be a negative Middle Earth year.  Instead, it should
    be converted to a previous age, but year zero is valid.'''
    
    age_lengths = [None, 590, 3441, 3021, 2000, 2000, 2000]
    start = 1971
    year_diff = (start - 1) - year
    if year == start:
        me_age = 0
        me_year = 7
    if year != start:
        for age in range(len(age_lengths) -1, 0, -1):
            if year_diff >= age_lengths[age]:
                year_diff -= age_lengths[age]
            else:
                me_age = age
                me_year = age_lengths[age] - year_diff - 1
                return (me_age, me_year)
        

def main():
    # Here is where you can prototype and run some code...
    # Webcat will ignore what's here
    pass


###############################################################

# Here is where you will write your testing code
import unittest

class Test_Calendars(unittest.TestCase):    
  ''' Testing for the gregorian and milankovic calendar functions as well as
  the middle earth conversion functions '''
        
  def test_gregorian1(self):
        # This test will test to make sure the year inputed in
        # the Gregorian function correctly identifies leap years.
        self.assertTrue(gregorian(1960), "Year 1960 should be a leap year") 
        # not divisible by 4
        self.assertTrue(gregorian(2000), "Year 2000 should be a leap year")
        # divisible by 4, 100, and 400
        self.assertFalse(gregorian(2100), "Year should NOT be a leap year") 
        # divisible by 4, 100, but not 400
    
  def test_gregorian2(self):
        # This test will check to see if the gregorian_count function
        # correctly counts the amount of leap years between two years.
        self.assertEqual(gregorian_count(1990, 2010), 5, 
        "There should be 5 leap years counted between 1990 and 2010")
        self.assertEqual(gregorian_count(2010, 2011), 0, 
        "There should be no leap years counted between 2010 and 2011")
        self.assertEqual(gregorian_count(2024, 2015), 0, 
        "year1 should be less than year2")
        self.assertEqual(gregorian_count(2020, 2020), 0, 
        "year1 and year2 should be different")
    
  def test_milankovic1(self):
        # This test will test to make sure the year inputed in
        # the Milkanovic function correctly identifies leap years.
        self.assertTrue(milankovic(1960), "Year 1960 should be a leap year") 
        # divisible by 4 and not 100
        self.assertFalse(milankovic(1966), "Year 1966 should NOT be a leap year") 
        # not divisible by 4
        self.assertTrue(milankovic(2000), "Year 2000 should be a leap year") 
        # divisible by 4, 100, and leaves a remainder of 200 when divided by 
        # 900
        self.assertFalse(milankovic(2100), "Year should NOT be a leap year") 
        # divisible by 4, 100, but doesn't leave a remainder of 200/600 
        # when divided by 900
    
  def test_milankovic2(self):
        # This test will check to see if the milkanovic_count function
        # correctly counts the amount of leap years between two years.
        self.assertEqual(milankovic_count(1980, 2001), 6, 
        "There should be 6 leap years counted between 1980 and 2001")
        self.assertEqual(milankovic_count(2010, 2011), 0, 
        "There should be no leap years counted between 2010 and 2011")
        self.assertEqual(milankovic_count(2024, 2015), 0, 
        "year1 should be less than year2")
        self.assertEqual(milankovic_count(2020, 2020), 0, 
        "year1 and year2 should be different")
        
  def test_fromMiddle(self):
        # This test will check that the age and year inputed respectively, are
        # correctly converted into the modern year form
        self.assertEqual(fromMiddle(6, 1999), 1970, 
        "The age 6 and year 1999 in Middle Earth years, should convert to 1970")
        self.assertEqual(fromMiddle(3, 2941), -4019,
        "The age 3 and year 2941 in Middle Earth years, should convert to -4019")
        
        
  def test_toMiddle(self):
        # This test will convert the year inputed correctly converts to the
        # proper age and year in the modern earth age
        self.assertEqual(toMiddle(0), (6, 29),
        "The year 0, should convert to age 6 and year 29 in Middle Earth years")
        self.assertEqual(toMiddle(-11000), (1, 81),
        "The year -11000, should convert to age 1 and year 81 in Middle Earth years")
       

# ... repeat for all functions, testing throughly for several different 
# inputs producing expected outputs ...
    
    
###############################################################    
    
if __name__ == "__main__":
    main() # needed to actually run the main method
    unittest.main() # finds and runs any test methods in our TestCase classes
    