# DATA EXPLORATION FILE
# https://fivethirtyeight.com/features/the-riddler-just-had-to-go-and-reinvent-beer-pong/

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# setup
sns.set(style='whitegrid')

# import data
data = pd.read_csv('data.csv')

# plot
fig, (ax1, ax2) = plt.subplots(nrows=2, sharex=True)
plot1 = sns.scatterplot(x = 'NUM_CUPS', y = 'NUM_BALLS', data=data, ax=ax1)
plot1.set_title('Mean number of balls thrown, 10k reps')
plot2 = sns.scatterplot(x = 'NUM_CUPS', y = 'NUM_ROUNDS', data=data, ax=ax2)
plot2.set_title('Mean number of rounds completed, 10k reps')
plt.show()
