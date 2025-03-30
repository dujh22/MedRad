# 🏥 MedRad: LLMs驱动的可靠临床决策框架

<div align="center">
  <img src="https://img.shields.io/badge/python-3.11-blue" alt="Python Version">
  <img src="https://img.shields.io/badge/pytorch-2.6.0-orange" alt="PyTorch Version">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
</div>

## 🌟 项目亮点

MedRad是一个革命性的医学决策辅助系统，它就像一位经验丰富的医生助手，能够：

- 🧠 智能分析：结合大语言模型和专业知识
- 🎯 精准诊断：提供可靠的医学决策建议
- 🔄 灵活应用：适用于多种医疗场景
- 🔌 便捷集成：轻松对接现有系统

## 🚀 快速开始

### 1️⃣ 环境准备

首先，让我们准备必要的模型文件：

```bash
# 下载基座模型
git clone https://huggingface.co/baichuan-inc/Baichuan2-13B-Chat
# 或访问 https://github.com/dujh22/AiMed.git

# 下载文本嵌入模型
git clone https://huggingface.co/shibing624/text2vec-base-chinese-paraphrase
```

### 2️⃣ 安装依赖

```bash
# 安装PyTorch（根据您的CUDA版本选择合适的命令）
pip3 install torch torchvision torchaudio

# 安装项目依赖
pip install -r requirements.txt
```

### 3️⃣ 启动服务

启动前，请先修改MedRad/config.py文件中的基座模型路径到所在的文件夹

```bash
# 启动API服务
python openai_api.py
```

### 4️⃣ 本地调用

```bash
python MedRad.py
```

测试数据位于 `data/test_data/` 目录下，包含：

- 医学知识问答测试集
- 门诊对话测试集
- 临床诊断测试集

## 💡 使用示例

除去MedRad.py的实现方式，您也可以直接使用MedRad框架进行二次开发：

### 医学知识问答

```python
import MedRad

# 创建助手实例
medrad = MedRad_Agent()

# 进行医学知识问答
query = {
    "QU": "Naglers反应表现为",
    "OP": {
        "A": "破伤风梭菌",
        "B": "肉毒杆菌",
        "C": "产气荚膜梭菌",
        "D": "败血症梭菌"
    }
}
medrad.handle_query(query)
```

### 门诊咨询

```python
# 处理患者主诉
complaint = "头疼该怎么办"
medrad.handle_outpatient_consultation(complaint)
```

### 临床诊断

```python
# 分析临床病历
medical_record = "临床病历数据"
medrad.handle_medical_record(medical_record)
```

## 📁 项目结构

```
MedRad/
├── Baichuan-13B-Chat/          # 基座模型文件
├── text2vec-base-chinese-paraphrase/  # 文本嵌入模型
├── data/                       # 数据文件夹
│   └── test_data/             # 测试数据
├── utils/                      # 工具脚本
├── openai_api.py              # API服务
├── word_similarity.py         # 词语相似度算法
├── sentence_similarity.py     # 句子相似度算法
├── BaseOnly.py                # 基础功能实现
├── search.py                  # 检索中间件
├── QAexamAgent.py            # 医学知识问答Agent
├── MedicalAgent.py           # 门诊对话Agent
├── ClinicalDiagnosisAgent.py # 临床诊断Agent
└── MedRad.py                 # 主框架
```

## 🤝 贡献指南

欢迎加入我们的开发团队！如果您有任何想法或改进建议，请随时提交Issue或Pull Request。

## 📝 致谢

- 代码开发：Jinhua DU
- 数据支持：清华大学OpenDE团队

---

<div align="center">
  <p>让AI为医疗决策保驾护航</p>
</div>
