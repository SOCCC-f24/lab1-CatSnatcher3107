#!/usr/bin/python3
"""
        temp.py - converts Celsius temperatures to Fahrenheit
        Created by: Sophia Brady
        Created on: 091024
        Course number: CSC 138 
        Course Section: EG

        Changes: Added parenthesis to make sure the formula could run properly. Changed the print line so the result would have F to symbolize the Uuits of Fahrenheit
"""
def c2f(c):
    return (c * 9 / 5) + 32
#this is the formula used to convert Celsius to Fahrenheit
def main(cel):
    return c2f(cel)

if __name__ == "__main__":
    cel = 100         # input (Celsius)
    print(f"{main(cel)}F")  # output (Fahrenheit)
