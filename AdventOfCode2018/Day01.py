import Utilities

input_numbers: list[int] = [int(item) for item in Utilities.read_lines_from_file("Input/Day01.txt")]

frequency: int = sum(input_numbers)

print("The Sum of all frequencies is: " + str(frequency))

previous_frequencies: set[int] = set()
frequency = 0
duplicate_found: bool = False
while not duplicate_found:
    for number in input_numbers:
        frequency += number
        if frequency in previous_frequencies:
            print("The first dupicate frequency was: " + str(frequency))
            duplicate_found = True
            break
        previous_frequencies.add(frequency)
        