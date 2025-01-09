import matplotlib.pyplot as plt
import seaborn as sns

# Task 1
years = [2000, 2005, 2010, 2015, 2020]
population = [6.1, 6.5, 6.9, 7.3, 7.8]  # in billions

plt.plot(population, years)
plt.title("Population Over Time")
plt.xlabel("Labels")
plt.ylabel("Population")
plt.grid(True)
#plt.savefig("population.png", transparent = True)

# Task 2
categories = ["A", "B", "C", "D"]
values = [15, 25, 35, 20]

#sns.barplot()

# Professor Saad's Lecture
s = "saad"
print(s.count('a'))

hydro = ['V','I','L','F','Y','M','A','W','P']
# or hydro = "VILFYMAWP"

def hydro_phob(s):
    total = 0
    for c in hydro:
        total += s.count(c)
    return total / len(s)
    # or return sum( [s.count(c) for c in hydro]) / len(s)


