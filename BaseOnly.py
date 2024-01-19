from sentence_similarity import AnnoySimilarity
import json

# 词模型
from word_similarity import WordEmbeddingSimilarity
WordModel = WordEmbeddingSimilarity(model_name_or_path = '/home/djh/code/MedRad/text2vec-base-chinese-paraphrase/pytorch_model')

# 知识库
# 药品
drug_index_place = '/home/djh/code/MedRad/data/drug_index.json'
with open(drug_index_place, 'r', encoding='utf-8') as drug_index_f:
    drug_index = json.load(drug_index_f)
WordModel.add_corpus(list(drug_index.keys()))
# 检查
check_index_place = '/home/djh/code/MedRad/data/check_index.json'
with open(check_index_place, 'r', encoding='utf-8') as check_index_f:
    check_index = json.load(check_index_f)
WordModel.add_corpus(list(check_index.keys()))
# 检验
exam_index_place = '/home/djh/code/MedRad/data/exam_index.json'
with open(exam_index_place, 'r', encoding='utf-8') as exam_index_f:
    exam_index = json.load(exam_index_f)
WordModel.add_corpus(list(exam_index.keys()))
# 疾病
disease_index_place = '/home/djh/code/MedRad/data/disease_index.json'
with open(disease_index_place, 'r', encoding='utf-8') as disease_index_f:
    disease_index = json.load(disease_index_f)
WordModel.add_corpus(list(disease_index.keys()))
# 症状
symptomatic_index_place = '/home/djh/code/MedRad/data/symptomatic_index.json'
with open(symptomatic_index_place, 'r', encoding='utf-8') as symptomatic_index_f:
    symptomatic_index = json.load(symptomatic_index_f)
WordModel.add_corpus(list(symptomatic_index.keys()))
# QA
qa_index_place = '/home/djh/code/MedRad/data/qa_index.json'
with open(qa_index_place, 'r', encoding='utf-8') as qa_index_f:
    qa_index = json.load(qa_index_f)
WordModel.add_corpus(list(qa_index.keys()))

# 句模型
# 指南
guidebook_index_place = "/home/djh/code/MedRad/data/guidebook_index.json"
with open(guidebook_index_place, 'r', encoding='utf-8') as guidebook_index_f:
    guidebook_index = json.load(guidebook_index_f)
# guidebook_corpus = list(guidebook_index.keys())
# guidebook_model = AnnoySimilarity(corpus=guidebook_corpus)
# guidebook_model.build_index()
guidebook_index_file = '/home/djh/code/MedRad/data/guidebook_annoy_model.index'
#guidebook_model.save_index(guidebook_index_file)
guidebook_model = AnnoySimilarity()
guidebook_model.load_index(guidebook_index_file)

# 电子病历
emr_index_place = "/home/djh/code/MedRad/data/emr_index.json"
with open(emr_index_place, 'r', encoding='utf-8') as emr_index_f:
    emr_index = json.load(emr_index_f)
# emr_corpus = list(emr_index.keys())
# emr_model = AnnoySimilarity(corpus=emr_corpus)
# emr_model.build_index()
emr_index_file = '/home/djh/code/MedRad/data/emr_annoy_model.index'
# emr_model.save_index(emr_index_file)
emr_model = AnnoySimilarity()
emr_model.load_index(emr_index_file)

# 论文
paper_index_place = "/home/djh/code/MedRad/data/paper_index.json"
with open(paper_index_place, 'r', encoding='utf-8') as paper_index_f:
    paper_index = json.load(paper_index_f)
# paper_corpus = list(paper_index.keys())
# paper_model = AnnoySimilarity(corpus=paper_corpus)
# paper_model.build_index()
paper_index_file = '/home/djh/code/MedRad/data/paper_annoy_model.index'
# paper_model.save_index(paper_index_file)
paper_model = AnnoySimilarity()
paper_model.load_index(paper_index_file)