import csv
import os

file_to_load = os.path.join('/Users','edwardkim','Desktop','DataClass','Election_Analysis','election_results.csv')

with open(file_to_load,'r') as election_data:
    print(election_data)


# name_candidate = []
# total_votes_ccs = ()
# total_votes_ = []
# total_votes_ = []
# complete_total = []
# popular_vote = []
# with open('/Users/edwardkim/Desktop/DataClass/Election_Analysis/election_results.csv','r') as f:
#     line = csv.reader(f,delimiter=',')
#     header = next(line)
#     print('header',header)
#     for row in line:
#         if row[2] == "Charles Casper Stockham":
#             total_votes_ccs += row[0]

#         name_candidate.append([row[2]])
# print(name_candidate)

