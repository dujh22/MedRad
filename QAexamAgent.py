#!/usr/bin/env python3
# coding: utf-8

# 本脚本适用于pytho3.10及以上
import requests
from search import *

class QAexamAgent:
    def __init__(self):
        # 设置是否逐步输出还是只输出最终结果
        self.step_by_step = True
        # 模型api
        self.url = 'http://192.168.0.118:2227/v1/chat/completions'
        # 请求头
        self.header = {'Content-Type': 'application/json'}
        # 请求体
        self.data = {
            'model': "AiMed",
            'stream': True,
            'temperature': 1
        }

    def handle_medical_query(self, query):
        # 从json格式的Query中拆解出各部分信息
        Question_all = json.dumps(query, ensure_ascii=False)
        question = query.get("QU")
        if self.step_by_step: print(f"Question: {question}")
        open_options = query.get("OP")
        if self.step_by_step: 
            print("Options:")
            for option, value in open_options.items():
                print(f"{option}: {value}")
        option_A = open_options.get("A") if open_options.get("A") else ""
        option_B = open_options.get("B") if open_options.get("B") else ""
        option_C = open_options.get("C") if open_options.get("C") else ""
        option_D = open_options.get("D") if open_options.get("D") else ""

        # 使用信息检索技术检索相关信息
        related_information = self.retrieve_information(Question_all)
        
        # 解析每个选项，并与检索到的信息进行比较
        option_A_result = self.analyze_option(Question_all, option_A, related_information)
        option_B_result = self.analyze_option(Question_all, option_B, related_information)
        option_C_result = self.analyze_option(Question_all, option_C, related_information)
        option_D_result = self.analyze_option(Question_all, option_D, related_information)
        
        # 综合分析每个选项的结果
        final_answer = self.conclude_answer(Question_all, option_A_result, option_B_result, option_C_result, option_D_result)
        
        return final_answer

    def retrieve_information(self, query):
        # 实现具体的信息检索逻辑
        related_information = []
        related_information.append(rag_disease(query, topn = 1, similarity_k = 0.5))
        if self.step_by_step:
            print('\n')
            print("-" * 50)
            print('\n')
            print("RAG检索到的信息有:")
            print('\n')
            for info in related_information:
                print(info)  
        # 将每个字典转换为JSON字符串
        json_strings = [json.dumps(obj) for obj in related_information]
        # 将所有JSON字符串拼接成一个字符串
        combined_string = ''.join(json_strings)
        return combined_string

    def analyze_option(self, question, option, information):
        # 解析选项，并与信息进行比较
        prompt = "问题是{},关于该选择题的其中一个选项是{},你能分析一下这个选项吗，其他信息可供你参考：{}, ".format(question,option, information)
        if self.step_by_step:
            print('\n')
            print("-" * 50)
            print('\n')
            print(prompt)
            print('\n')
            print("-" * 50)
            print('\n')
            print("选项 {} 的分析结果是:".format(option))
            print('\n')
        analysis_result = self.model_reply(prompt)
        return analysis_result

    def conclude_answer(self, query, *options_results):
        # 对比各个选项的分析结果，得出最终答案
        prompt = "问题:{},针对选项A分析结果:{},选项B分析结果:{},选项C分析结果:{},选项D分析结果:{},请给出该问题的正确选项".format(query,options_results[0], options_results[1],options_results[2],options_results[3])
        if self.step_by_step:
            print('\n')
            print("-" * 50)
            print('\n')
            print(prompt)
            print('\n')
            print("-" * 50)
            print('\n')
            print("最终答案是:")
            print('\n')
        best_option = self.model_reply(prompt)
        return best_option
    
    def model_reply(self, prompt):
        reply = ""
        messages = []
        messages.append({"role": "user", "content": prompt})
        self.data["messages"] = messages
        # 模型回复
        if self.step_by_step:
            response = requests.post(self.url, headers=self.header, json=self.data, stream=True)
            for chunk in response.iter_content(chunk_size=1024): # 注意chunk是bytes类型，需要先转换
                # 处理响应内容
                # 将bytes类型转换为字符串类型
                str_obj = chunk.decode('utf-8')
                str_obj = str_obj.replace('data: ', '').strip()
                try:
                    # 将字符串类型转换为json格式
                    json_obj = json.loads(str_obj)
                    # 直接解析到对应回复的解析
                    if 'content' in json_obj['choices'][0]['delta'].keys():
                        print(json_obj['choices'][0]['delta']['content'], end="", flush=True)  # 同一行流式结果
                        reply += json_obj['choices'][0]['delta']['content']
                except:
                    continue
        else:
            response = requests.post(self.url, headers=self.header, json=self.data, stream=True)
            for chunk in response.iter_content(chunk_size=1024): 
                str_obj = chunk.decode('utf-8')
                str_obj = str_obj.replace('data: ', '').strip()
                try:
                    json_obj = json.loads(str_obj)
                    if 'content' in json_obj['choices'][0]['delta'].keys():
                        reply += json_obj['choices'][0]['delta']['content']
                except:
                    continue
        return reply


# 示例使用
agent = QAexamAgent()
query = {
    "QU": "Naglers反应表现为",
    "OP":
    {
        "A": "破伤风梭菌",
        "B": "肉毒杆菌",
        "C": "产气荚膜梭菌",
        "D": "败血症梭菌"
    }
}
result = agent.handle_medical_query(query)
print(result)
print("标准答案为：C")
