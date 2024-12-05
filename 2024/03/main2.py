import re
from operator import mul


memory = re.findall(r"(mul\(\d+,\d+\)|don't\(\)|do\(\))", open(0).read())

for dont in [1, 0]:
    print(eval('(' + 
               ''.join(memory).replace("don't()", f')+{dont}*(')
                              .replace('do()', ')+1*(')
                              .replace(')m', ')+m') +
               ')'))

# make 4HbQ proud
