# 构建字典

import os
import json

def index_medicines(directory_path, output_file_path):
    medicine_index = {}

    with open(directory_path, 'r', encoding='utf-8') as f:
        data_list = json.load(f)
        for idx, item in enumerate(data_list):
            medicine_name = item.get('title')
            if medicine_name:
                medicine_index[medicine_name] = {
                    "file": directory_path,
                    "position": idx
                }
                            
    with open(output_file_path, 'w', encoding='utf-8') as f:
        json.dump(medicine_index, f, ensure_ascii=False, indent=4)

# 可以调用这个函数，指定目录和输出文件的路径
index_medicines('/data/qa.json', '/home/djh/code/MedRad/data/qa_index.json')
