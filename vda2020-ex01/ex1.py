# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 00:07:39 2020

@author: anirbanhp
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="darkgrid")

tips = sns.load_dataset("tips")
fmri = sns.load_dataset("fmri")
print(fmri)
#sns.relplot(x="total_bill", y="tip", data=tips)
#sns.relplot(x="total_bill", y="tip", hue="smoker", style="size", data=tips)
#sns.relplot(x="total_bill", y="tip", hue="size", palette="ch:r=-.5,l=.8", size="size", data=tips)

#1.Are there days of the week on which the dataset covers only one meal, i.e., either lunch or dinner?
sns.relplot(x="day", y="time",  data=tips)

#2.Was the highest tip given by a man or a woman?
sns.relplot(x="sex", y="tip", hue="total_bill", data=tips)

#3. Was the highest tip given for the highest total bill?
sns.relplot(x="total_bill", y="tip", hue="total_bill", palette="ch:r=-.1,l=.8" , data=tips)


