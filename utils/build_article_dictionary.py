import os
import json


def clean_string(s):
    """清理字符串，将非 UTF-8 字符替换为下划线"""
    new_str = []
    for char in s:
        try:
            char.encode('utf-8')
            new_str.append(char)
        except UnicodeEncodeError:
            new_str.append('_')
    return ''.join(new_str)


def generate_file_paths(directory_path, output_json_path):
    file_paths = {}

    # 遍历指定文件夹
    for foldername, subfolders, filenames in os.walk(directory_path):
        for filename in filenames:
            # 清理文件名和路径
            clean_filename = clean_string(filename)
            clean_foldername = clean_string(foldername)
            file_key = clean_filename.replace(".json", "")
            file_value = os.path.abspath(os.path.join(clean_foldername, clean_filename))
            file_paths[file_key] = file_value

    # 保存到json文件
    with open(output_json_path, 'w', encoding='utf-8') as json_file:
        json.dump(file_paths, json_file, ensure_ascii=False, indent=4)


# 调用函数
directory_path = '/data/paper'  # 替换为文件夹路径
output_json_path = '/data/paper_index.json'  # json文件的保存路径和名称
generate_file_paths(directory_path, output_json_path)
