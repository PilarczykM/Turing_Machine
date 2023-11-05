def replace_a_with_c(input_string):
    tape = list(input_string)
    index = 0

    while index < len(tape):
        if tape[index] == 'A':
            tape[index] = 'C'
        index += 1

    return ''.join(tape)

# Example usecase:
input_text = "BACA"
result = replace_a_with_c(input_text)
print(result)  # Result "BCCC"
