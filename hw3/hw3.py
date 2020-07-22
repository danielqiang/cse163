# This is a hacky workaround to an unfortunate bug on macs that causes an
# issue with seaborn, the graphing library we want you to use on this
# assignment.  You can just ignore the above line or delete it if you are
# not using a mac!

# Add your imports and code here!
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style='ticks')


def compare_bachelors_1980(df: pd.DataFrame) -> pd.DataFrame:
    cond = (df['Sex'].isin(['M', 'F']) &
            (df['Year'] == 1980) &
            (df['Min degree'] == "bachelor's"))
    return df[cond][['Sex', 'Total']]


def top_2_2000s(df: pd.DataFrame) -> pd.Series:
    cond = df['Year'].between(2000, 2010) & (df['Sex'] == 'A')
    df['Total'] = df[cond]['Total'].apply(pd.to_numeric)
    df = df[cond][['Min degree', 'Total']].groupby('Min degree').mean()
    return df['Total'].nlargest(n=2)


def percent_change_bachelors_2000s(df: pd.DataFrame, sex: str = 'A') -> float:
    cond = (df['Min degree'] == "bachelor's") & (df['Sex'] == sex)
    _2010 = df[cond & (df['Year'] == 2010)]['Total']
    _2000 = df[cond & (df['Year'] == 2000)]['Total']
    return float(_2010.squeeze()) - float(_2000.squeeze())


def line_plot_bachelors(df: pd.DataFrame) -> None:
    df = df[df['Sex'] == 'A'][['Year', 'Total']]
    df['Total'] = df['Total'].apply(pd.to_numeric, errors='coerce')
    print(df)
    g = sns.relplot(data=df)
    g.set_xlabels('Year')
    g.set_ylabels('Percentage')
    g.set_titles('Percentage Change over time')

    plt.show()


def main():
    df = pd.read_csv('hw3-nces-ed-attainment.csv')
    line_plot_bachelors(df)


if __name__ == '__main__':
    main()
