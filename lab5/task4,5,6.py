import re


# ex 4
text = "Aaaaaa aaaa"
x = re.findall(r"([A-Z][a-z]+)",text)
print(x)

# ex 5
text = "asdsdb"
x = re.search(r"a.*?b$",text)
print(x)

# ex 6
text = "dsds hello.ds jdjfs,dsds"
x = re.sub(r"[ ,.]", ":", text)
print(x)
