#!/bin/python3

weight = int(input("Weight: "))
input_unit = input("(K)g or (L)bs: ")

if input_unit == 'L' or input_unit == 'l':
	print("WWeight in Kg: ",(weight * 0.45))
elif input_unit.upper() == "K":
	print("Weight in Lbs: ",(weight // 0.45))
