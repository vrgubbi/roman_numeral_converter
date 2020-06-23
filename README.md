# roman_numeral_converter  
Roman numeral converter that converts integer numbers into Roman numerals  

Introduction:  
Roman numerals are a number system where letters represent numbers. The modern use of Roman numerals involves the letters I, V, X, L, C, D, and M.

Examples:  
160 = C + LX = CLX  
1776 = M + DCC + LXX + VI = MDCCLXXVI  
2014 = MM + X + IV = MMXIV  

The largest number that can be represented in this notation is 3,999 (MMMCMXCIX).  

Programming:  
Python programming language (version 3.x) has been choosen in this project for the conversion of Roman numeral to Integer  

Roman numeral codes and its equivalent integers has been mapped in dictionary
roman_numerals = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'} which can be found in the file roman_numeral_converter.py.  

Function 'get_roman_numerals' has been defined and called. This function has two dependent functions.  

This function takes the one Integer argument which will then be converted to Roman numeral and the same will be returned.  

Test Cases:  
Multiple test cases has been written in the file test_converter to validate the output of Roman numeral conversion.  
