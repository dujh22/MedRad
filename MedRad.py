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

def show_demo():
    # 演示用例
    demo_query = {
        "QU": "Naglers反应表现为",
        "OP": {
            "A": "破伤风梭菌",
            "B": "肉毒杆菌", 
            "C": "产气荚膜梭菌",
            "D": "败血症梭菌"
        }
    }
    demo_complaint = "头疼该怎么办"
    demo_record = """
    患者王某,男,45岁,因"反复头痛2年,加重3天"入院。
    既往有高血压病史5年,规律服用降压药。
    查体:T 36.5℃,P 76次/分,BP 160/95mmHg。
    神志清楚,查体合作。颈软,瞳孔等大同圆。
    """
    return demo_query, demo_complaint, demo_record

def main():
    while True:
        print("\n请选择服务类型:")
        print("1. 医学考试问答")
        print("2. 门诊咨询")
        print("3. 病历分析") 
        print("4. 演示模式")
        print("5. 退出")
        
        choice = input("请输入选择(1-5): ")
        
        if choice == "1":
            print("\n请输入考试题目和选项,格式如下:")
            print('{"QU": "问题", "OP": {"A": "选项A", "B": "选项B", "C": "选项C", "D": "选项D"}}')
            print("直接回车将使用演示题目")
            query_str = input("请输入: ")
            try:
                if query_str.strip():
                    query = json.loads(query_str)
                else:
                    query = show_demo()[0]
                MedRad.handle_query(query)
            except:
                print("输入格式有误,请重试")
                
        elif choice == "2":
            complaint = input("\n请描述您的症状(直接回车使用演示案例): ")
            if not complaint.strip():
                complaint = show_demo()[1]
            MedRad.handle_outpatient_consultation(complaint)
            
        elif choice == "3":
            medical_record = input("\n请输入病历内容(直接回车使用演示案例): ")
            if not medical_record.strip():
                medical_record = show_demo()[2]
            MedRad.handle_medical_record(medical_record)
            
        elif choice == "4":
            print("\n=== 演示模式 ===")
            demo_query, demo_complaint, demo_record = show_demo()
            
            print("\n1. 医学考试问答演示:")
            MedRad.handle_query(demo_query)
            
            print("\n2. 门诊咨询演示:")
            MedRad.handle_outpatient_consultation(demo_complaint)
            
            print("\n3. 病历分析演示:")
            MedRad.handle_medical_record(demo_record)
            
        elif choice == "5":
            print("感谢使用,再见!")
            break
            
        else:
            print("无效的选择,请重试")

if __name__ == "__main__":
    main()
