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
# E-mail:           zhmi120@sina.com
# Create:           2016-1-24
# Recent-changes:   2016-1-24

# <codecell>

import string
import math

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
    #category_list = map(lambda x: float(x),category_list[1:])
    category_list = map(lambda x: int(math.floor(float(x))),category_list[1:])
    return category_list

# <codecell>

def mergeCategoryWithSurvived(survived_list,category_list):
    survived_category_list = map(None,survived_list,category_list)
    return survived_category_list

# <codecell>

configVariables()
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
survived_male_probability = float(survived_male_num)/survived_num
survived_female_probability = float(survived_female_num)/survived_num

print "survived_male_probability:",survived_male_probability #0.318713450292
print "survived_female_probability:",survived_female_probability #0.681286549708

# <codecell>

# P(survived|Age)
# child:0——9;   juvenile:10——17   youth:18——34 middle-age:35—59 old-people:60
survived_child_num = len(filter(lambda x: x[0] == 1 and x[1] >= 0 and x[1] <= 9,survived_category_record_list[1])) #38
survived_juvenile_num = len(filter(lambda x: x[0] == 1 and x[1] >= 10 and x[1] <= 17,survived_category_record_list[1])) #23
survived_youth_num = len(filter(lambda x: x[0] == 1 and x[1] >= 18 and x[1] <= 34,survived_category_record_list[1])) #187
survived_middle_age_num = len(filter(lambda x: x[0] == 1 and x[1] >= 35 and x[1] <= 59,survived_category_record_list[1])) #87
survived_old_people_num = len(filter(lambda x: x[0] == 1 and x[1] >= 60,survived_category_record_list[1])) #7

survived_child_probability = float(survived_child_num)/survived_num
survived_juvenile_probability = float(survived_juvenile_num)/survived_num
survived_youth_probability = float(survived_youth_num)/survived_num
survived_middle_age_probability = float(survived_middle_age_num)/survived_num
survived_old_people_probability = float(survived_old_people_num)/survived_num


print "survived_child_probability:",survived_child_probability
print "survived_juvenile_probability:",survived_juvenile_probability
print "survived_youth_probability:",survived_youth_probability
print "survived_middle_age_probability:",survived_middle_age_probability
print "survived_old_people_probability:",survived_old_people_probability

# <codecell>

# P(survived|Fare)

# <codecell>


# <codecell>




# <codecell>


