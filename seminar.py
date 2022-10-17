
import pandas as pd
import matplotlib.pyplot as plt
table = pd.read_csv('company_sales_data.csv')
table

months = table['month_number'].tolist()
total_profits = table['total_profit'].tolist()
#months
#total_profits
plt.plot(months,total_profits) 
plt.yticks([100000, 200000, 300000, 400000])
plt.xticks(months)
# yticks([0, 1, 2], ['January', 'February', 'March'],
#        rotation=45)  # Set text labels and properties.

plt.xlabel('months')
plt.ylabel('total_profit')
plt.title('Tend of Sales')

plt.show()


plt.scatter(months, toothpastes, label='sales of toothpastes: хххх year')
# plt.yticks([0, 2000, 4000, 6000, 8000, 10000])
plt.xticks(months)
plt.xlabel('months')
plt.ylabel('total_profit')
plt.title('Tend of Sales')
plt.legend(loc = 2)
plt.grid(color='k', linestyle='--', linewidth=1)
plt.show()
