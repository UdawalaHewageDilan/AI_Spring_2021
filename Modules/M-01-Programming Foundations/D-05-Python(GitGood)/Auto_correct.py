import re

text = """as it turned out our chance meeting with 
REverend aRTHUR BElling was
was to change our whole way of life, and every sunday we'd hurry along to 
St lOONY up the Cream BUn and Jam."""

text = text.lower()


pattern_day = re.compile(r'\w{3}day')

matches = pattern_day.findall(text)
for match in matches:
    
