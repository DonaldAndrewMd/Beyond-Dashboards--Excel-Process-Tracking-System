import numpy as np
import pandas as pd
import random

np.random.seed(42)
#Common Number prefixes in Nigeria
prefix=["080","091","090","070",]
people=600
phones=[]

for i in range(people):
        code = np.random.choice(prefix)
#Creating random 8-digit numbers
        randnum = str(random.randint(23456789,98765432))
#Appending the 3-digit prefix to the 8 digits to make 11-digit number
        number=code+randnum
        phones.append([number])

# Creating DataFrame
df = pd.DataFrame(phones, columns=["phone no."])

# Saving to CSV
df.to_csv('Fictitious_Phone_Number.csv', index=False)

