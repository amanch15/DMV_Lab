import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("iris.csv")

# Fix column names
df.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]

# Fix spelling issue
df["species"] = df["species"].replace("versincolor", "versicolor")

# Group data
grouped = df.groupby("species").mean()
species_count = df["species"].value_counts()
species_list = df["species"].unique()

# Create subplots (3 rows × 2 columns)
fig, axs = plt.subplots(3, 2, figsize=(12, 12))

# ------------------ 1. BAR CHART ------------------
grouped.plot(kind="bar", ax=axs[0,0])
axs[0,0].set_title("Bar Chart")
axs[0,0].set_xlabel("Species")
axs[0,0].set_ylabel("Average Values")
axs[0,0].grid(axis='y', linestyle='--', linewidth=0.7)

# ------------------ 2. PIE CHART ------------------
axs[0,1].pie(
    species_count,
    labels=species_count.index,
    autopct='%1.1f%%',
    startangle=90,
    wedgeprops={'edgecolor': 'black'}
)
axs[0,1].set_title("Pie Chart")
axs[0,1].grid(True, linestyle='--', linewidth=0.5)

# ------------------ 3. SCATTER PLOT ------------------
for sp in species_list:
    subset = df[df["species"] == sp]
    axs[1,0].scatter(subset["sepal_length"], subset["petal_length"], label=sp)

axs[1,0].set_title("Scatter Plot")
axs[1,0].set_xlabel("Sepal Length")
axs[1,0].set_ylabel("Petal Length")
axs[1,0].legend()
axs[1,0].grid(True, linestyle='--', linewidth=0.5)

# ------------------ 4. LINE CHART ------------------
for sp in species_list:
    subset = df[df["species"] == sp]
    axs[1,1].plot(subset.index, subset["sepal_length"], label=sp)

axs[1,1].set_title("Line Chart")
axs[1,1].set_xlabel("Index")
axs[1,1].set_ylabel("Sepal Length")
axs[1,1].legend()
axs[1,1].grid(True, linestyle='--', linewidth=0.5)

# ------------------ 5. STAIR (STEP) CHART ------------------
for sp in species_list:
    subset = df[df["species"] == sp]
    axs[2,0].step(subset.index, subset["sepal_length"], label=sp)

axs[2,0].set_title("Stair Chart")
axs[2,0].set_xlabel("Index")
axs[2,0].set_ylabel("Sepal Length")
axs[2,0].legend()
axs[2,0].grid(True, linestyle='--', linewidth=0.5)

# Hide empty subplot (bottom right)
axs[2,1].axis('off')

# Adjust layout
plt.tight_layout()
plt.show()