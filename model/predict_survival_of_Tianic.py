# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

#-*- coding:utf8 -*-
#!usr/bin/python

# <codecell>

# Filename:         class_Predicted_survival_of_Tianic.py
# Description:      Predicted the survival of Tianic based on Naive Bayesian model.
# Data Type:        .csv
# Date Description: After preprocessing on the raw data, we get two data set:handled_test.csv and handled_train.csv.Each
#                   flie contains PassengerId,Age,Sex,Fare four main fields.And the difference is the handled_train includes
#                   survived filed additionally.
# Author:           zhmi
# E-mail:           
# Create:           2016-1-25
# Recent-changes:   2016-1-25

# <codecell>

import string
import math
import csv

# <codecell>

input_data_path = "/home/zhmi/Pycharm Project/Predict_survival_of_Tianic/input_data"
train_data_path = input_data_path + "/handled_train.csv"
test_data_path = input_data_path + "/handled_test.csv"

# <codecell>

def readFile(path):
    fp = open(path)
    raw_list = fp.readlines()
    filter_list = map(lambda x: x.strip(),raw_list)
    data_list = map(lambda x: x.split(","),filter_list)
    fp.close()
    return data_list

# <codecell>

def filterDataByCategory(data_list, category_id):
    category_list = map(lambda x: x[category_id],data_list)
    category_list = map(lambda x: int(math.floor(float(x))),category_list[1:])
    return category_list

# <codecell>

def mergeCategoryWithSurvived(survived_list,category_list):
    survived_category_list = map(None,survived_list,category_list)
    return survived_category_list

# <codecell>

def predictSurvivedProbabilityBySex(survived_male_probability,\
                                    survived_female_probability,\
                                    passenger_id_list,\
                                    sex_list):
    sur_pro_sex_list = []
    for i in sex_list:
        if i == 0:
            sur_pro_sex_list.append(survived_male_probability)
        else:
            sur_pro_sex_list.append(survived_female_probability)
    
    sur_pro_id_sex_list = map(None,passenger_id_list,sur_pro_sex_list)  
    return sur_pro_id_sex_list

# <codecell>

def predictSurvivedProbabilityByAge( survived_child_probability,\
                                     survived_juvenile_probability,\
                                     survived_youth_probability,\
                                     survived_middle_age_probability,\
                                     survived_old_people_probability,\
                                     passenger_id_list,\
                                     age_list):

    sur_pro_age_list = []
    
    # child:0——9;   juvenile:10——17   youth:18——34 middle-age:35—59 old-people:60
    for i in age_list:
        if i <= 9:
            sur_pro_age_list.append(survived_child_probability)
        elif i >= 10 and i <= 17:
            sur_pro_age_list.append(survived_juvenile_probability)
        elif i >= 18 and i <= 34:
            sur_pro_age_list.append(survived_youth_probability)
        elif i >= 35 and i <= 59:
            sur_pro_age_list.append(survived_middle_age_probability)
        else :
            sur_pro_age_list.append(survived_old_people_probability)
               
    sur_pro_id_age_list = map(None,passenger_id_list,sur_pro_age_list)
    return sur_pro_id_age_list

# <codecell>

def predictSurvivedProbabilityByFare(survived_third_class_probability,\
                                     survived_second_class_probability,\
                                     survived_first_class_probability,\
                                     passenger_id_list,\
                                     fare_list):

    sur_pro_fare_list = []
    
    # third-class-fare: 0--12 second-class-fare: 13--29 first-class_fare: >=30

    for i in fare_list:
        if i <= 12:
            sur_pro_fare_list.append(survived_third_class_probability)
        elif i >= 13 and i <= 29:
            sur_pro_fare_list.append(survived_second_class_probability)
        else :
            sur_pro_fare_list.append(survived_first_class_probability)
               
    sur_pro_id_fare_list = map(None,passenger_id_list,sur_pro_fare_list)
    return sur_pro_id_fare_list

# <codecell>

def predictSurProByTwoFeatures(passenger_id_list,id_feature_one_list,id_feature_two_list):
    sur_pro_two_features_list = []
    for i in xrange(len(id_feature_one_list)):
        sur_pro_two_features_list.append(id_feature_one_list[i][1]*id_feature_two_list[i][1])
    sur_pro_id_two_features_list = map(None,passenger_id_list,sur_pro_two_features_list)     
    return sur_pro_id_two_features_list

# <codecell>

