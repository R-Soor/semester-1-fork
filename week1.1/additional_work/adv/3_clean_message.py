"""Advanced Task 3: Clean Message Toolkit
- Collect a message that might contain extra spaces or mixed casing.
- Use at least three different string methods (e.g. strip, title, replace, upper) to tidy the message.
- Print the original and cleaned versions so the difference is obvious.
- Extension: show the message length before and after cleaning.
"""

raw_message = input("Type a message to tidy: ")
raw_length = len(raw_message)
stripped_message = raw_message.strip()
lowercased_message = stripped_message.lower()
titled_message = lowercased_message.title()
cleaned_length = len(titled_message)
print(f"Here is the original mesage: {raw_message}, and here is the cleaned version: {titled_message}, original length ={raw_length}, cleaned length ={cleaned_length}")


# TODO: apply a sequence of string methods to produce a cleaned_message
# Example methods: strip, title, replace, lower, upper
# TODO: display the original and cleaned messages
# Extension: display the character counts for each version
