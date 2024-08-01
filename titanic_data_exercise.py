import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


titanic_data = pd.read_csv('titanic.csv')


survival_rate_by_gender = titanic_data.groupby('Sex')['Survived'].mean()


print(survival_rate_by_gender)


sns.barplot(x=survival_rate_by_gender.index, y=survival_rate_by_gender.values)
plt.title('Survival Rate by Gender')
plt.ylabel('Survival Rate')
plt.xlabel('Gender')
plt.show()
