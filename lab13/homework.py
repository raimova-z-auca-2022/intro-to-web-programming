import re

text = """
Hello, my name is John Doe. You can reach me at 555-1234 or 555-5678.
My email is john.doe@example.com and support@example.org.
There are 12 apples, 34 oranges, and 56 bananas in the basket.
An apple a day keeps the doctor away. Even elephants enjoy eating.
"""

# 1. Extract Phone Numbers
phone_numbers = re.findall(r'\d{3}-\d{4}', text)
print("Phone Numbers Found:", phone_numbers)

# 2. Match at the Start of the String
if re.match(r'Hello', text):
    print("Match found at the start: Hello")
else:
    print("No match at the start")

if re.search(r'Hello', text):
    print("Found: Hello")

# 3. Replace Numbers with "NUMBER"
modified_text = re.sub(r'\d+', 'NUMBER', text)
print("\nModified Text:")
print(modified_text)

# 4. Extract Email Addresses
emails = re.findall(r'\b\w+@\w+\.\w+\b', text)
print("\nEmail Addresses Found:", emails)

# 5. Find Words Starting with a Vowel
vowel_words = re.findall(r'\b[aeiouAEIOU]\w*\b', text, re.IGNORECASE)
print("\nWords starting with a vowel:", vowel_words)
