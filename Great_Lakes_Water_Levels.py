# +
# """"
# To use this notebook for your in-class assignment, you will need these 
# files, which you shoujld have downloaded:
# * mhu.csv -- Lake Michigan and Lake Huron
# * sup.csv -- Lake Superior
# * eri.csv -- Lake Erie
# * ont.csv -- Lake Ontario

# As instructed in the in-class activity notebook for today, you are 
# only expected to complete one PART below. Do not worry if your group 
# is not big enough to finish all parts below, but if you have extra 
# time, you're welcome to do so.
# """"

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -


# PART 1
# Using the Michigan/Huron Dataset, plot the Water Level, the second 
# column, as a function of time years

mhu = pd.read_csv('mhu.csv')
plt.plot(mhu['time'], mhu['lake average'])
plt.xlabel('Years')
plt.ylabel('Water Level')

# PART 2
# Using the Superior Dataset, plot the Water Level, the second column, 
# as a function of time years

superior = pd.read_csv("sup.csv")
plt.plot(superior['year'], superior['lake levels'])
plt.xlabel("Year")
plt.ylabel("Lake Superior Water Level")

# PART 3
# Using the Erie Dataset, plot the Water Level, the second column, 
# as a function of time years

# +
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

erie = pd.read_csv('eri.csv')
plt.plot(erie['time'],erie['water level'])
# -

# PART 4
# Using the Ontario Dataset, plot the Water Level, the second column, 
# as a function of time years



# PART 5
# Using the Michigan/Huron and Superior Datasets, plot the 
# Michigan/Hurion Water Level vs Superior Water Level to see if there 
# is any correlation between the water levels.

# +
mhu= pd.read_csv('mhu.csv')
sup= pd.read_csv('sup.csv')

plt.plot(mhu["lake average"], sup["lake levels"])
plt.xlabel("Michigan/Huron Water Level")
plt.ylabel("Superior Water Level")
# -

# PART 6
# Using the Michigan/Hurion and Erie Datasets, plot the 
# Michigan/Huron Water Level vs Erie Water Level to see if there is 
# any correlation between the water levels.
erie = pd.read_csv("eri.csv")
huron = pd.read_csv("mhu.csv")
#plt.plot(erie['time'], erie['water level'], label = 'Erie')
#plt.plot(huron['time'], huron['lake average'], label = 'Huron')
plt.plot(erie['water leve'], huron['lake average'])
plt.legend()
plt.grid()
plt.xlabel("Erie Water Level")
plt.ylabel("Huron Water Level")


# PART 7
# Using the Superior and Ontario Datasets, plot the Superior Water 
# Level vs Ontario Water Level to see if there is any correlation 
# between the water levels.


