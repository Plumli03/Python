def reverse_name(backward_name):
    forward_name = ""  # Initialize an empty string to store the reversed name
    length = len(backward_name) - 1  # Start with the last index of the string

    while length >= 0:
        forward_name += backward_name[length]  # Append the current character to the result
        length -= 1  # Move to the previous character

    return forward_name

print(reverse_name("nohtyp"))
