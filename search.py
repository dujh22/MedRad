from BaseOnly import WordModel, guidebook_model, emr_model, paper_model, qa_index, drug_index, check_index, exam_index, disease_index, symptomatic_index, guidebook_index, emr_index, paper_index
import json

# 检索用

def rag_drug(query, topn = 1, similarity_k = 0.8):
    res = WordModel.most_similar(query, topn)
    info = []
    for q_id, c in res.items():
        for corpus_id, s in c.items():
            if s >= similarity_k:
                info.append(drug_index.get(WordModel.corpus[corpus_id]))
    rag = []
    if info:
        for temp_info in info:
            if temp_info == None:
                continue
            file_path = temp_info['file']
            position = temp_info['position']
            with (open(file_path, 'r', encoding='utf-8') as f):
                data_list = json.load(f)
                rag.append(data_list[position])
    return rag

def rag_check(query, topn = 1, similarity_k = 0.8):
    res = WordModel.most_similar(query, topn)
    info = []
    for q_id, c in res.items():
        for corpus_id, s in c.items():
            if s >= similarity_k:
                info.append(check_index.get(WordModel.corpus[corpus_id]))
    rag = []
    if info:
        for temp_info in info:
            if temp_info == None:
                continue
            file_path = temp_info['file']
            position = temp_info['position']
            with (open(file_path, 'r', encoding='utf-8') as f):
                data_list = json.load(f)
                rag.append(data_list[position])
    return rag

def rag_exam(query, topn = 1, similarity_k = 0.8):
    res = WordModel.most_similar(query, topn)
    info = []
    for q_id, c in res.items():
        for corpus_id, s in c.items():
            if s >= similarity_k:
                info.append(exam_index.get(WordModel.corpus[corpus_id]))
    rag = []
    if info:
        for temp_info in info:
            if temp_info == None:
                continue
            file_path = temp_info['file']
            position = temp_info['position']
            with (open(file_path, 'r', encoding='utf-8') as f):
                data_list = json.load(f)
                rag.append(data_list[position])
    return rag

def rag_disease(query, topn = 1, similarity_k = 0.8):
    res = WordModel.most_similar(query, topn)
    info = []
    for q_id, c in res.items():
        for corpus_id, s in c.items():
            if s >= similarity_k:
                info.append(disease_index.get(WordModel.corpus[corpus_id]))
    rag = []
    if info:
        for temp_info in info:
            if temp_info == None:
                continue
            file_path = temp_info['file']
            position = temp_info['position']
            with (open(file_path, 'r', encoding='utf-8') as f):
                data_list = json.load(f)
                rag.append(data_list[position])
    return rag

def rag_symptomatic(query, topn = 1, similarity_k = 0.8):
    res = WordModel.most_similar(query, topn)
    info = []
    for q_id, c in res.items():
        for corpus_id, s in c.items():
            if s >= similarity_k:
                info.append(symptomatic_index.get(WordModel.corpus[corpus_id]))
    rag = []
    if info:
        for temp_info in info:
            if temp_info == None:
                continue
            file_path = temp_info['file']
            position = temp_info['position']
            with (open(file_path, 'r', encoding='utf-8') as f):
                data_list = json.load(f)
                rag.append(data_list[position])
    return rag

def rag_qa(query, topn = 1, similarity_k = 0.8):
    res = WordModel.most_similar(query, topn)
    info = []
    for q_id, c in res.items():
        for corpus_id, s in c.items():
            if s >= similarity_k:
                info.append(qa_index.get(WordModel.corpus[corpus_id]))
    rag = []
    if info:
        for temp_info in info:
            if temp_info == None:
                continue
            file_path = temp_info['file']
            position = temp_info['position']
            with (open(file_path, 'r', encoding='utf-8') as f):
                data_list = json.load(f)
                rag.append(data_list[position])
    return rag

def rag_guidebook(query, topn = 1, similarity_k = 0.8):
    res = guidebook_model.most_similar(query, topn)
    info = []
    for q_id, c in res.items():
        for corpus_id, s in c.items():
            if s > similarity_k:
                info.append(guidebook_index[guidebook_model.corpus[corpus_id]])
    rag = []
    if info:
        for file_path in info:
            if file_path == None:
                continue

            with (open(file_path, 'r', encoding='utf-8') as f):
                data = json.load(f)
                rag.append(data)
    return rag

def rag_emr(query, topn = 1, similarity_k = 0.8):
    res = emr_model.most_similar(query, topn)
    info = []
    for q_id, c in res.items():
        for corpus_id, s in c.items():
            if s > similarity_k:
                info.append(emr_index[emr_model.corpus[corpus_id]])
    rag = []
    if info:
        for file_path in info:
            if file_path == None:
                continue

            with (open(file_path, 'r', encoding='utf-8') as f):
                data = json.load(f)
                rag.append(data)
    return rag

def rag_paper(query, topn = 1, similarity_k = 0.8):
    res = paper_model.most_similar(query, topn)
    info = []
    for q_id, c in res.items():
        for corpus_id, s in c.items():
            if s > similarity_k:
                info.append(paper_index[paper_model.corpus[corpus_id]])
    rag = []
    if info:
        for file_path in info:
            if file_path == None:
                continue

            with (open(file_path, 'r', encoding='utf-8') as f):
                data = json.load(f)
                rag.append(data)
    return rag

if __name__ == "__main__":
    query = ("拉稀伴随腹痛")
    for i in rag_qa(query, 5):
        print(i)
