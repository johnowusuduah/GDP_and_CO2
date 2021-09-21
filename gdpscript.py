import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv(
    "https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv"
)

# data.head()

data1 = data.loc[
    :,
    [
        "Mortality rate, infant (per 1,000 live births)",
        "GDP per capita (constant 2010 US$)",
        "Country Name",
        "",
    ],
]


plt.scatter(
    data=data1,
    x="GDP per capita (constant 2010 US$)",
    y="Mortality rate, infant (per 1,000 live births)",
)
plt.title("Mortality vs GDP")
plt.style.use("ggplot")
plt.xlabel("GDP")
plt.ylabel("Mortality")
plt.show()
