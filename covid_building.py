import pandas as pd
import plotly.graph_objs as go
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects


#covid latest 14days infected building info
url='https://www.chp.gov.hk/files/misc/building_list_eng.csv'
df1=pd.read_csv(url)

df1.head()

df1.info()

large_to_small = df1.groupby('District').size().sort_values().index[::-1]


fig, ax = plt.subplots()
fig.set_size_inches(10, 6)
plt.title('No of cases by infected district', fontsize=10)
ax = sns.countplot(x="District", data=df1, palette="Set3", order=large_to_small)
plt.xticks(rotation=45)



str1 = 'Taikoo Shing'
df1['b2']= df1['Building name'].str.upper()
n_cases = df1['b2'].str.count(str1.upper()).sum().astype(str)


fig = plt.figure(figsize=(7, 1))
text = fig.text(0.5, 0.5, n_cases, color='blue',
                          ha='center', va='center', size=20)
text.set_path_effects([path_effects.Stroke(linewidth=3, foreground='black'),
                       path_effects.Normal()])

plt.show()
print(f"No of infected cases under {str1} : {n_cases}")

