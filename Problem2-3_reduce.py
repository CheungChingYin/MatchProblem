#coding:UTF-8
import sys
current_word = None #记录前一个单词， 用于比较
count = 0
word = None
current_count = 0  #每个单词最终的数量

for line in sys.stdin: #切分成行
    line = line.strip()
    word, count = line.split('\t', 1) #key为第一个\t前的值, 只截断一次
    try:
        count = int(count)
    except ValueError:  # count如果不是数字的话，直接忽略掉
        continue
    if current_word == word: #上一个是否和当前的相同
        current_count +=count
    else:
        if current_word:#不相同且不是第一个就输出
            print "%s\t%s" % (current_word, current_count)
        current_count = count
        current_word = word

if word == current_word:  # 不要忘记最后的输出
    print "%s\t%s" % (current_word, current_count)