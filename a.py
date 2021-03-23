##https://zhuanlan.zhihu.com/p/106720092
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

text = open("D:\\a.txt",encoding='utf8').read()
text = text.replace('\n',"").replace("\u3000","")
text_cut = jieba.lcut(text)
text_cut = ' '.join(text_cut)
print(text_cut)
stop_words = open("d:\\B.txt",encoding="utf8").read().split("\n")



background = Image.open("D:\\a.png")
graph = np.array(background)

word_cloud = WordCloud(font_path="simsun.ttc",
                       background_color="white",
                       mask=graph, # 指定词云的形状
                       stopwords=stop_words)

word_cloud.generate(text_cut)
plt.subplots(figsize=(12,8))
plt.imshow(word_cloud)
plt.axis("off")
plt.show()

#plt.savefig('D:\\1.jpg',dpi=100)