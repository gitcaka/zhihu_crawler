import matplotlib.pyplot as plt
import wordcloud
import jieba
import pandas as pd
from matplotlib.image import imread
import numpy as np
from PIL import Image
import re

img = np.array(Image.open("car.png"))
doc_list = [
    "无人驾驶汽车的未来会怎么发展？.txt",
    "无人驾驶的前景，您怎么看？.txt",
    "自动驾驶什么时候才会凉凉，估计还要多久？.txt",
    "自动驾驶就算落地，最多取代司机而已，又能有多大实用价值呢，为啥花那么多钱发展呢？.txt"
]

replace_word = ['一个']

l = []
np = 0
for doc in doc_list:
    with open(doc, 'r', encoding='utf-8') as f:
        print('读取文本：{}'.format(doc))
        paras = f.readlines()
        for para in paras:
            np += 1
            ls = jieba.lcut(para)
            for j in ls:
                # 去除无用字
                if len(j) > 1 and j not in replace_word:
                    l.append(j)
txt = " ".join(l)

# 使用正则表达式去除所有英文单词
txt = re.sub(r'[a-zA-Z]+', '', txt)


print('共{}字'.format(len(txt)))
print('共{}个单词'.format(len(l)))
print('共{}条评论'.format(np))

# 生成词云图
stoplist = list(pd.read_csv('baidu_stopwords.txt',names = ['w'],sep='aaa',encoding = 'utf-8',engine='python').w)
w = wordcloud.WordCloud(font_path="msyh.ttc",width = 1000,height=700,background_color="white",mask=img,scale=16,stopwords=stoplist)

# 加载文本
w.generate(txt)
w.to_file('wordcloud1.png')

# 展示
# out_img = Image.open('wordcloud1.png')
# plt.imshow(out_img)
# plt.axis('off')
# plt.show()

print('结束')