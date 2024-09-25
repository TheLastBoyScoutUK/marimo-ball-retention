import marimo

__generated_with = "0.8.20"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ## Hypothesis

        The data below is from the the [473rd CIES Football Observatory Weekly Post](https://football-observatory.com/WeeklyPost473) using SkillCorner data to determine the midfielders with the best statistics for keeping the ball in high-pressure for the 2024/25 season .

        A player is considered under pressure when he is in possession of the ball and at least one opponent player nearby him is trying to either recover the ball or limit his options. For each situation, SkillCorner determines the intensity of pressure by considering the speed of the players applying it, their distance to the player in possession and the angle of their movement. More information is available [here](https://skillcorner.crunch.help/en/models-general-concepts/pressure-intensity). 

        **Just by eyeballing the list, it looks like older players tend to be better at ball retention; that is, the older the player, the higher the ball retention %. Let's test this hypothesis.**
        """
    )
    return


@app.cell(hide_code=True)
def __():
    import pandas as pd

    # Load the uploaded Excel file to check its contents
    file_path = "./ball_retention.xlsx"
    data = pd.read_excel(file_path)

    # Display the first few rows of the data to understand its structure
    data.head(100)
    return data, file_path, pd


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ## Steps to Prove or Disprove the Hypothesis:

        1. **Convert Age**: The age column contains a "yrs" suffix, which we'll need to clean up for numerical analysis.

        2. **Statistical Test**: We can compute the correlation between age and ball retention percentage. A positive correlation would support the hypothesis, while a negative or no correlation would challenge it.

        3. **Visualisation**

        The best way to visualise this relationship is through:

        - **Scatter plot**: This will show how ball retention % changes with age.
        - **Trendline**: A line of best fit will help highlight any trends.
        """
    )
    return


@app.cell
def __(data):
    # Clean the "Age" column to remove the "yrs" suffix and convert to a numeric value
    data["Age"] = data["Age"].str.replace(" yrs", "").astype(float)

    # Calculate the correlation between Age and % Ball Retention
    correlation = data["Age"].corr(data["% Ball Retention"])


    # Define a function to classify the strength of the correlation based on the given ranges
    def classify_correlation(correlation):
        correlation = abs(correlation)
        if correlation > 0.70:
            return "Very strong correlation"
        if correlation > 0.50:
            return "Strong correlation"
        if correlation > 0.30:
            return "Moderate correlation"
        if correlation > 0.10:
            return "Weak correlation"
        if correlation >= 0.00:
            return "No or very weak correlation"
        return "Invalid correlation value"
    return classify_correlation, correlation


@app.cell
def __(classify_correlation, correlation, mo):
    mo.md(
        f"""
    The strength of a correlation is typically interpreted based on the magnitude of the correlation coefficient, 
    𝑟
    r, which ranges from -1 to 1. Here’s a general guideline for interpreting the strength of the correlation:

    | **Correlation Range** | **Description**                                              |
    | :-------------------- | :----------------------------------------------------------- |
    | **0.00 to ±0.10**     | No or very weak correlation. The relationship between the two variables is negligible or non-existent. |
    | **±0.10 to ±0.30**    | Weak correlation. There is a slight relationship, but it's not strong. |
    | **±0.30 to ±0.50**    | Moderate correlation. There is a noticeable relationship, but it's not very strong. |
    | **±0.50 to ±0.70**    | Strong correlation. The two variables are significantly related. |
    | **±0.70 to ±1.00**    | Very strong correlation. There is a very strong relationship, with values close to ±1 indicating a near-perfect linear relationship. |

    To indicate a strong correlation, the coefficient would typically need to fall in the range of ±0.50 to ±0.70 or higher. Anything below ±0.30 is usually considered weak

    **{round(correlation, 2)} which is {classify_correlation(correlation).lower()}**

    Visual inspection of a scatter plot (below) further supports this conclusion, as the data points are widely spread, with no obvious upward or downward trend related to age.
        """
    )
    return


@app.cell(hide_code=True)
def __(data):
    # Create a scatter plot with a trendline to visualise the relationship
    import matplotlib.pyplot as plt
    import numpy as np

    plt.figure(figsize=(8, 6))
    plt.scatter(
        data["Age"],
        data["% Ball Retention"],
        color="blue",
        alpha=0.6,
        label="Data Points",
    )

    # Trendline
    z = np.polyfit(data["Age"], data["% Ball Retention"], 1)
    p = np.poly1d(z)
    plt.plot(data["Age"], p(data["Age"]), color="red", label="Trendline")

    plt.title("Relationship Between Age and % Ball Retention")
    plt.xlabel("Age")
    plt.ylabel("% Ball Retention")
    plt.legend()
    plt.grid(True)
    plt.show()
    return np, p, plt, z


@app.cell(hide_code=True)
def __():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
