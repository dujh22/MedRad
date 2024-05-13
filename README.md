# MedRad:一个医学大模型的可靠辅助决策框架

## 简介

MedRad是一个先进的医学决策辅助系统，旨在应对医学领域数据的迅速增长和临床决策的复杂性。它结合了大型语言模型、知识工程、Chain of Thought (CoT) 推理、Retrieval-Augmented Generation (RAG) 技术和智能代理，以提升医疗决策的准确性和可靠性。本框架专为不同复杂度的医学场景设计，如医学知识问答、门诊对话和临床病历诊断。

## 特点

- **集成先进技术**：结合了大型语言模型、知识工程等多种技术。
- **高可靠性决策**：专为提供高质量的医学决策路径而设计。
- **灵活适应性**：适用于多种不同的医学应用场景。
- **易于集成**：通过松耦合设计，易于与其他系统集成。

## 安装

1. 请先到[基座模型百川2网址](https://huggingface.co/baichuan-inc/Baichuan2-13B-Chat/tree/main)下载全部模型bin文件到Baichuan-13B-Chat文件夹内，或者到[AiMed网址](https://github.com/dujh22/AiMed.git)下载全部模型bin文件到Baichuan-13B-Chat（如果不修改代码中的文件夹路径参数的话）文件夹内
   同时到[shibing624/text2vec-base-chinese-paraphrase](https://huggingface.co/shibing624/text2vec-base-chinese-paraphrase)下载文本嵌入模型到text2vec-base-chinese-paraphrase文件夹内

2. python选用3.11.5(3.11均可)

3. 安装pytorch

假设本地机器CUDA版本最高支持为11.7, 我们希望尽可能安装可支持的最新的pytorch版本，比如2.0.1，具体下载命令参照：https://pytorch.org/get-started/previous-versions/

```shell
conda install pytorch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 pytorch-cuda=11.7 -c pytorch -c nvidia
```

4. 推理前请安装依赖：

```shell
pip install -r requirements.txt
```

## 项目构成说明

| 名称                                                         | 用途                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Baichuan-13B-Chat文件夹，text2vec-base-chinese-paraphrase文件夹 | 包括项目使用的各种模型的参数数据                             |
| data文件夹                                                   | 包括项目使用的原始数据和处理后的数据，test_data是测试用数据  |
| utils文件夹                                                  | 一些数据处理用脚本                                           |
| openai_api.py                                                | 按照openai标准实现的baichuan流式访问接口，需要最先独立启动：python openai_api.py |
| word_similarity.py                                           | 针对词类型的检索实现的相关算法                               |
| sentence_similarit.py                                        | 针对句子或者篇章类型的检索实现的相关算法                     |
| BaseOnly.py                                                  | 统一对数据的读取、对模型的读取                               |
| search.py                                                    | 大模型调用所有检索算法的中间件                               |
| QAexamAgent.py                                               | 医学知识问答Agent（LLM+RAG+CoT实现）                         |
| MedicalAgent.py                                              | 门诊医患对话Agent（LLM+RAG+CoT实现）                         |
| ClinicalDiagnosisAgent.py                                    | 临床病历诊断Agent（LLM+RAG+CoT实现）                         |
| MedRad.py                                                    | MedRad框架整体Agent                                          |

## 快速开始

提供一个简单的例子来展示如何使用MedRad进行基本的任务。

```python
import MedRad

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
```

## 贡献

代码部分由Jinhua DU完成，数据来源涉及清华大学OpenDE团队。
```
@misc{du24medrad,
author = {Jinhua Du},
title = {MedRad: A Framework for Reliable Assisted Decision Making in a Medical LargeLanguage Model},
year={2024},
publisher = {GitHub},
journal = {GitHub repository},
howpublished = {\url{https://github.com/dujh22/MedRad}}
}
```

