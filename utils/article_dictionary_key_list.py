import json

def load_keys_from_json(json_filepath, output_txt_path):
    # 加载json文件
    with open(json_filepath, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # 将所有键写入到txt文件
    with open(output_txt_path, 'w', encoding='utf-8') as txt_file:
        for key in data.keys():
            key
            txt_file.write(key + '\n')

# 调用函数
json_filepath = '/data/emr_index.json'  # JSON文件路径
output_txt_path = '/data/emr_list.txt'  # 输出的txt文件路径
load_keys_from_json(json_filepath, output_txt_path)
