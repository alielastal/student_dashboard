# scripts/eda.py
import matplotlib.pyplot as plt
import seaborn as sns

def plot_distributions(df):
    """Exam score distribution chart"""
    sns.histplot(df['exam_score'], kde=True, bins=20)
    plt.title("Final exam grade distribution")
    plt.xlabel("Exam score")
    plt.ylabel("Number of students")
    plt.tight_layout()
    plt.show()

def plot_scatter(df):
    """Drawing the relationship between study hours and exam grade"""
    sns.scatterplot(x='hours_studied', y='exam_score', data=df)
    plt.title("The relationship between study hours and exam grade")
    plt.tight_layout()
    plt.show()

def plot_heatmap(df):
    """Draw a correlation matrix"""
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Correlation matrix between variables")
    plt.tight_layout()
    plt.show()