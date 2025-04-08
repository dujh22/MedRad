
# **Large Language Models Driven Reliable Clinical Decision-Making: Framework and Application**

## *Abstract*

With the proliferation of data and increased complexity of clinical decision-making in the medical field, powerful computational tools are needed to assist physicians in making precision and reliable decisions. While the Large Language Models (LLMs) with billions of parameters in model size have obtained series of achievements in a broad range of biomedical and healthcare applications, the issues in terms of reliability and stability are still needed to be addressed. To this end, we propose the framework of MedRad, a system that combines LLMs, knowledge engineering, Chain of Thought (CoT) reasoning, Retrieval-Augmented Generation (RAG) techniques, and intelligent agents (Agents) to improve clinical decision-making reliability. Based on fine-tuned LLMs and existing studies in biomedical and healthcare domain, we further concentrate on how these techniques could be utilized to achieve highly reliable clinical decision-making in scenarios with varying complexity, such as medical knowledge QA and clinical diagnosis recommendations. Experimental results demonstrate that MedRad has the ability to provide high-quality decision paths in the above scenarios, and the potential to extend to more biomedical and healthcare scenarios through its loosely coupled design.

KEYWORDS

Large Language Models; Clinical Decision-Making; Chain of Thought; Retrieval-Augmented Generation; Intelligent Agents

## *Introduction*

Reliable clinical decision-making is critical to improve the patient health. However, this kind of tasks always holds high complexity due to individual differences. The physicians usually bear huge pressure to handle a large amount of patient information and make critical decisions in a short period of time. Meanwhile, the complexity of clinical decision-making is continually increasing with the massive growth of medical data and the variability of clinical cases. Although the traditional clinical decision support systems (CDSS) are competent in dealing with standardized processes, they could hardly interpret unstructured medical data, handle complex cases, and extend to learn evolving medical knowledge. Accompanied by the public's concern for the quality of healthcare services increasing gradually, evidence-based medical decision-making^1^^ ^has become more and more prominent in research value, which means "combining the best currently available research evidence with one's own professional skills and patient values for treatment". In recent years, with the rapid development of artificial intelligence (AI), machine learning and big data analytics have been introduced into decision support tools to enhance their ability to manage complex data.

However, the applications of AI techniques have been severely challenged due to the complexity of clinical decision-making and the extremely high demands for reliability, such as the lack of theoretical and causal models, sensitivity to imperfect data, and higher arithmetic consumption^2^. In the late of 2022, the release of ChatGPT brought an increasing interest in LLMs^3^, while its powerful capabilities in terms of content generation and human-computer interaction provides potential support to evidence-based clinical decision-making^4^.

In this study, a framework towards LLMs driven reliable clinical decision-making called MedRad, is proposed to improve the accuracy of clinical decision-making, as well as enhance the reliability and stability of decision-making while maintaining the accuracy. By combining the latest artificial intelligence technologies including deep learning, natural language processing, and medical knowledge engineering, MedRad aims to create a more intelligent and adaptive clinical decision-making system, which would not only be able to process and analyze complex medical data, but also give clear, explainable and logical paths of decisions. Therefore, the physicians could better understand and trust the automatic generated decisions. In this way, the MedRad framework seeks to support healthcare professionals to make precision and reliable decisions in an increasingly complex healthcare environment.

![图片描述](./pic/1.png)

Figure 1.   Study framework.

## *Related Works*

