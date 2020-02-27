from pyquery import PyQuery as pq
html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1">first item</li>
         <li class="item-2">first item</li>
         <li class="item-3">first item</li>
     </ul>
 </div>
'''
doc = pq(html)
lis = doc('li').items()
for li in lis:
    print(li)