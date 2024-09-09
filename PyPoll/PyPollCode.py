#get dependencies
import pandas as pd
import os
from pathlib import Path

#import and read files and settting destination for file

file = Path('PyPoll/Resources/election_data.csv', encoding="ISO-8859-1")
output_path = Path('PyPoll/Analysis/PyPollAnalysis.txt', encoding="ISO-8859-1")
df = pd.read_csv(file)

#grabbing total number of votes
total_v = df.shape[0]

#writing to the file

out1 = open(output_path, 'w')
out1.write('Election Results\n')
out1.write('\n')
out1.write('-------------------------\n')
out1.write('\n')
out1.write('Total Votes: ' + str(total_v) + '\n')
out1.write('\n')
out1.write('-------------------------\n')
out1.write('\n')
out1.close()

#grabbing the candidates and their vote data adn writing it with the loop 
counts = df['Candidate'].value_counts()
total = counts.sum()

perc = (counts / total) * 100


with open(output_path, 'a') as file:

    for candidate, count, in counts.items():
        percentage = perc[candidate]
        file.write(f'{candidate} {percentage:.3f}% ({count})  \n')
  
        file.write("\n")  

#finds the candidate with the most votes
winner = counts.idxmax()

#writing the rest 
out2 = open(output_path, 'a')
out2.write('\n')
out2.write('-------------------------\n')
out2.write('\n')
out2.write('Winner: ' + winner + '\n')
out2.write('\n')
out2.write('-------------------------\n')
out2.close()