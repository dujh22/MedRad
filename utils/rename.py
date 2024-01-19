import os
import re

# 设置文件夹路径
folder_path = '/data/paper'

# 定义正则表达式模式以匹配特定前缀
patterns = [
    r"W\d+-",                       # 匹配 "W" 后跟任意数字和一个破折号
    r"W\d+—",  # 匹配 "W" 后跟任意数字和一个破折号
    r"W\d+-修改稿不送审-",            # 匹配具体的字符串模式
    r"W\d+—修改稿不送审-",            # 匹配具体的字符串模式
    r"W\d+-修改稿-",                 # 同上
    r"W\d+—修改稿-",                 # 同上
    r"W\d+ –修改稿-",
    r"W\d+-二查修改稿-",              # 同上
    r"W\d+-二查返回-",               # 同上
    r"W\d+-二次修改后-",              # 同上
    r"二查修改后-",              # 同上
    r"二查修改-",              # 同上
    r"二查修改后无需送审-",
    r"二查修改稿-",
    r"二查修回-",
    r"二次修改后-",
    r"二次修改-",
    r"二查返回-",
    r"修改稿-",
    r"修改稿不送审-"
]

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    if filename.endswith(".json"):  # 确保处理的是JSON文件
        new_name = filename
        for pattern in patterns:
            new_name = re.sub(pattern, "", new_name)  # 使用正则表达式删除匹配的前缀
        # 如果文件名已更改，则重命名文件
        if new_name != filename:
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_name))
