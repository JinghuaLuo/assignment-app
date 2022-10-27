# import packages
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

# show the title
st.title('Titanic APP by Jinghua Luo')

# read csv and show the dataframe
df = pd.read_csv('train.csv')
st.write(df)

# create a figure with three subplots, size should be (15, 5)
# show the box plot for ticket price with different classes
# you need to set the x labels and y labels
# a sample diagram is shown below

fig, ax = plt.subplots(1, 3, figsize=(15, 5))
count = 0
for i, i_df in df.groupby('Pclass').Fare:
    s = pd.Series(i_df)
    s.plot.box(ax=ax[count])
    ax[count].set_xlabel(f'Plcass={i}')
    ax[0].set_ylabel('Fare')
    count = count + 1
st.pyplot(fig)


