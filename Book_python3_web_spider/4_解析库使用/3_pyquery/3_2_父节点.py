html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
from pyquery import PyQuery as pq
doc = pq(html)
items = doc('.list')
container = items.parent()  # parent 方法来获取某个节点的父节点，
print(type(container))
print(container)

print('----------------------')
# print(items.parents())  # 祖父节点,返回所有的祖先节点。
parent = items.parents('.wrap')  # 筛选返回祖父节点
print(parent)