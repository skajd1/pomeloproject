import numpy as np
from konlpy.tag import Okt
import math

# text는 리스트에 문장 단위로 텍스트 데이터가 저장돼있음

def get_similarity(token_list):
    similarity = []
    for i, token_i in enumerate(token_list):
        tmp = []
        for j, token_j in enumerate(token_list):
            if i==j : tmp.append(0.)
            else :
                its = len(set(token_i) & set(token_j))
                ii = math.log(len(token_i))
                jj = math.log(len(token_j))
                tmp.append(its/(ii+jj))
        similarity.append(tmp)
    return similarity

def pagerank(x, df=0.85, max_iter=30):
    assert 0 < df < 1

    # initialize
    A = x/x.sum(axis= 0)

    R = np.ones(A.shape[0]).reshape(-1,1)
    bias = (1 - df) * np.ones(A.shape[0]).reshape(-1,1)
    # iteration
    for _ in range(max_iter):
        R = df * (A * R) + bias

    return R

def summary(text):
    global g
    okt = Okt()
    ntext = []
    for x in text :
        ntext.append(x.strip()) 
    # token_list 변수에 각 문장이 key이고 value는 그 문장의 명사를 추출하여 저장
    token_list = dict()
    for x in ntext:
        token_list[x] = okt.nouns(x)
    graph = np.array(get_similarity(token_list))
    
    rank = pagerank(graph)
    
    # rank의 합이 가장 높은게 제일 중요한 문장
    text_summary = []
    index = rank.sum(axis=1).argsort()[-3:]
    for i in index:
        text_summary.append(text[i])
    print(text_summary)
    return text_summary
summary(['나는 사람이다', '나는 박우철이다', '사람과 가장 친한 동물인 개다','개 또한 포유류다','사람은 포유류다','어제 아침은 너무 피곤했다','난 지금 카디비 노래를 듣고 있다.','왜 제대로 동작안하지','난 사람 아닌듯'])





