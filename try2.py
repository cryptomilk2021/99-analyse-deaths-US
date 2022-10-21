#works with 4


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy


df = pd.read_csv('sample1.csv', encoding="windows-1252")
#
# df = df_fatalities['age']
# df = df.to_frame()




# df = pd.DataFrame(np.random.randn(1000, 4)).add_prefix('C')
print(df)
k = len(df.columns)
n = 2
m = (k - 1) // n + 1
fig, axes = plt.subplots(m, n, figsize=(n * 5, m * 3))
for i, (name, col) in enumerate(df.iteritems()):
    r, c = i // n, i % n
    ax = axes[r, c]
    col.hist(ax=ax)
    ax2 = col.plot.kde(ax=ax, secondary_y=True, title=name)
    ax2.set_ylim(0)

fig.tight_layout()

plt.show()