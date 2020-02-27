from pyquery import PyQuery as pq
html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
doc = pq(html)
items = doc('.list')
print(type(items))
print(items)
lis = items.find('li')  # 查找子节点
print(type(lis))
print(lis)
# find 的查找范围是节点的所有子孙节点，而如果我们只想查找子节点，那可以用 children 方法
print('-----------')
lis = items.children('.active')
print(type(lis))
print(lis)