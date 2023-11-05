def add_one_to_binary_tape(binary_tape):
    tape = list(binary_tape)
    carry = 1
    index = len(tape) - 1

    while index >= 0:
        if tape[index] == '0':
            tape[index] = '1'
            carry = 0
            break
        else:
            tape[index] = '0'
            index -= 1

    if carry == 1:
        tape.insert(0, '1')

    return ''.join(tape)

# Przykład użycia:
binary_number = "1101"
result = add_one_to_binary_tape(binary_number)
print(result)  # Wynik to "1110"
