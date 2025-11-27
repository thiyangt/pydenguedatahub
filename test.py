from pydenguedatahub.datasets import srilanka_weekly_data, india_annual_data

df1 = srilanka_weekly_data()
df2 = india_annual_data()

print(df1.head())
print(df2.head())

