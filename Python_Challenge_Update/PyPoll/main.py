import os # import os library to generate the path to our csv file
import csv # import csv module to read our csv file

# create/initizlize new variable "election_path"
# assign variable to path module "os.path.join" to read csv file in Resource folder
election_path = os.path.join('Resources', 'election_data.csv')
# create/ initialized new variable "poll_analysis" to hold results of election analysis
poll_analysis = os.path.join('Analysis', 'election_analysis.txt')


# create/initialize empty variables to track polling analysis
total_votes = 0 # integer for votes
can_list = [] # list of candidate names
can_votes = {} # dict - key=candidate name: values=votes
winner = '' # string for winner's name
winning_count = 0 # integer for winner's vote count

# create a scope to read and analyze csv
# open csv file and read each rows, 3 columns and 3521001 rows
with open(election_path) as election_data:
    # create reader object, to view rows and call values by index number
    # if csv had numerous columns,best to use dictionary type = key: column names/ values:columns     
    reader = csv.reader(election_data)
        # Read the header and skip to next row/line
    header = next(reader)

        #first_row = next(reader)
        # create a loop for each row in the reader
        # calculate the following...
    for row in reader:
        
                #run animation 
        print ('. ', end='')
        
        # after each row (vote in this case), add 1 vote to the total vote count
        total_votes = total_votes + 1
        # select candidate name from each row (index 2)
        can_name = row[-1]
            
        # conditional logic - if
        # in the event the candidate's name does not match existing candidate's name 
        if can_name not in can_list:
            # add/append a new list with new candidate's name
            can_list.append(can_name)
            # track new candidate's voter count
            can_votes[can_name] = 0
        # and add one vote to that candidate's count    
        #increment vote count by 1 to that candidate's count
        can_votes[can_name] = can_votes[can_name] + 1
        
# print the results and export the data to our text file 'poll_analysis'
# create a new scope to read and write 'w' analysis
with open(poll_analysis, 'w') as txt_file:

    # use format strings "f'Text type: {variable}" to print final election results (to terminal)
        election_results = (
            f'\n\nElection Results\n'
            f'-------------------------\n'
            f'Total Votes: {total_votes}\n'
            f'-------------------------\n'
            )
        print(election_results, end='')
    
        # save the final vote count to the text file 'poll_anylysis'
        txt_file.write(election_results)

        # create a loop for each row to determine the winner
        for candidate in can_votes:

            # retrieve vote count and percentage
            # use .get method
            votes = can_votes.get(candidate)
            # convert votes into a percentage, use float so number is not rounded but given decimal values
            vote_percentage = float(votes) / float(total_votes) * 100

            # determine winning vote count and candidate
            # conditional logic - if
            # if the current # of votes is more than the winning count
            if (votes > winning_count):
                winning_count = votes
                winner= candidate

                # print each candidate's voter count and percentage (to terminal)
                # use f'strings to print text, .3f is for 3 decimal points spacing
            voter_output = f'{candidate}: {vote_percentage:.3f}% ({votes})\n'
            print(voter_output)

            # Save each candidate's voter count and percentage to text file
            txt_file.write(voter_output)

        # print the winning candidate (to terminal)
        # use f'string to print text
        winning_candidate_summary = (
            f'-------------------------\n'
            f'Winner: {winner}\n'
            f'-------------------------\n'
        )
        print(winning_candidate_summary)

        # Save the winning candidate's name to the text file
        txt_file.write(winning_candidate_summary)
