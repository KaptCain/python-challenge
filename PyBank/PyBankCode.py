#import dependencies
import pandas as pd
import os
from pathlib import Path

#importing and reading the file
file = Path('PyBank/Resources/budget_data.csv', encoding="ISO-8859-1")
output_path = Path('PyBank/Analysis/PyBankAnalysis.txt', encoding="ISO-8859-1")
df = pd.read_csv(file)


#counting up the number of months 
month_count = df['Date'].nunique()

#getting the net amount of all the profits and losses

net_amount = df['Profit/Losses'].sum()

#getting the changes over the entire period

rev_change = df['Profit/Losses'].diff()

#getting the average of those changes and rounding it to the second decimal place to reflect money

rev_avg = rev_change.mean()
rev_avg = round(rev_avg,2)

#grabbing greatest increase in profits

max_chng = df['Profit/Losses'].diff()
rev_max = max_chng.max()

#taking the unnecessary decimal off 
rev_max = int(rev_max)

#grabbing index of the max change to grab the date

rev_max_ndx = max_chng.idxmax()
mx_date = df['Date'].iloc[rev_max_ndx]

#grabbing the gretaest decrease in profits
min_chng = df['Profit/Losses'].diff()
rev_min = min_chng.min()

#taking the unnecessary decimal off 
rev_min = int(rev_min)


#grabbing the index of the minimum change to get the date
rev_min_ndx = min_chng.idxmin()
min_date = df['Date'].iloc[rev_min_ndx]


#creating a file to output to
output = open(output_path, 'w')
output.write('Finacial Analysis\n')
output.write('\n')
output.write('----------------------------\n')
output.write('\n')
output.write('Total Months: ' + str(month_count) + '\n')
output.write('\n')
output.write('Total: $' + str(net_amount) + '\n')
output.write('\n')
output.write('Average Change: $' + str(rev_avg) + '\n')
output.write('\n')
output.write('Greatest Increase in Profits: ' + str(mx_date) +' ($' + str(rev_max) + ')\n')
output.write('\n')
output.write('Greatest Decrease in Profits: ' + str(min_date) + ' ($' + str(rev_min) + ')\n')
output.write('\n')
output.close()




