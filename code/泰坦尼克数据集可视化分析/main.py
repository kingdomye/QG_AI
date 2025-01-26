import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class TitanicData:
    def __init__(self):
        self.file = "./titanic_data/train.csv"
        self.df = pd.read_csv(self.file)

    def describe(self):
        print(self.df.describe())

    def all_survival_rate(self):
        n = self.df.Survived.value_counts()
        plt.figure(figsize=(6, 6))
        plt.pie(n, autopct='%.2f%%', labels=['death', 'survival'], pctdistance=0.4, labeldistance=0.6,
                shadow=True, explode=[0, 0.1], textprops=dict(size=15))
        plt.title('all_survival_rate')
        plt.Text(0.5, 1.0, 'all_survival_rate')
        plt.show()

    def sex_survival_rate(self):
        sex_count = self.df.groupby(by='Sex')['Survived'].value_counts()
        plt.figure(figsize=(2 * 5, 5))

        axes1 = plt.subplot(1, 2, 1)
        axes1.pie(sex_count.loc['female'][::-1], autopct='%.2f%%', labels=['death', 'survival'], pctdistance=0.4,
                  labeldistance=0.6,
                  shadow=True, explode=[0, 0.1], textprops=dict(size=15), colors=['#9400D3', '#FFB6C1'], startangle=90)
        axes1.set_title('female survival rate')

        axes2 = plt.subplot(1, 2, 2)
        axes2.pie(sex_count.loc['male'], autopct='%.2f%%', labels=['death', 'survival'], pctdistance=0.4, labeldistance=0.6,
                  shadow=True, explode=[0, 0.1], textprops=dict(size=15), colors=['#2E8B57', '#AFEEEE'])
        axes2.set_title('male survival rate')
        plt.Text(0.5, 1.0, 'male survival rate')
        plt.show()

    def age_survival_rate(self):
        age_range = self.df['Age']
        age_num, _ = np.histogram(age_range, range=(0, 80), bins=16)

        age_survived = []
        for age in range(5, 81, 5):
            survived_num = self.df.loc[(age_range >= age - 5) & (age_range <= age)]['Survived'].sum()
            age_survived.append(survived_num)

        plt.figure(figsize=(12, 6))
        plt.bar(np.arange(2, 78, 5) + 0.5, age_num, width=5, label='all people', alpha=0.8)
        plt.bar(np.arange(2, 78, 5) + 0.5, age_survived, width=5, label='survived people')
        plt.xticks(range(0, 81, 5))
        plt.yticks(range(0, 121, 10))
        plt.xlabel('age', position=(0.95, 0), fontsize=15)
        plt.ylabel('counts', position=(0, 0.95), fontsize=15)
        plt.title('age survival rate')
        plt.grid(True, linestyle=':', alpha=0.6)
        plt.legend()
        plt.show()


if __name__ == '__main__':
    titanic = TitanicData()
    titanic.age_survival_rate()
