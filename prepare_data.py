#!/usr/bin/python
#-*-coding:utf-8-*-
import pandas as pd
df = pd.read_csv('Annotated_data_all_na_free_test_train.csv')


dataset_name = 'DCmetro'
sentences = df['incident'] #['Would you like a plain sweater or something else?​', 'Great. We have some very nice wool slacks over here. Would you like to take a look?']
labels = df['Labels'] #['Yes' , 'No' ]
train_or_test_list = df['TrainOrTest'] #['train', 'test']


meta_data_list = []

for i in range(len(sentences)):
    meta = str(i) + '\t' + train_or_test_list[i] + '\t' + labels[i]
    meta_data_list.append(meta)

meta_data_str = '\n'.join(meta_data_list)

f = open('data/' + dataset_name + '.txt', 'w+')
f.write(meta_data_str)
f.close()

corpus_str = '\n'.join(sentences)

f = open('data/corpus/' + dataset_name + '.txt', 'w+')
f.write(corpus_str)
f.close()