def flagSurvivivedByOneFeature(passenger_id_feature_list,survived_num):
    passenger_id_survived_list = []
    id_feature_list = passenger_id_feature_list[:]
    id_feature_list.sort(key = lambda x: x[1])
    passenger_id_survived_list \
    = map(lambda x: (x[0],1),id_feature_list[-survived_num:])\
    + map(lambda x: (x[0],0),id_feature_list[:-survived_num])
        
    passenger_id_survived_list.sort(key = lambda x:x[0]) 
    return passenger_id_survived_list

# <codecell>


# <codecell>

def writeFile(file_name,data_list):
    csvfile = file(file_name, 'wb')
    writer = csv.writer(csvfile)
    writer.writerow(['PassengerId','Survived'])
    writer.writerows(data_list)
    csvfile.close()

# <codecell>

train_data_list = readFile(train_data_path)

category_record_list = []
for i in xrange(4):
    category_record_list.append(filterDataByCategory(train_data_list,i+1))
    
survived_category_record_list = []
for i in xrange(3):
    survived_category_record_list.append(mergeCategoryWithSurvived(category_record_list[0],category_record_list[i+1]))

'''
survived-sex:survived_category_record_list[0]
survived-age:survived_category_record_list[1]
survived-fare:survived_category_record_list[2]
'''

# <codecell>

# P(survived)
total_num = len(category_record_list[0]) #891
survived_num = len(filter(lambda x: x == 1,category_record_list[0])) #342
survived_probability = float(survived_num)/total_num #0.383838383838
print "survived_probability:",survived_probability

# <codecell>

# P(survived|male);P(survived|female) 
survived_male_num = len(filter(lambda x: x[0] == 1 and x[1] == 0,survived_category_record_list[0])) #109
survived_female_num = len(filter(lambda x: x[0] == 1 and x[1] == 1,survived_category_record_list[0])) #233

male_num = len(filter(lambda x: x[1] == 0,survived_category_record_list[0]))
female_num = len(filter(lambda x: x[1] == 1,survived_category_record_list[0]))

survived_male_probability = float(survived_male_num)/male_num
survived_female_probability = float(survived_female_num)/female_num 

print "survived_male_probability:",survived_male_probability 
print "survived_female_probability:",survived_female_probability 

# survived_male_probability: 0.188908145581
# survived_female_probability: 0.742038216561

# <codecell>

# P(survived|Age)
# child:0——9;   juvenile:10——17   youth:18——34 middle-age:35—59 old-people:60
survived_child_num = len(filter(lambda x: x[0] == 1 and x[1] >= 0 and x[1] <= 9,survived_category_record_list[1])) #38
survived_juvenile_num = len(filter(lambda x: x[0] == 1 and x[1] >= 10 and x[1] <= 17,survived_category_record_list[1])) #23
survived_youth_num = len(filter(lambda x: x[0] == 1 and x[1] >= 18 and x[1] <= 34,survived_category_record_list[1])) #187
survived_middle_age_num = len(filter(lambda x: x[0] == 1 and x[1] >= 35 and x[1] <= 59,survived_category_record_list[1])) #87
survived_old_people_num = len(filter(lambda x: x[0] == 1 and x[1] >= 60,survived_category_record_list[1])) #7

child_num = len(filter(lambda x: x[1] <= 9,survived_category_record_list[1])) 
juvenile_num = len(filter(lambda x: x[1] >= 10 and x[1] <= 17,survived_category_record_list[1])) 
youth_num = len(filter(lambda x: x[1] >= 18 and x[1] <= 34,survived_category_record_list[1])) 
middle_age_num = len(filter(lambda x: x[1] >= 35 and x[1] <= 59,survived_category_record_list[1])) 
old_people_num = len(filter(lambda x: x[1] >= 60,survived_category_record_list[1])) 

survived_child_probability = float(survived_child_num)/child_num
survived_juvenile_probability = float(survived_juvenile_num)/juvenile_num
survived_youth_probability = float(survived_youth_num)/youth_num
survived_middle_age_probability = float(survived_middle_age_num)/middle_age_num
survived_old_people_probability = float(survived_old_people_num)/old_people_num

'''
survived_child_probability: 0.612903225806
survived_juvenile_probability: 0.450980392157
survived_youth_probability: 0.345018450185
survived_middle_age_probability: 0.414285714286
survived_old_people_probability: 0.269230769231
'''

# <codecell>

# P(survived|Fare)
# third-class-fare: 0--12 second-class-fare: 13--29 first-class_fare: >=30

