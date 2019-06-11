import re
str_content ='![](http://127.0.0.1:8000/static/uploadfiles/article/1560232925.png)'
prefix ='http://127.0.0.1:8000'
result = re.findall(r'!\[\]\((.+?)\)',str_content)
for item in result:
    if item.find(prefix):
        continue
    else:
        str_content=str_content.replace(item,prefix+item)
print(str_content)