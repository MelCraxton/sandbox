from random import randint
import plotly.express as px

class Die:

    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)
    

die1 = Die()
die2 = Die()

results = []

for roll_num in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)

frequencies = []
max_results = die1.num_sides + die2.num_sides
poss_results = range(2, max_results + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)


print(frequencies)

title = "Possible results of a rolling two dice"
labels = {'x': "Result", 'y': "Frequency of Result"}
fig=px.bar(x=poss_results, y=frequencies, title=title, labels = labels)
fig.update_layout(xaxis_dtick=1)
fig.show()
fig.write_html('dice_visual.html')