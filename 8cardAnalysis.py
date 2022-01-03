import pandas as pd
import matplotlib.pyplot as plt

# Import data
df = pd.read_csv("8_card_data.csv")

# print average, median, win%, bad_loss%
ave_cards = round(df["0"].mean(), 2)
median_cards = df["0"].median()
print(f"The average is {ave_cards}  and the median is {median_cards}")
# ave: 18.904  median: 16.0

wins = int(df[df["0"] == 52].count())
win_perc = round((100*wins)/int(df.count()), 2)
print(f"There were {wins} wins, which is {win_perc}%")
# 541,422 wins, which is 5.41%

bad_loss = int(df[df["0"] == 8].count())
bad_loss_perc = round((100*bad_loss)/int(df.count()), 2)
print(f"There were {bad_loss} losses without any pairs, which is {bad_loss_perc}%")
# 1,122,186 losses without any pairs, which is 11.22%

# determine at what card the odds of winning are 50%
win_50_quant = int(df.quantile(q=1-(2*win_perc/100))) 
# win_perc is 0.0541, which means the (1 - 0.0541 =) 94.59th quantile is a win - i.e 52 cards
# quantile is area under the curve, so we want 5.41% to be half that area. 
# so 1 - (double the win percent) is the quantile where the odds of winning are 50% 
print(f"Once you reach the {win_50_quant}nd card you have a 50% chance of winning")
# 32nd card



# PLOT
plt.hist(df["0"], bins=45, density=True) # normalized
plt.title("8-card garbage")
plt.xlabel("Cards")
plt.ylabel("Frequency") 
plt.show()