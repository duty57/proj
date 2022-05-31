from matplotlib import pyplot as plt
import main

plt.plot(main.years, main.it_pop, color='red')
plt.fill_between(main.years, main.it_pop, 0)

plt.show()