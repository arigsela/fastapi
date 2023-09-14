"""
String Formating
"""

first_name = "Ari"
print("Hi " + first_name)

# f (formatting) String
print(f"Hi {first_name}")

sentence = "Hi {} {}"
lastname = "Sela"
print(sentence.format(first_name, lastname))
