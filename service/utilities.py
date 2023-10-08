import string
import random
import os
from env import PUBLIC_DIR, FILENAME_SIZE
from pdf import get_abstract
from sentence_transformers import SentenceTransformer, util


def random_file_name():
    letters = string.ascii_lowercase + string.ascii_uppercase
    while True:
        file_name = ''.join(random.choice(letters) for _ in range(FILENAME_SIZE))    
        full_file_name = f'{PUBLIC_DIR}/{file_name}'
        if not os.path.exists(file_name):
            return full_file_name, file_name
        

def similarity(main_abs, rest_abs):
    model = SentenceTransformer('all-mpnet-base-v2')
    embedding1 = model.encode(main_abs, convert_to_tensor=True)
    scores = []
    for i in rest_abs:
        embed = model.encode(i, convert_to_tensor=True)
        cosine_similarity = util.pytorch_cos_sim(embedding1, embed)
        similarity_score = cosine_similarity.item()
        scores.append(cosine_similarity)
    return similarity_score


def get_similar_files(filename):
    main_abstact = get_abstract(filename)
    other_files = [i for i in os.listdir(PUBLIC_DIR) if i != filename]
    abstracts = []
    scores = []
    for fielname in other_files:
        abstracts.append(get_abstract(fielname))
        score = similarity(main_abstact, abstracts)
        scores.append(score)

    similar_projects = []
    for i in range(len(scores)):
        print(scores[i])
        if scores[i] > 0.4:
            similar_projects.append(other_files[i])
    return similar_projects