survived_third_class_num = len(filter(lambda x: x[0] == 1 and x[1] <= 12 ,survived_category_record_list[2]))
survived_second_class_num = len(filter(lambda x: x[0] == 1 and x[1] <= 29 and x[1]>= 13 ,survived_category_record_list[2]))
survived_first_class_num = len(filter(lambda x: x[0] == 1 and x[1] >= 30 ,survived_category_record_list[2]))

third_class_num = len(filter(lambda x: x[1] <= 12 ,survived_category_record_list[2]))
second_class_num = len(filter(lambda x: x[1] <= 29 and x[1]>= 13 ,survived_category_record_list[2]))
first_class_num = len(filter(lambda x: x[1] >= 30 ,survived_category_record_list[2]))

survived_third_class_probalibity = float(survived_third_class_num)/third_class_num
survived_second_class_probalibity = float(survived_second_class_num)/second_class_num
survived_first_class_probalibity = float(survived_first_class_num)/first_class_num

'''
survived_third_class_probalibity: 0.233160621762
survived_second_class_probalibity: 0.418867924528
survived_first_class_probalibity: 0.5875
'''

# <codecell>

test_data_list = readFile(test_data_path)
# [['PassengerId', 'Sex', 'Age', 'Fare'],...]

test_category_record_list = []
for i in xrange(4):
    test_category_record_list.append(filterDataByCategory(test_data_list,i))
    
test_data_num = len(test_category_record_list[0])
survived_num = int(test_data_num * survived_probability)#160

survived_pro_sex_list = predictSurvivedProbabilityBySex(survived_male_probability,\
                                                   survived_female_probability,\
                                                   test_category_record_list[0],\
                                                   test_category_record_list[1])


passenger_id_survived_by_sex_list = flagSurvivivedByOneFeature(survived_pro_sex_list,survived_num)



writeFile('predict_by_sex',passenger_id_survived_by_sex_list)

# <codecell>

survived_pro_age_list = predictSurvivedProbabilityByAge( survived_child_probability,\
                                                         survived_juvenile_probability,\
                                                         survived_youth_probability,\
                                                         survived_middle_age_probability,\
                                                         survived_old_people_probability,\
                                                         test_category_record_list[0],\
                                                         test_category_record_list[2])

passenger_id_survived_by_age_list = flagSurvivivedByOneFeature(survived_pro_age_list,\
                                                               survived_num)

writeFile('predict_by_age',passenger_id_survived_by_age_list)

# <codecell>

survived_pro_fare_list = predictSurvivedProbabilityByFare( survived_third_class_probalibity,\
                                                           survived_second_class_probalibity,\
                                                           survived_first_class_probalibity,\
                                                           test_category_record_list[0],\
                                                           test_category_record_list[3])

passenger_id_survived_by_fare_list = flagSurvivivedByOneFeature(survived_pro_fare_list,\
                                                                survived_num)

writeFile('predict_by_fare',passenger_id_survived_by_fare_list)

# <codecell>

sur_pro_id_sex_age_list = predictSurProByTwoFeatures(test_category_record_list[0],\
                                                     survived_pro_sex_list,\
                                                     survived_pro_age_list)

id_survived_by_sex_age_list = flagSurvivivedByOneFeature(sur_pro_id_sex_age_list,\
                                                         survived_num)
writeFile('predict_by_sex_age',id_survived_by_sex_age_list)

# <codecell>

sur_pro_id_sex_fare_list = predictSurProByTwoFeatures(test_category_record_list[0],\
                                                      survived_pro_sex_list,\
                                                      survived_pro_fare_list)

id_survived_by_sex_fare_list = flagSurvivivedByOneFeature(sur_pro_id_sex_fare_list,\
                                                          survived_num)
writeFile('predict_by_sex_fare',id_survived_by_sex_fare_list)


# <codecell>

sur_pro_id_age_fare_list = predictSurProByTwoFeatures(test_category_record_list[0],\
                                                      survived_pro_age_list,\
                                                      survived_pro_fare_list)

id_survived_by_age_fare_list = flagSurvivivedByOneFeature(sur_pro_id_age_fare_list,\
                                                          survived_num)
writeFile('predict_by_age_fare',id_survived_by_age_fare_list)

# <codecell>

sur_pro_id_sex_age_fare_list = predictSurProByTwoFeatures(test_category_record_list[0],\
                                                          sur_pro_id_age_fare_list,\
                                                          survived_pro_sex_list)

id_survived_by_sex_age_fare_list = flagSurvivivedByOneFeature(sur_pro_id_sex_age_fare_list,\
                                                              survived_num)
writeFile('predict_by_sex_age_fare',id_survived_by_sex_age_fare_list)


# <codecell>


# <codecell>


# <codecell>


