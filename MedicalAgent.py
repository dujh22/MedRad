#!/usr/bin/env python3
# coding: utf-8

# 本脚本适用于pytho3.10及以上
import requests
from search import *

class MedicalAgent:
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
    
    def outpatient_consultation(self, complaint):
        # 门诊流程
        symptoms = self.analyze_patient_complaint(complaint)
        symptom_info, disease_info, check_info, test_info = self.retrieve_relevant_information(symptoms)
        diagnosis = self.preliminary_diagnosis(symptom_info, disease_info)
        examination_suggestions = self.suggest_examinations(test_info, check_info)
        treatment_suggestions = self.suggest_treatments(diagnosis)
        guidelines = self.retrieve_guidelines(symptoms)
        final_decision = self.make_final_decision(guidelines, examination_suggestions, treatment_suggestions)
        return final_decision
    
    def analyze_patient_complaint(self, complaint):
        # 分析患者的主诉并提取关键症状信息
        prompt = "请根据患者的主诉分析关键症状: " + complaint
        if self.step_by_step:
            print("分析的症状:")
        symptoms = self.model_reply(prompt)
        return symptoms

    def retrieve_relevant_information(self, symptoms):
        # 根据症状同步检索症状库、疾病库、检查库和检验库
        symptom_info = self.json_list_to_str(rag_symptomatic(symptoms, topn = 1, similarity_k = 0.5))
        disease_info = self.json_list_to_str(rag_disease(symptoms, topn = 1, similarity_k = 0.5))
        check_info = self.json_list_to_str(rag_check(symptoms, topn = 1, similarity_k = 0.5))
        test_info = self.json_list_to_str(rag_exam(symptoms, topn = 1, similarity_k = 0.5))
        if self.step_by_step:
            print("检索到的症状信息:", symptom_info)
            print("检索到的疾病信息:", disease_info)
            print("检索到的检查信息:", check_info)
            print("检索到的检验信息:", test_info)
        return symptom_info, disease_info, check_info,test_info

    def preliminary_diagnosis(self, symptom_info, disease_info):
        # 使用检索到的信息进行初步诊断
        prompt = "初步诊断: 症状信息: " + symptom_info + ", 疾病信息: " + disease_info
        if self.step_by_step:
            print("初步诊断:")
        diagnosis = self.model_reply(prompt)
        return diagnosis

    def suggest_examinations(self, test_info, check_info):
        # 根据检查库和检验库的信息提出检查建议
        prompt = "检查建议: " + test_info + ", 检验建议: " + check_info
        if self.step_by_step:
            print("检查检验建议:")
        examination_suggestions = self.model_reply(prompt)
        return examination_suggestions

    def suggest_treatments(self, diagnosis):
        # 在初步诊断的基础上提出治疗建议
        prompt = "治疗建议: " + diagnosis
        if self.step_by_step:
            print("治疗建议:")
        treatment_suggestions = self.model_reply(prompt)
        return treatment_suggestions

    def retrieve_guidelines(self, symptoms):
        # 检索相关的文献和指南
        guidelines = self.json_list_to_str(rag_guidebook(symptoms, topn = 1, similarity_k = 0.5))
        return guidelines

    def make_final_decision(self, guidelines, examination_suggestions, treatment_suggestions):
        # 综合所有信息并给出总结性决策
        prompt = "最终决策: 指南: " + guidelines + ", 检查建议: " + examination_suggestions + ", 治疗建议: " + treatment_suggestions
        if self.step_by_step:
            print("最终决策:")
        final_decision = self.model_reply(prompt)
        return final_decision

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
    
    def json_list_to_str(self, json_list):
        # 将每个字典转换为JSON字符串
        json_strings = [json.dumps(obj) for obj in json_list]
        # 将所有JSON字符串拼接成一个字符串
        combined_string = ''.join(json_strings)
        return combined_string

# 示例使用
agent = MedicalAgent()
complaint = "感冒"
final_decision = agent.outpatient_consultation(complaint)