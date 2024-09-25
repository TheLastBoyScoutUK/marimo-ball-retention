import marimo

__generated_with = "0.8.20"
app = marimo.App(width="medium")


@app.cell
def __():
    import pandas as pd

    # Load the uploaded Excel file to check its contents
    file_path = "./ball_retention.xlsx"
    data = pd.read_excel(file_path)

    # Display the first few rows of the data to understand its structure
    data.head()
    return data, file_path, pd


@app.cell
def __(data):
    # Clean the "Age" column to remove the "yrs" suffix and convert to a numeric value
    data["Age"] = data["Age"].str.replace(" yrs", "").astype(float)

    # Calculate the correlation between Age and % Ball Retention
    correlation = data["Age"].corr(data["% Ball Retention"])

    correlation
    return (correlation,)


@app.cell
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


if __name__ == "__main__":
    app.run()
