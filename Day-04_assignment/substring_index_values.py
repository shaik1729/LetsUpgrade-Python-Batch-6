import re

str = "what we think we become; we are python programmer"
print("      index")
for m in re.finditer('we', str):
         print('we -->', m.start())