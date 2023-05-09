def programa():
    while True:
        number_keywords=int(input())
        if not number_keywords:
            break
        else:
            List_keywords=list(input().split())
            score_keywords=list(map(int, input().split()))
            keywords={}
            for i in range(number_keywords):
                keywords[List_keywords[i]]=score_keywords[i]
            sentence=list(input().split())
            sentence=set(sentence)
            sentence=list(sentence)
            score=0
            for palabra in sentence:
                if palabra in keywords:
                    score+=keywords[palabra]
            print(score)
                
        


programa()