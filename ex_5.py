def swap_start_and_end_bits(binary_number):
    tape = list(binary_number)
    if len(tape) >= 2:
        start_bit = tape[0]
        end_bit = tape[-1]

        tape[0] = end_bit
        tape[-1] = start_bit

    return ''.join(tape)


# Przykład użycia:
binary_number = "11010"
result = swap_start_and_end_bits(binary_number)
print(result)  # Wynik to "01011"
