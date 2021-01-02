def is_palindrome(input_string):
    new_string = ""
    reverse_string = ""
    input_string = input_string.lower()

    for i in input_string:
        if i != " ":
            new_string = new_string + i
            reverse_string = i + reverse_string

    if new_string == reverse_string:
        return True
    return False


print(is_palindrome("Never Odd or Even"))  # Should be True
print(is_palindrome("abc"))  # Should be False
print(is_palindrome("malayalam"))  # Should be True
