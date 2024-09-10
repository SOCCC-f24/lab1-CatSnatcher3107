#!/usr/bin/python3
"""
Sophia Brady, CSC 138 EG, September 10th, 2024
"""
def c2f(c):
    return (c * 9 / 5) + 32
#this is the formula used to convert Celsius to Fahrenheit
def main(cel):
    return c2f(cel)

if __name__ == "__main__":
    cel = 100         # input (Celsius is set to 100 degrees)
    print(f"{main(cel)}F")  # output (Fahrenheit, I made the code to print F to symbolize that the result of this code was in Fahrenheit)
