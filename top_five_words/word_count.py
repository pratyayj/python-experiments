import string
from collections import OrderedDict
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
file = open("trump.txt", encoding="utf-8")

dictionary = OrderedDict()

for line in file:
    line = line.translate(str.maketrans('','',string.punctuation))
    for word in line.split():
        if word in dictionary:
            count = dictionary.get(word)
            count = count + 1
            dictionary[word] = count
        else:
            dictionary[word] = 1

dictionary = {k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1], reverse=True)}

keys = list(dictionary.keys())
keys = keys[:5]

values = list(dictionary.values())
values = values[:5]

objects = keys
y_pos = np.arange(len(objects))
performance = values

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Count')
plt.title('Trump Inauguration Speech Top 5 Words Count')

plt.show()
