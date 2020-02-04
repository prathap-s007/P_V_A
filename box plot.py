import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn
import random
df = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])
seaborn.boxplot(x=None, y=None, hue=None, data=df, order=None, hue_order=None, orient=None, color=None, palette=None, saturation=0.75, width=0.8, dodge=True, fliersize=5, linewidth=None, whis=1.5, notch=False, ax=None)
#df.show()