![](file:////Users/djh/Library/Containers/com.kingsoft.wpsoffice.mac/Data/tmp/wps-djh/ksohtml//wps4.png)**Clinical Decision Support Systems**

The history of Clinical Decision Support Systems dates back to 1970s. The first generation of CDSS was primarily based on rule-based reasoning to aid decision-making. Over time, data-based machine learning approaches have been gradually integrated into CDSS systems. With the development of powerful computing devices and widespread electronic health records (EHRs), CDSS began to utilize big data for more precision prediction and analysis, further evolving into Intelligent CDSS (ICDSS). Generally, ICDSS could be used to enable accurate diseases diagnosis and management^5^ cancers prevention and metastasis prediction^6^ organ failure prediction and mortality assessment^7^, etc., to help physicians generate clinical, therapeutic and diagnostic approaches for optimal disease management. Driven by artificial intelligence, considerable studies have begun to utilize deep learning techniques to empower ICDSS. For example, Rajkomar et al. demonstrated the potential application of deep learning models to handle EHRs and medical prediction tasks^8^. Moreover, Esteva et al. explored the accuracy of deep learning models in dermatological diagnosis, emphasizing the association between model interpretability and patient safety^9^. The U.S. AI healthcare startups Abridge, Birch.ai to produce solutions to automatically extract cases through doctor-patient dialog^10^.

**Applications of Large Language Models in Healthcare**

In recent years, large pre-trained language models, such as GPT and BERT, have begun to play a key role in medical domain with the development of computing power. These models are capable of processing a huge amounts of unstructured medical text data to provide deeper insights and predictions. Currently, they have been used to automate medical record summaries, medical literature analysis, disease prediction, and provide personalized health care recommendations. Google has led the way by releasing large models such as Med-PALM and Med-PALM2^11^ and presenting the medical assessment dataset MultiMedQA^12^. Although Med-PALM2 with 540B parameters has passed the U.S. Medical Licensing Examination (USMLE) exam with a promising score of 86.5, large language models still face challenges in dealing with highly specialized medical knowledge, especially in understanding complex medical terminology and clinical guidelines.

**Chain of Thought Reasoning and Retrieval-Augmented Generation Technology**

The Chain of Thought (CoT) reasoning technique enhances the logic and transparency of decision making by modeling the physician's thought process. By breaking down the decision-making process into a series of logical steps, CoT provides a more intuitive and interpretable way to explain the model's reasoning process^13^. The main idea is to utilize a large language model to interpret a small number of samples and explain the reasoning process in response to a prompt. Meanwhile, the Retrieval-Augmented Generation (RAG) technique strengthens the model's understanding of medical knowledge by combining powerful retrieval and generative capabilities^14^. This approach allows the model to retrieve relevant information from a large amount of medical data before making a decision, thus improving the accuracy and depth of decision making. Combining CoT and RAG could significantly upgrade the performance of CDSS, especially when dealing with complicated and non-standardized clinical cases.

In summary, despite the significant progress made by large language models in processing specific types of medical data, there are still considerable deficiencies in terms of the stability and reliability of clinical decision-making. This is mainly due to the fact that these models lack in-depth understanding of medical domain-specific knowledge during the training process and may suffer from decision bias induced by the training data. In addition, these models are usually in dispute for sufficient transparency and interpretability, making it difficult for healthcare professionals to understand and trust their decision-making process and also results^15^. Therefore, this paper proposes the MedRad framework, which combines large language modeling, knowledge engineering, CoT and RAG techniques to improve the efficiency and reliability of medical decision making.

## *Method*s

Generally, MedRad is a framework designed for more accurate and reliable medical decisions, which takes advantages of LLMs and logical reasoning principles to a broad dataset of medical knowledge. Specifically, MedRad could be defined as: given a predicate dataset  *D* , the goal is to design and implement a function *f* that enables it to transform the actual needs of a medical scenario *R* into reliable and accurate medical decisions  *A* . Formally, * f * :( *D* ,  *R* ) → *A.* In the following, the meaning of each symbol in the above equation will be introduced in detail.

 *D* : a pre-data set that includes all available medical knowledge resources, both structured data (e.g. knowledge graphs, medical knowledge bases, etc.) and unstructured data (e.g. electronic medical records, online consultation records, etc.).

 *R* : The actual demand of a medical scenario, which may be any medical query or demand, e.g., symptom query, therapeutic regime consultation, etc.

 *A* : The medical decision or advice generated by the function, which is a direct response to the input demand  *R* . *A* should meet the criteria of interpretability and reliability to ensure that the replies provided in different medical contexts are evidence-based.

 *f* : The decision function or model, which is the core transformation mechanism responsible for accepting the predicate dataset *D* and the actual requirements *R* as inputs, then generating the medical decisions *A* as outputs.

These symbols are used to abstractly represent the different components of the proposed medical decision support system. In this way, we could more precisely design and implement the system step-by-step to meet the stringent requirements for accuracy and reliability in the clinical domain. This will be explained in turn below.

### Medical dataset ***D***

A variety of medical data has been utilized to develop MedRad (Table 1). Among them, medical books and research publications were formatted into JSON files, while the rest were converted into text data for LLMs secondary pre-training. All of these data are in Chinese, which covers all aspects of modern medicine in China. However, traditional Chinese medicine data was not addressed here.

Table 1.   Chinese medical dataset for MedRad training.

| **No.** | **Medical data**       | **No. of records** | **Format** |
| ------------- | ---------------------------- | ------------------------ | ---------------- |
| 1             | EHRs                         | 75,240                   | JSON             |
| 2             | Medical books                | 188                      | TXT              |
| 3             | Clinical practice guidelines | 10,030                   | JSON             |
| 4             | Medical journal publications | 200,000                  | TXT              |
| 5             | Disease bank                 | 7,409                    | JSON             |
| 6             | Symptom bank                 | 5,333                    | JSON             |
| 7             | Examination bank             | 522                      | JSON             |
| 8             | Drug bank                    | 8,521                    | JSON             |
| 9             | Medical QA                   | 1,000,000                | JSON             |

### Medical Scenario Requirements ***R***

A whole-process, whole-scene healthcare refers to health management and disease prevention, diagnosis, control, treatment, as well as rehabilitation. Through exhaustive analysis of the mainstream, more than 40 medical scenarios will be involved, for example, intelligent consultation, intelligent imaging, intelligent records, surgical robots, surgical navigation, intelligent operating rooms, AI pharmaceuticals and remote intelligent clinical trials. The AI+ healthcare aims to enhance the efficiency and quality of healthcare services through advanced technologies, and provides patients with precision healthcare management. Especially, two typical medical scenarios were selected for further research and discussion, namely medical knowledge quiz and clinical diagnosis recommendations, which represent the common and the high complexity of clinical decision-making systems respectively.

### *Medical Knowledge QA*

The medical knowledge QA is referred to the task of using AI systems to automatically answer medical questions posed by users in order to meet their knowledge needs. Unlike existing search engines, QA system is an advanced product of information service that return users with precise natural language answers, rather than a list of documents sorted based on keyword matching. To quantitatively evaluate the performance of medical knowledge QA system, a diversity of datasets has been elaborately presented in English, such as MedQA^16^、MedMCQA^17^、MultiMedQA^12^、PubMedQA^18^.[]()

### *Clinical Diagnosis Recommendations*

The clinical diagnosis recommendations scenario typically refers to automatically make decisions about the  subsequent examination and treatment plan based on the doctor-patient dialogues. For example, the patient says, " *Doctor, yesterday I had a sudden weakness and numbness on my right side. It lasted for a few minutes and then went away. I also had difficult speaking for a while. Can you help me figure out what happened?* " A promising decision-making system is supposed to simulate a doctor and answer the question based on the patient's description, such as:

*"You may have experienced a transient ischemic attack. You'd better take some examinations to confirm the diagnosis. We need to start with radiology imaging procedures, hematology tests (blood tests), complete blood count (CBC), x-ray computed tomography (scan CT), electrocardiogram, renal function tests (kidney function tests), and glucose measurements (glucose levels) to get a better understanding of what happened. Can we schedule these examinations for you?"*

### Decision-making methodology ***F***

The MedRad framework specially concentrates on a loosely coupled design with the baseline LLMs, and focuses on how to utilize advanced technologies to achieve more reliable medical decisions in different medical scenarios. Table 2 list the main technologies involved in MedRad.

Table 2.  The main technologies involved in MedRad.

| **No.** | **Technology**                                  | **Description**                                                                                                                                                                  |
| ------------- | ----------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1             | Domain-Specific LLMs Training(Secondary Pre-training) | Train LLMs from scratch for specific medical domains and focus on in-depth learning of medical knowledge. Currently, medical corpus and high computational resource are very critical. |
| 2             | Domain-Adaptive Fine-tuning                           | Further fine-tuning on medical domain data based on general LLMs aims to integrate general information with specialized medical knowledge.                                             |
| 3             | Mixture of Experts (MoE)                              | Integrating multiple expert models through the MoE architecture utilizes the specialized knowledge of different models to improve decision accuracy and reliability19.                 |
| 4             | Retrieval-Augmentation(RAG)                           | A retrieval mechanism allows the model to access external information sources, in order to enhance the ability and quality of decision-making on specific questions.                   |
| 5             | Chain of Thought (CoT)                                | Emphasize that LLMs should provide detailed reasoning steps when making decision, to improve the interpretability and credibility of decisions.                                        |
| 6             | Agents                                                | A system which takes LLMs as its core controllers; Meanwhile, the LLMs could be capable of perceiving its environment and taking actions in a period to achieve its goals.             |

### Decision outcome ***A***

The decision outcome of the proposed MedRad mainly depends on the effective combination of RAG, CoT and Agent technologies. Specifically, MedRad firstly utilizes RAG to look for the information and knowledge related to the scenario from a large amount of medical data, then analyzes the problem by constructing a CoT, and finally combines the Agent's ability to synthesize and evaluate the results of the RAG and CoT for a final decision  *A* .

### *Outcome of Medical Knowledge QA*

In medical knowledge QA scenario, MedRad should learn  massive medical knowledge and accurately understand the question in advance, then quickly return the correct answer. RAG, CoT and Agent will be adopted to implement the QA tasks, see Figure 2. Generally, MedRad takes 5 steps to implement a QA task.

![图片描述](./pic/2.png)

Figure 2.  The framework of medical knowledge QA

① Starts the QA session once the Agent receives a medical question from users;

② The Agent recognizes the question through keyword extraction, categorization of question type (e.g., symptom query, drug information, or disease-related knowledge), and urgency assessment;

③ Adopt RAG technique to find the most relevant information about the question from medical dataset. For each possible option (e.g., A, B, C, D), the Agent analyzes and compares them separately, as well as assesses the accuracy, relevance and reliability. The medical knowledge required here covers medical terminologies, pathological mechanisms, treatment protocols, and also drug effects;

④ The Agent performs a comprehensive analysis to compare the supporting evidence of different options, by considering the consistency of the medical logic and clinical practice; At the same time, it checks the credibility, timeliness, and consistency of the information sources with the existing medical consensus;

⑤ The Agent figures out the best answer based on a comprehensive evaluation of the options and the consistency check with the medical evidence; It then provides feedback to the user, including the basis for the answer, relevant medical information, and possible further recommendations or instructions.

The whole process encompasses the entire workflow from receiving a user question to providing a well-considered, information-supported answer. For practical application, the Agent will also include additional functionalities such as the ability to interact with the user, the ability to handle vague or incomplete queries, and the ability to continuously learn and adapt to new information.

*Outcome of Clinical Diagnosis Recommendations*

For the clinical diagnosis recommendations scenario, MedRad is supposed to automatically diagnose the illness of patient, and suggest the subsequent treatment measures based on the patient's complaint. The approach to deal with such scenarios could use a strategy by combining CoT, RAG and Agent. Generally, the Agent analyzes the patient's chief complaint, diagnoses the disease, and proposes a treatment plan by simulating the doctor's clinical thinking process (CoT). Figure 3 list the main steps involved here.

① The Agent analyzes and understands the patient's complaint, then interprets the key symptom information;

② Based on the Clinical Thinking Path, specific symptoms are extracted from the patient's chief complaint and relevant information will be collected by searching the dataset *D* through RAG;

③ The Agent combines the retrieved data to make a preliminary decision, which always considers the possibilities of different diseases;

④The Agent suggests appropriate clinical examinations  to confirm the diagnosis;

⑤ After checking the examination results, the Agent makes treatment recommendations, including medication, surgery, or other medical interventions; Moreover, with the help of RAG, it searches the medical literature and clinical guidelines to ensure that the recommendations are consistent with the latest medical research and best practices;

⑥ Ultimately, the Agent integrates all the information to provide a comprehensive decision summary, which aimes to assist the physician in determining the best treatment path and also provide clear explaination to the patient.

In the clinical diagnosis recommendations scenario, the Agent simulates the way what a doctor thinks as far as possible at every step to ensure that the resulting decisions meet both clinical standards and the needs of individual patient. This process requires not only advanced natural language processing capabilities, but also an in-depth medical knowledge understanding and strong logical reasoning.

![图片描述](./pic/3.png)

Figure 3.  The framework of clinical diagnosis recommendations.

## *Experiment* & *Results*

 ![](file:////Users/djh/Library/Containers/com.kingsoft.wpsoffice.mac/Data/tmp/wps-djh/ksohtml//wps8.png)This section will demonstrate MedRad's performance in two principal clinical application scenarios and comparatively analyze the experimental results based on current leading LLMs. Especially, the quantitative index,  *precision* , will be adopted to evaluate the ability of medical knowledge QA, while the testing data were collected from the national medical licensing examination in China^20^. Moreover, an open testing platform has been constructed to provide 20 senior chief physicians from top tertiary hospitals in China to be responsible for qualitative evaluation of MedRad. These tests were designed to evaluate the effectiveness and accuracy of MedRad in real-world clinical decision-making.

Given the linguistic diversity of clinical medical data and literature resources, this study particularly emphasizes the importance of supporting multilingualism in the development of MedRad, mainly focusing on the integration of Chinese and English resources. Therefore, the well-known general LLMs, namely GPT-4-Turbo and Baichuan were chosen for the following comparison, both of which are advanced models for natural language processing tasks in English and Chinese separately. In addition, we have specially developed and compared a large model, AiMed, which has been specifically secondary pre-trained for the medical domain based on the Baichuan model, with the aim of exploring the performance of professionally customized models in medical applications.

In order to comprehensively assess the performance of MedRad and the comparative methods, the experimental results would be qualitatively summarized using a grading system with five grades: very poor, barely passed, average, good and excellent, represented by 1-5 stars. This grading system will not only easily visualize the relative performance of each method, but also facilitate the comparison of efficacy in different clinical decision-making scenarios, as shown in in Table 3.

Table 3.   The testing performance of MedRad.

| **Models**             | **QA (Quantitatively)** | **QA (Qualitatively)** | **Clinical Diagnosis** |
| ---------------------------- | ----------------------------- | ---------------------------- | ---------------------------- |
| Baichuan                     | 44.04%                        | **                           | ***                          |
| AiMed                        | 59.46%                        | ***                          | ***                          |
| GPT4-Turbo                   | 65.33%                        | ****                         | ****                         |
| **MedRad-** Baichuan   | 60.72%                        | ***                          | ****                         |
| **MedRad-** AiMed      | 75.85%                        | ****                         | *****                        |
| **MedRad-** GPT4-Turbo | 83.28%                        | *****                        | *****                        |

Specifically for the above results, the model performance is analyzed below. Baichuan performs well in the clinical diagnosis recommendations (three stars), but the lowest score in the medical knowledge QA indicates that it could hardly understand the medical question. GPT-4 performs well in both the medical knowledge quiz and clinical diagnosis recommendations (four stars). After the application of the proposed MedRad framework,   the performance of MedRad-Baichuan, MedRad-AiMed and MedRad-GPT4 have been largely improved. Especially, MedRad-GPT4 performs well (five stars) in the selected scenarios, which proves that the combination of GPT-4 model and MedRad framework has the potential to achieve the best performance in different clinical scenarios.

The MedRad framework and the enhanced models, especially MedRad-GPT4 and MedRad-AiMed, demonstrated their superior performance in two major scenarios: medical knowledge QA and clinical diagnosis recommendations. These results highlight the effectiveness of the MedRad framework in enhancing LLMs to process specialized medical knowledge and complex medical data, understand natural language and clinical conversations. The success of the MedRad framework demonstrates that performance in clinical application scenarios with highly specialized requirements and accuracy needs could be significantly improved by carefully selecting and optimizing the underlying models. This is particularly demonstrated by the overall excellent performance of MedRad-GPT4 in common clinical scenarios, further emphasizing the importance of specialized training for specific applications. In summary, choosing the proper LLMs and performing targeted optimization is the key to achieve efficient AI applications in the clinical and healthcare field.

## *Discussion*

The diversity and complexity of the clinical task makes it a decision-intensive issue. Therefore, drawing clear conclusions based on specific situations and tasks, combined with medical knowledge, is the crux of the matter of clinical decision-making. Although the existing studies, while focusing on accuracy, still fall short in terms of reliability and stability of large models. Because of this, we propose the MedRad framework to build a medical assisted decision-making system that is both accurate and reliable by digging deeper into large language models as well as combining techniques such as CoT, RAG, and Agent to provide higher quality healthcare services.

## **Conclusions**

In the future, MedRad is expected to be able to adapt to more diversified clinical application scenarios with stronger generalization and self-learning capabilities. To this end, MedRad needs to be able to automatically adapt to different application environments through advanced technologies such as Agents, forming a fine-grained decision support subsystem for specific scenarios. At the same time, MedRad should be able to automatically optimize its decision-making framework based on the feedback of actual results during the decision-making process. With the advancement of technology and in-depth research, MedRad would be effectively integrated into clinical practice, not only providing clinicians with powerful assistive tools to enhance the efficiency and safety of diagnosis and treatment, but also helping doctors to improve their work efficiency and focus on more complex and urgent medical tasks. In addition, the application of MedRad will greatly alleviate the current strain on medical resources and enable patients to utilize this tool for initial self-diagnosis, ushering in a new era of clinical practice that combines AI technology and human expertise.

## **Acknowledgments**

This work was funded by the CAMS Fund, grant number 2024MESP010.

---

## **Conflicts of Interest**

None declared.

---

## **References**

1. Guyatt G, Cairns J, Churchill D, et al. Evidence-based medicine: a new approach to teaching the practice of medicine.  *JAMA* , 1992;268(17):2420-2425.

2. Begoli E, Bhattacharya T, Kusnezov D. The need for uncertainty quantification in machine-assisted medical decision making. *N**at** M**ach** I* *ntell* , 2019;1(1):20-23.

3. [Birhane A, Kasirzadeh A, Leslie D, Wachter S.]() Science in the age of large language models. *N**at** R**ev** P* *hys* , 2023;1-4.

4. Ferdush J, Begum M, Hossain ST. Chatgpt and clinical decision support: Scope, application, and limitations. *A**nn** B**iomed** E* *ng* , 2023;1-6.

5. Price-Haywood EG, Robinson W, Harden-Barrios J, Burton J, Burstain T. Intelligent clinical decision support to improve safe opioid management of chronic noncancer pain in primary care. *O**chsner* * J* , 2018;18(1):30-35.

6. Feng QX, Liu C, Qi L, et al. An intelligent clinical decision support system for preoperative prediction of lymph node metastasis in gastric cancer. *J A**m** C**oll** R* *adiol* , 2019;16(7):952-960.

7. Gago P, Santos MF, Silva A, Cortez P, Neves J, Gomes L. Intcare: a knowledge discovery based intelligent decision support system for intensive care medicine. *J D**ecis** S* *yst* , 2005;14(3):241-259.

8. Rajkomar A, Oren E, Chen K, et al. Scalable and accurate deep learning with electronic health records. *NPJ D**igit** M* *ed* , 2018;1(1):18.

9. Esteva A, Kuprel B, Novoa RA, et al. Dermatologist-level classification of skin cancer with deep neural networks.  *Nature* , 2017;542(7639):115-118.

10. Alsentzer E, Murphy JR, Boag W, et al. Publicly available clinical BERT embeddings.  *Association for Computational Linguistics* ; 2019:72-78.

11. Singhal K, Tu T, Gottweis J, et al. Towards expert-level medical question answering with large language models. A *rXiv* .2023; abs/2305.09617.

12. Singhal K, Azizi S, Tu T, et al. Large language models encode clinical knowledge.  *Nature* , 2023;620(7972):172-180.

13. Wei J, Wang X, Schuurmans D, et al. Chain-of-thought prompting elicits reasoning in large language models. presented at: Proceedings of the 36th International Conference on Neural Information Processing Systems; 2024; New Orleans, LA, USA.

14. Lewis P, Perez E, Piktus A, et al. Retrieval-augmented generation for knowledge-intensive NLP tasks. presented at: Proceedings of the 34th International Conference on Neural Information Processing Systems; 2020; Vancouver, BC, Canada.

15. Ribeiro MT, Singh S, Guestrin C. “why should i trust you?” explaining the predictions of any classifier presented at: Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining; 2016; San Francisco, California, USA.

16. Jin D, Pan E, Oufattole N, et al. What disease does this patient have? a large-scale open domain question answering dataset from medical exams. ArXiv. 2020;abs/2009.13081

17. Pal A, Umapathi LK, Sankarasubbu M. MedMCQA:A large-scale multi-subject multi-choice dataset for medical domain question answering. presented at: Proceedings of the Conference on Health, Inference, and Learning; 2022; Proceedings of Machine Learning Research. https://proceedings.mlr.press/v174/pal22a.html

18. [Jin Q, Dhingra B, Liu Z, Cohen W, Lu X. PubMedQA: A Dataset for Biomedical Research Question Answering. Association for Computational Linguistics; 2019:2567-2577.]()

19. Artetxe M, Bhosale S, Goyal N, et al. Efficient large scale language modeling with mixtures of experts.  *Association for Computational Linguistics* ; 2022:11699-11732.

20.Lyu T, Li X, Zhang Y, et al. Study on the Construction of a Question-Answer Corpus Dataset for Chinese Medical Knowledge Large Language Models.  *J Med Inf* . 2024;45(05):20-25.
