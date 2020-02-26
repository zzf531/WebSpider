import re
"""
\b 匹配任何单词边界(\B 与之相反)
"""

m = re.search('^The', 'The end')
if m is not None:
    print(m.group())

m = re.search(r'\bThe', 'end. The')
if m is not None: print(m.group())

m = re.search(r'\Bthe', 'bitethe dog')
if m is not None: print(m.group())
