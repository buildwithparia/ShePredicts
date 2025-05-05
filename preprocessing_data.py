''' N.B. 1: just a little reminder! before entering training the model era, convert all those y/n values to 1/0 
it can make your life easier when you try train your model!
most algorithms work better with numerical value...do don't risk it
I was lucky all those y/n rows have 1/0 values by default! yay! '''


'''N.B. 2: I wasn't that lucky...after double checking the dataset I saw the Cycle(R/I) column use weird 
values: 2 & 4 instead of 0/1 or R/I...so it need to be fixed...always double check...🤨'''

import pandas as pd

df = pd.read_csv("PCOS_selected_features.csv")
df['Cycle(R/I)'].replace({2: 0, 4: 1}, inplace=True)

df.to_csv("PCOS_final_dataset.csv", index=False)
print( "I promise your final dataset is ready🧐")




