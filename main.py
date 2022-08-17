import pandas as pn

#First delivery-----------------------------------------------------------------------------------#
medellin = pn.read_csv('MedellinSH.csv', sep=';')
medellin.harassmentRisk = medellin.harassmentRisk.fillna(medellin.harassmentRisk.mean())
print(medellin.harassmentRisk)
#-------------------------------------------------------------------------------------------------#                             