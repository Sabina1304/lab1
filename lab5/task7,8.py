# ex 7
test = "_ggg_sd_ff_midka"
list = re.split(r"[_]+", test)
result = ""
for x in list:
    result += x.capitalize()
print(result)


# ex 8
result = ""
test = "aaAAsBBBdsdsdCCCdsDDD"
list = re.split(r"[A-Z]",test)
for x in list:
        if x != "":
            result += x
    
print(result)