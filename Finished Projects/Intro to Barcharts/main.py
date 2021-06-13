import matplotlib.pyplot as plt
import numpy as np

col_count = 3
bar_width = 0.2

korea_scores = (554, 536, 538)
canada_scores = (518, 523, 525)
china_scores = (613, 570, 580)
france_scores = (495, 505, 499)

index = np.arange(col_count)

k1 = plt.bar(index, korea_scores, bar_width, label='Korea', color=(0.3, 0.3, 0.7), alpha=0.4)
c1 = plt.bar(index + bar_width, canada_scores, bar_width, label='Canada', color=(1, 0.4, 0.4), alpha=0.4)
ch1 = plt.bar(index + 2 * bar_width, china_scores, bar_width, label='China', color=(0.4, 1, 0.4), alpha=0.4)
f1 = plt.bar(index + 3 * bar_width, france_scores, bar_width, label='France', color=(0.4, 1, 1), alpha=0.4)


def CreateLabels(data):
	for item in data:
		height = item.get_height()
		plt.text(item.get_x() + item.get_width() / 2.0, height * 1.05, '%d' % int(height), ha='center', va='bottom')


CreateLabels(k1)
CreateLabels(c1)
CreateLabels(ch1)
CreateLabels(f1)

plt.ylabel('Mean Score in PISA 2012')
plt.xlabel('Subjects')
plt.title('Test Scores by Country')

plt.xticks(index + 0.3 / 2, ('Math', 'Reading', 'Science'))
plt.grid(True)
plt.legend(frameon=False, loc=2, bbox_to_anchor=(1, 1))
plt.show()
