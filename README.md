# text_gcn

The implementation of Text GCN for Washington DC Metro Tweets Classification

Liang Yao, Chengsheng Mao, Yuan Luo. "Graph Convolutional Networks for Text Classification." In 33rd AAAI Conference on Artificial Intelligence (AAAI-19), 7370-7377

Follow the following steps:

Edit prepare_data.py to convert your data file to the format required by the model. This python file takes a certain form of data. See 'Annotated_data_all_na_free_test_train.csv'. 


Run following commands in terminal:

1- pip2 uninstall tensorflow -y

2- pip2 install tensorflow==1.4.0

3- python2 prepare_data.py

4- python2 remove_words.py DCmetro

5- python2 build_graph.py DCmetro

6- python2 train.py DCmetro
