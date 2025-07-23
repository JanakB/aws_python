import re
txt="The rain in spain"
print(re.search("^The.*spain$",txt))
print(re.search(".*rain.*spain$"))

