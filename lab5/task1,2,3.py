import re
# ex 1
text = "ab a0b"
x = re.findall(r'(ab|a[0])', text)
print(x)

# ex 2
text = "abbb abbb abb abc abd"
x = re.findall(r'abb|abbb', text)
x = re.findall(r'.*ab{2,3}.*', text)
print(x)

# ex 3
text = "aaaa_a_a aaa A_A"
x = re.findall(r"[a-z]_[a-z]+",text)
print(x)