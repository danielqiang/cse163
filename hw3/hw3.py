import cse163_utils  # noqa: F401
# This is a hacky workaround to an unfortunate bug on macs that causes an
# issue with seaborn, the graphing library we want you to use on this
# assignment.  You can just ignore the above line or delete it if you are
# not using a mac!

# Add your imports and code here!
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

sns.set()


def compare_bachelors_1980(df: pd.DataFrame) -> pd.DataFrame:
    """
    Returns a pd.DataFrame object containing the percentage for women vs. men
    who earned a Bachelor's degree in 1980.
    """
    cond = (df['Sex'].isin(['M', 'F']) &
            (df['Year'] == 1980) &
            (df['Min degree'] == "bachelor's"))
    return df[cond][['Sex', 'Total']]


def top_2_2000s(df: pd.DataFrame) -> pd.Series:
    """
    Returns a pd.DataFrame object containing the two most commonly awarded
    degree levels between 2000 and 2010 inclusive. Uses the mean percent
    as the comparator.
    """
    cond = df['Year'].between(2000, 2010) & (df['Sex'] == 'A')
    df['Total'] = df[cond]['Total'].apply(pd.to_numeric)
    df = df[cond][['Min degree', 'Total']].groupby('Min degree').mean()
    return df['Total'].nlargest(n=2)


def percent_change_bachelors_2000s(df: pd.DataFrame, sex: str = 'A') -> float:
    """
    Returns the difference between the total percent
    of Bachelor's degrees received
    in 2000 and 2010 for the sex specified by `sex`.
    """
    cond = (df['Min degree'] == "bachelor's") & (df['Sex'] == sex)
    _2010 = df[cond & (df['Year'] == 2010)]['Total'].squeeze()
    _2000 = df[cond & (df['Year'] == 2000)]['Total'].squeeze()
    return float(_2010) - float(_2000)


def line_plot_bachelors(df: pd.DataFrame) -> None:
    """
    Draws a Seaborn line plot which visualizes the percentage of people
    earning Bachelor's degrees over time. Saves the line plot as an
    image file ('line_plot_bachelors.png').
    """
    df = df[(df['Sex'] == 'A') & (df['Min degree'] == "bachelor's")]
    df = df[['Year', 'Total']].apply(
        pd.to_numeric, errors='coerce').dropna()

    sns.relplot(data=df, x='Year', y='Total', kind='line')
    plt.title("Percentage Earning Bachelor's over time")
    plt.ylabel('Percentage')
    plt.savefig('line_plot_bachelors.png')


def bar_chart_high_school(df: pd.DataFrame) -> None:
    """
    Draws a Seaborn bar plot which visualizes the percentages of women,
    men, and total people with a minimum education of high school degrees
    in 2009. Saves the line plot as an image file ('bar_char_high_school.png').
    """
    df['Total'] = df['Total'].apply(
        pd.to_numeric, errors='coerce').dropna()
    df = df[(df['Min degree'] == 'high school') &
            (df['Year'] == 2009)]

    ax = sns.barplot(x='Sex', y='Total', data=df)
    ax.set_title('Percentage Completed High School By Sex')
    ax.set_ylabel('Percentage')
    plt.savefig('bar_chart_high_school.png')


def plot_hispanic_min_degree(df: pd.DataFrame) -> None:
    """
    Draws a Seaborn line plot which visualizes the percentage of Hispanic
    individuals who earned Bachelor's degrees between 1990 and 2010 inclusive.
    Saves the line plot as an image file ('plot_hispanic_min_degree.png').
    """
    df = df[df['Year'].between(1990, 2010) & (df['Sex'] == 'A')]
    df = df.assign(Total=df['Total'].apply(
        pd.to_numeric, errors='coerce').dropna())
    df = df.loc[
        df['Min degree'].isin(['high school', "bachelor's"]),
        ['Year', 'Min degree', 'Hispanic']
    ]
    df['Hispanic'] = df['Hispanic'].astype(float)
    sns.relplot(x='Year', y='Hispanic',
                hue='Min degree', kind='line', data=df)
    plt.title('Percentage of Degrees '
              'Earned by Hispanic Students')
    plt.ylabel('Percentage')
    plt.savefig('plot_hispanic_min_degree.png')


def fit_and_predict_degrees(df: pd.DataFrame) -> float:
    """
    Returns the test mean squared error of a decision tree
    regressor trained on 80% of the data provided in `df`.
    Labels: 'Total' column in `df`
    Features: ['Year', 'Min degree', 'Sex'] columns in `df`
    """
    df = df[['Year', 'Min degree', 'Sex', 'Total']]
    df = df.assign(Total=df['Total'].apply(
        pd.to_numeric, errors='coerce')).dropna()
    features = pd.get_dummies(df[['Year', 'Min degree', 'Sex']])
    labels = df['Total']
    features_train, features_test, labels_train, labels_test = \
        train_test_split(features, labels, test_size=0.2)
    model = DecisionTreeRegressor()
    model.fit(features_train, labels_train)
    results = model.predict(features_test)
    err = mean_squared_error(labels_test, results)
    return err


def main():
    df = pd.read_csv('hw3-nces-ed-attainment.csv', na_values='---')
    line_plot_bachelors(df)
    bar_chart_high_school(df)
    plot_hispanic_min_degree(df)
    fit_and_predict_degrees(df)


if __name__ == '__main__':
    main()
