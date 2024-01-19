#!/usr/bin/env python3
# coding: utf-8

# 这个脚本适用于python 3.10及以上版本
import requests
from search import *

class ClinicalDiagnosisAgent:
    def __init__(self):
        # 设置是否逐步输出还是只输出最终结果
        self.step_by_step = True
        # 模型API地址
        self.url = 'http://192.168.0.118:2227/v1/chat/completions'
        # 请求头
        self.header = {'Content-Type': 'application/json'}
        # 请求体
        self.data = {
            'model': "AiMed",
            'stream': True,
            'temperature': 1
        }
    
    def analyze_medical_record(self, medical_record):
        # 解构病历内容，提取关键信息
        basic_info = self.decompose_medical_record(medical_record)
        similar_patient_info = self.retrieve_similar_patient_info(basic_info)
        admission_diagnosis = self.analyze_admission_info(basic_info, similar_patient_info)
        treatment_plan = self.analyze_inpatient_info(basic_info, admission_diagnosis)
        discharge_plan = self.analyze_discharge_info(basic_info, treatment_plan)
        return discharge_plan

    def decompose_medical_record(self, medical_record):
        # 解构病历内容，提取关键信息
        prompt = "请解析病历的基本信息: " + medical_record
        basic_info = self.model_reply(prompt)
        return basic_info
    
    def extract_admission_details(self, basic_info):
        # 提取入院信息的细节
        prompt = f"提取入院信息的细节: 基本信息: {basic_info}"
        admission_details = self.model_reply(prompt)
        return admission_details

    def extract_inpatient_details(self, basic_info):
        # 提取住院治疗细节
        prompt = f"提取住院治疗细节: 基本信息: {basic_info}"
        inpatient_details = self.model_reply(prompt)
        return inpatient_details

    def extract_discharge_details(self, basic_info):
        # 提取出院信息的细节
        prompt = f"提取出院信息的细节: 基本信息: {basic_info}"
        discharge_details = self.model_reply(prompt)
        return discharge_details

    def retrieve_similar_patient_info(self, basic_info):
        # 检索相似患者信息
        similar_info = self.json_list_to_str(rag_emr(basic_info, topn = 1, similarity_k = 0.5))
        return similar_info

    def analyze_admission_info(self, basic_info, similar_patient_info):
        # 分析患者的入院信息，包括主诉、病史等
        admission_info = self.extract_admission_details(basic_info)
        # 查询症状和疾病数据库以获取相关信息
        symptom_info = self.json_list_to_str(rag_symptomatic(admission_info, topn = 1, similarity_k = 0.5))
        disease_info = self.json_list_to_str(rag_disease(admission_info, topn = 1, similarity_k = 0.5))
        # 检索与病人症状和疾病相关的文献
        literature_info = self.json_list_to_str(rag_paper(admission_info, topn = 1, similarity_k = 0.5))
        # 结合上述信息，形成初步诊断
        prompt = "请结合以下信息给出初步诊断: " + symptom_info + disease_info + literature_info + similar_patient_info
        admission_diagnosis = self.model_reply(prompt)
        return admission_diagnosis

    def needs_further_examination(self, info):
        # 判断是否需要进一步检查
        prompt = f"判断是否需要进一步检查: {info}"
        needs_check = self.model_reply(prompt)
        return needs_check == '是'

    def analyze_inpatient_info(self, basic_info, admission_diagnosis):
        # 提取和分析住院治疗信息
        inpatient_info = self.extract_inpatient_details(basic_info)
        # 查询药物和手术治疗数据库(手术库暂未实现)
        drug_info = self.json_list_to_str(rag_drug(inpatient_info, topn = 1, similarity_k = 0.5))
        # 根据需要进行进一步检查
        check_info = self.json_list_to_str(rag_check(inpatient_info, topn = 1, similarity_k = 0.5)) if self.needs_further_examination(inpatient_info) else None
        if admission_diagnosis == None:
            admission_diagnosis = ""
        if inpatient_info == None:
            inpatient_info = ""
        if drug_info == None:
            drug_info = ""
        if check_info == None:
            check_info = ""
        # 基于上述信息，制定治疗计划
        prompt = "请结合以下信息制定治疗计划: " + admission_diagnosis + inpatient_info + drug_info + check_info
        treatment_plan = self.model_reply(prompt)
        return treatment_plan

    def analyze_discharge_info(self, basic_info, treatment_plan):
        # 提取和分析出院相关信息
        discharge_info = self.extract_discharge_details(basic_info)
        # 根据需要进行进一步检查
        check_info = self.json_list_to_str(rag_check(discharge_info, topn = 1, similarity_k = 0.5)) if self.needs_further_examination(discharge_info) else None
        # 形成出院诊断
        if treatment_plan == None:
            treatment_plan = ""
        if discharge_info == None:
            discharge_info = ""
        if check_info == None:
            check_info = ""
        prompt = "请结合以下信息制定出院诊断: " + discharge_info + treatment_plan + check_info
        discharge_info = self.model_reply(prompt)
        # 提出出院后的医嘱
        prompt = f"出院医嘱: 出院诊断: {discharge_info}, 进一步检查: {check_info}"
        discharge_advice = self.model_reply(prompt)
        return discharge_info, discharge_advice

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

# 使用伪代码进行病历诊断
agent = ClinicalDiagnosisAgent()
medical_record = "临床病历数据"
discharge_plan = agent.analyze_medical_record(medical_record)