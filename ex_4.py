def move_first_letter_to_end(input_text):
    tape = list(input_text)
    if len(tape) > 1:
        first_letter = tape[0]
        tape[0] = tape[1]

        for i in range(1, len(tape) - 1):
            tape[i] = tape[i + 1]

        tape[-1] = first_letter

    return ''.join(tape)


# Use case:
input_text = "ABCDEF"
result = move_first_letter_to_end(input_text)
print(result)  # Result "BCDEFA"
