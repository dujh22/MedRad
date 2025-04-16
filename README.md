# 🏥 MedRad: LLM-Driven Reliable Clinical Decision Framework

<div align="center">
  <img src="https://img.shields.io/badge/python-3.11-blue" alt="Python Version">
  <img src="https://img.shields.io/badge/pytorch-2.6.0-orange" alt="PyTorch Version">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
</div>

## 🌟 Key Features

MedRad is a revolutionary medical decision support system that acts as an experienced medical assistant, capable of:

- 🧠 Intelligent Analysis: Combining large language models with professional knowledge
- 🎯 Precise Diagnosis: Providing reliable medical decision recommendations
- 🔄 Flexible Application: Suitable for various medical scenarios
- 🔌 Easy Integration: Seamlessly connecting with existing systems

## 🚀 Quick Start

### 1️⃣ Environment Setup

First, let's prepare the necessary model files:

```bash
# Download base model
git clone https://huggingface.co/baichuan-inc/Baichuan2-13B-Chat
# or visit https://github.com/dujh22/AiMed.git

# Download text embedding model
git clone https://huggingface.co/shibing624/text2vec-base-chinese-paraphrase
```

### 2️⃣ Install Dependencies

```bash
# Install PyTorch (choose the appropriate command based on your CUDA version)
pip3 install torch torchvision torchaudio

# Install project dependencies
pip install -r requirements.txt
```

### 3️⃣ Start Service

Before starting, please modify the base model path in MedRad/config.py to point to the correct folder

```bash
# Start API service
python openai_api.py
```

### 4️⃣ Local Usage

```bash
python MedRad.py
```

Test data is located in the `data/test_data/` directory, including:

- Medical knowledge Q&A test set
- Outpatient dialogue test set
- Clinical diagnosis test set

## 💡 Usage Examples

Besides the implementation in MedRad.py, you can also directly use the MedRad framework for secondary development:

### Medical Knowledge Q&A

```python
import MedRad

# Create assistant instance
medrad = MedRad_Agent()

# Perform medical knowledge Q&A
query = {
    "QU": "Nagler's reaction is characterized by",
    "OP": {
        "A": "Clostridium tetani",
        "B": "Clostridium botulinum",
        "C": "Clostridium perfringens",
        "D": "Clostridium septicum"
    }
}
medrad.handle_query(query)
```

### Outpatient Consultation

```python
# Handle patient complaints
complaint = "What should I do about my headache"
medrad.handle_outpatient_consultation(complaint)
```

### Clinical Diagnosis

```python
# Analyze clinical records
medical_record = "Clinical record data"
medrad.handle_medical_record(medical_record)
```

## 📁 Project Structure

```
MedRad/
├── Baichuan-13B-Chat/          # Base model files
├── text2vec-base-chinese-paraphrase/  # Text embedding model
├── data/                       # Data folder
│   └── test_data/             # Test data
├── utils/                      # Utility scripts
├── openai_api.py              # API service
├── word_similarity.py         # Word similarity algorithm
├── sentence_similarity.py     # Sentence similarity algorithm
├── BaseOnly.py                # Basic functionality implementation
├── search.py                  # Search middleware
├── QAexamAgent.py            # Medical knowledge Q&A Agent
├── MedicalAgent.py           # Outpatient dialogue Agent
├── ClinicalDiagnosisAgent.py # Clinical diagnosis Agent
└── MedRad.py                 # Main framework
```

## 🤝 Contributing

Welcome to join our development team! If you have any ideas or suggestions for improvement, please feel free to submit an Issue or Pull Request.

## 📝 Acknowledgments

- Code Development: Not disclosed
- Data Support: Not disclosed

---

<div align="center">
  <p>Let AI safeguard medical decision-making</p>
</div>
