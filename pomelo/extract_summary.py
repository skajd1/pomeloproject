import numpy as np
from konlpy.tag import Okt, Kkma, Komoran
import math
import re
import kss

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
                tmp.append(its/(1+ii+jj))
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
    okt = Okt()
    ntext = []
    text = kss.split_sentences(text)
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
    for i in sorted(index):
        text_summary.append(text[i])
    return text_summary
    
# t = "카페 라떼종류핫(hot) 또는 아이스(iced) 음료, 밀크 커피원산지이탈리아색깔베이지, 라이트 브라운, 화이트관련 음료카페 모카(초콜릿 맛) 녹차 라테(그린티 라떼) 맛차. 카페 라떼(이탈리아어: caffè latte)는 에스프레소에 뜨거운 우유를 곁들인 커피 가운데 하나이다. 카페 라테는 전 세계에서 찾아볼 수 있는 커피의 한 종류로 카푸치노, 에스프레소와 함께 가장 흔한 메뉴이기도 하다. ‘카페 라테’는 이탈리아어로 ‘우유 커피’를 뜻한다. 프랑스어나 스페인어에서는 그대로 우유를 곁들인 커피라는 문어로, 카페 라떼를 옮겨 적는다. 이탈리아에서 카페 라테는 아침에만 먹는 음료이다. 꼭 정해진 것은 아니지만 커피를 증류해서 컵에 우려낸 다음에 데운 우유를 첨가한다. 이탈리아 외의 나라에서 에스프레소에 따뜻한 우유를 1:2 또는 1:3의 비율로 섞은 것으로 우유가 5mm정도 맨 위에 층을 이루고 있는 것이 특징이며 카푸치노와 흡사하다. 다만 두 종류의 차이는 우유와 에스프레소, 거품의 차이이다. 변종에는 초콜릿 맛의 모카가 포함되거나, 커피를 다른 종류의 우유 혹은 마살라 등으로 대체하기도 한다. 바닐라라테, 라테 마키아토 등 첨가물을 넣은 베리에이션 커피도 있다."
t = "안녕하세요.\n\n 또 다른 대형 헤드헌팅 업체 유앤파트너스는 평판조회 전문 법인 ‘하이어베스트’를 운영한다. 하이어베스트는 평판을 3단계로 나눠 검증한다. 각종 학력과 경력, 범죄 사실 여부를 조회하는 ‘배경 확인 서비스(Background Check Service)’ 후 지명 평판조회를 거친다. 지명 평판조회는 앞서 말한 지정 조회와 마찬가지로 후보자가 지명한 사람들을 대상으로 평판을 조회하는 작업이다."