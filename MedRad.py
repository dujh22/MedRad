import QAexamAgent
import MedicalAgent
import ClinicalDiagnosisAgent

class MedRad_Agent:
    def __init__(self):
        self.qa_agent = QAexamAgent()
        self.medical_agent = MedicalAgent()
        self.clinical_diagnosis_agent = ClinicalDiagnosisAgent()

    def handle_query(self, query):
        # 使用QAexamAgent处理医学查询
        result = self.qa_agent.handle_medical_query(query)
        print("问答结果:", result)

    def handle_outpatient_consultation(self, complaint):
        # 使用MedicalAgent处理门诊咨询
        final_decision = self.medical_agent.outpatient_consultation(complaint)
        print("门诊建议:", final_decision)

    def handle_medical_record(self, medical_record):
        # 使用ClinicalDiagnosisAgent处理病历
        discharge_plan = self.clinical_diagnosis_agent.analyze_medical_record(medical_record)
        print("出院计划:", discharge_plan)


# 创建MedRad_Agent实例
MedRad = MedRad_Agent()

# 使用MedRad_Agent处理不同类型的请求
# QAexamAgent 示例
query = {
    "QU": "Naglers反应表现为",
    "OP": {
        "A": "破伤风梭菌",
        "B": "肉毒杆菌",
        "C": "产气荚膜梭菌",
        "D": "败血症梭菌"
    }
}
MedRad.handle_query(query)

# MedicalAgent 示例
complaint = "头疼该怎么办"
MedRad.handle_outpatient_consultation(complaint)

# ClinicalDiagnosisAgent 示例
# 这里需要替换为具体的病历数据
medical_record = "临床病历数据"
MedRad.handle_medical_record(medical_record)
