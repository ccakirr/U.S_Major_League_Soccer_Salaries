import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("mls-salaries-2017.csv",index_col=1)
print("--------dataset control----------")

print("Shape:",df.shape)
print("Columns", df.columns)
print(df.info())
print("--------Salaries----------")
print("Base Salary -> mean:", df["base_salary"].mean(),
      "min:", df["base_salary"].min(),
      "max:", df["base_salary"].max())
print("Guaranteed -> mean:", df["guaranteed_compensation"].mean(),
      "min:", df["guaranteed_compensation"].min(),
      "max:", df["guaranteed_compensation"].max())

df["base_salary"].plot(kind = "hist", bins = 40, title = "Base Salary Distribution")
plt.xlabel("Salary")
plt.show()
df["guaranteed_compensation"].plot(kind = "box",title ="Guaranteed Compensation Boxplot")
plt.show()

salarybyposition = (df.groupby("position")["base_salary"].mean().sort_values(ascending=False))
print(salarybyposition)
salarybyposition.plot(kind = "bar", title = "Base Salary Mean By Position")
plt.show()

salarybyclub = df.groupby("club")["base_salary"].mean().sort_values(ascending=False)
print(salarybyclub)
salarybyclub.plot(kind = "bar", title = "Base Salary Mean By Club")
plt.show()
print("Top 5 clubs:",salarybyclub.head(5))

topTenplayersSalary = df.sort_values("base_salary", ascending=False).head(10)
print(topTenplayersSalary)

corr = df[["base_salary","guaranteed_compensation"]].corr()
df.plot(kind="scatter", x="base_salary", y="guaranteed_compensation")
plt.show()

print(df.groupby("club")["base_salary"].sum().sort_values(ascending=False))
print(df.groupby(["club","position"])["base_salary"].mean().sort_values(ascending=False))