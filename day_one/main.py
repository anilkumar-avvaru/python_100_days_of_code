#!/usr/bin/env python3
def generate_band_name():
    print("Welcome to the Band Name Generator.")
    street = input("What's the name of the city you grew up in?\n")
    pet = input("What's your pet's name?\n")
    return street + " " + pet


if __name__ == '__main__':
    band_name = generate_band_name()
    print("Your band name could be " + band_name)
