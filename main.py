import re

s = "apple ace asde asxf ape bdaxe acce abaDe a.e a/e a?e"

result = re.findall(pattern="a[^a-zA-Z]e", string=s)
# a.e 匹配任意以a开头以e结尾。 通配符表任意
print(result)  # ['ase', 'axe', 'ace']
