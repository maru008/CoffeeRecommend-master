from subprocess import ABOVE_NORMAL_PRIORITY_CLASS
import csv
import numpy as np

r= open('finished_data_cleaned.csv',encoding='cp949')
data=csv.reader(r)
for i in data:
    print(i)

target_data = [0,1,0,2,1] 

def findSameSakeList(sheet, userSakeReputation):
    SameSakeList = [] 
    sampleLen = len(sheet.col_values(0))-1
    for i in range(sampleLen):
        row = sheet.row_values(i+1)
        if row[userSakeReputation] == 2:
            SameSakeList.append(row)
        else:
            pass
    return SameSakeList

sake_number = 2
sheet = data.sheet_by_index(0)
samePersonList = findSameSakeList(sheet, sake_number)


def get_similarities(samePersonList, target_data):
    similarities = []
    sampleLen = len(samePersonList)

    for j in range(sampleLen):
        distance_list = []
        for i, value in enumerate(target_data):
            if value == -1:
                pass
            else:
                distance = value - samePersonList[j][i]
                distance_list.append(pow(distance, 2))

        similarities.append([j, 1/(1+np.sqrt(sum(distance_list)))])

    return sorted(similarities, key=lambda s: s[1], reverse=True)

def predict(samePersonList, similarities):#全samepersonに対して類似度×評価値をして予測評価値を出す
    predict_list = []
    for index, value in similarities:
        samePersonList[index] = [round(i*value,5) for i in samePersonList[index]] 

    np_samePerson = np.array(samePersonList)
    np_samePerson = list(np.mean(np_samePerson, axis=0))

    for index, value in enumerate(np_samePerson):
        predict_list.append([index, value])
    return sorted(predict_list, key= lambda s: s[1], reverse=True)


samePersonList = findSameSakeList(sheet, sake_number    ) 
similarities = get_similarities(samePersonList, target_data)
ranking = predict(samePersonList, similarities)
print(ranking)


