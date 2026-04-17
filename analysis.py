import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["Asha", "Ravi", "Meena", "John", "Sara"],
    "Math": [85, 70, 95, 60, 88],
    "Science": [90, 75, 85, 65, 92],
    "English": [80, 72, 88, 70, 86]
}

df = pd.DataFrame(data)

# Total & Percentage
df["Total"] = df["Math"] + df["Science"] + df["English"]
df["Percentage"] = df["Total"] / 3

# Pass/Fail condition
df["Result"] = df["Percentage"].apply(lambda x: "Pass" if x >= 40 else "Fail")

print("\n📊 Final Student Report:")
print(df)

# Topper
topper = df.loc[df["Total"].idxmax()]
print("\n🏆 Top Performer:")
print(topper)

# Average marks
print("\n📈 Class Average:")
print(df["Percentage"].mean())

# Visualization 1: Total Marks
plt.bar(df["Name"], df["Total"])
plt.title("Student Total Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# Visualization 2: Percentage trend
plt.plot(df["Name"], df["Percentage"], marker="o")
plt.title("Student Percentage Trend")
plt.xlabel("Students")
plt.ylabel("Percentage")
plt.show()
