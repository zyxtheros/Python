import matplotlib.pyplot as plt
import pandas as pd

raw_data = {'names': ['Nick', 'Panda', 'S', 'Ari', 'Valos'],
			'jan_ir': [143, 122, 101, 108, 365],
			'feb_ir': [122, 132, 144, 98, 62],
			'mar_ir': [65, 88, 12, 32, 65]
			}

df = pd.DataFrame(raw_data, columns=['names', 'jan_ir', 'feb_ir', 'mar_ir'])

df['total_ir'] = df['jan_ir'] + df['feb_ir'] + df['mar_ir']

print(df)

color = [(1, .04, 0.4), (1, 0.6, 1), (0.5, 0.3, 1), (0.3, 1, 0.5), (0.7, 0.7, 0.2)]

plt.pie(df['total_ir'],
		labels=df['names'],
		colors=color,
		autopct='%1.1f%%')

plt.axis('equal')

plt.show()