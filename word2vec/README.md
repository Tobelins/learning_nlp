1) 使用trans_charc.py得到基于字的文本（try.txt)，（如 我 爱 北 京 烤 鸭）或使用popseg.py得到基于词的文本(popseg.txt)（我 爱 北京 烤鸭  。）

python trans_charc.py

2)使用word2vec导出即将使用的词词典，其中分为包含所有词的词典和包含至少出现5次的词典
./word2vec/word2vec -train try.txt -min-count 10 -save-vocab pre_word_vec_10.txt
./word2vec/word2vec -train popseg.txt -min-count 5 -save-vocab pre_word_vec_5.txt

3)把不在字典中的词替换为UNK，因为此处使用pre_word_vec_0.txt，所以此处可忽略
python replace_unk.py  pre_word_vec_10.txt try.txt pos_lines_with_unk.txt

4)训练词向量，目前未去除开头数字
./word2vec/word2vec  -train pos_lines_with_unk.txt -output word_vec.txt -size 150 -window 5 -sample 1e-4 -negative 5 -hs 0 -binary 0  -cbow 0 -iter 3 -min-count 1 -hs 
