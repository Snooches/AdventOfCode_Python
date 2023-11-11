from Utilities import *

frequency: int = 0
for value in read_lines_from_file("Input\Day01.txt"):
	number: int = int(value)
	frequency += number
	
print("The Sum of all frequencies is: " + str(frequency))

previous_frequencies: set[int] = set()
frequency: int = 0
duplicate_found: bool = False
while (not duplicate_found):
	for value in read_lines_from_file("Input\Day01.txt"):
		number: int = int(value)
		frequency += number
		if frequency in previous_frequencies:
			print("The first dupicate frequency was: " + str(frequency))
			duplicate_found = True
			break
		else:
			previous_frequencies.add(frequency)