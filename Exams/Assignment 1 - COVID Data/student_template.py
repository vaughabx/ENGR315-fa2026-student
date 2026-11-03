import sys

"""
Create a program which will provide answers to the questions posed in the assignment description.
We've provided a function which will parse the NYT covid database file (named "us-counties.csv"); 
however, its correct implementation will be up to you. DO NOT MODIFY THIS FUNCTION.
Your code needs to be successful as well as sufficiently commented/documented to receive full credit.
"""


def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of tuples. Each tuple describes one entry in the source data set.
    Date: the day on which the record was taken in YYYY-MM-DD format
    County: the county name within the State
    State: the US state for the entry
    Cases: the cumulative number of COVID-19 cases reported in that locality
    Deaths: the cumulative number of COVID-19 death in the locality

    :param file_path: Path to data file
    :return: A List of tuples containing (date,county, state, fips, cases, deaths) information

    ____________________ DO NOT MODIFY THIS FUNCTION ___________________
    """
    # data point list
    data=[]

    # open the NYT file path
    try:
        fin = open(file_path)
    except FileNotFoundError:
        print('File ', file_path, ' not found. Exiting!')
        sys.exit(-1)

    # get rid of the headers
    fin.readline()

    # while not done parsing file
    done = False

    # loop and read file
    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        # format is date,county,state,fips,cases,deaths
        (date,county, state, fips, cases, deaths) = line.rstrip().split(",")

        # clean up the data to remove empty entries
        if cases=='':
            cases=0
        if deaths=='':
            deaths=0

        # convert elements into ints
        try:
            entry = (date,county,state, fips, int(cases), int(deaths))
        except ValueError:
            print('Invalid parse of ', entry)

        # place entries as tuple into list
        data.append(entry)


    return data



### Setup ###
import os


### Relative Path Setup ###
relative_path = "../../data/covid/us-counties.csv"

### Test relative path setup ###
if FileExistsError(relative_path):
    print("Can locate covid data")
else:
    print("Cannot locate covid data")

### Create a new list for just Virginia cases ###
covid_data = parse_nyt_data(relative_path)
virginia_cases = [entry for entry in covid_data if entry[2] == "Virginia"]


### Create a new list for Harrisonburg city cases ###
harrisonburg_cases = [entry for entry in virginia_cases if entry[1] == "Harrisonburg city"]


### Create a new list for Rockingham County cases ###
rockingham_cases = [entry for entry in virginia_cases if entry[1] == "Rockingham"]





### Question 1, Part a: When was the first positive COVID case in Harrisonburg? ###

### Make a list of number of cases for each datapoint in the Harrisonburg list ###
harrisonburg_number_of_cases_list = [entry[4] for entry in harrisonburg_cases]
print(harrisonburg_number_of_cases_list)

### Print the first term of the harrisonburg_cases list ###
first_harrisonburg_case_info = harrisonburg_cases[0]
print("First Harrisonburg Case Info",harrisonburg_cases[0])

### Find the specific date from the first case ###
first_harrisonburg_case_date = first_harrisonburg_case_info[0]
print("The first positive COVID case in Harrisonburg was", first_harrisonburg_case_date)




### Question 1, Part b: When was the first positive case in Rockingham County? ###

### Create a list of number of cases in Rockingham County at each datapoint ###
rockingham_number_of_cases_list = [entry[4] for entry in rockingham_cases]
print(rockingham_number_of_cases_list)

### Print the first term of the rockingham_cases list ###
first_rockingham_case_info = rockingham_cases[0]
print("First Rockingham Case Info",rockingham_cases[0])

### Find specific date from the first case ###
first_rockingham_case_date = first_rockingham_case_info[0]
print("The first positive COVID case in Rockingham County was", first_rockingham_case_date)




### Question 2, Part a: On what date was the greatest number of new cases reported in Harrisonburg? ###

### We already created a list of case numbers for Harrisonburg ###
### Create a list of differences from the number of Harrisonburg cases list ###
harrisonburg_new_cases = [harrisonburg_number_of_cases_list[i+1] - harrisonburg_number_of_cases_list[i] for i in range(len(harrisonburg_number_of_cases_list)-1)]
print(harrisonburg_new_cases)

### Find the max of the Harrisonburg new cases list ###
harrisonburg_max_new_cases = max(harrisonburg_new_cases)
print("The max amount of new cases in Harrisonburg in a day is", harrisonburg_max_new_cases)

### locate the max location in the list ###
max_index = harrisonburg_new_cases.index(harrisonburg_max_new_cases)
print("The maximum value of new cases in Harrisonburg occurs at the",max_index, "datapoint of harrisonburg_new_cases")

### Since we know that the new cases list is just a list of terms from the Harrisonburg cases list, The max should occur on the date of the 667 term ###
## Find the 668th term of Harrisonburg cases ###
harrisonburg_max_data_point = harrisonburg_cases[667]
print(harrisonburg_max_data_point)
w = harrisonburg_max_data_point[4]
print("w =",w)

### Double check if it makes sense ###
term_after_harrisonburg_max = harrisonburg_cases[668]
print(term_after_harrisonburg_max)
p = term_after_harrisonburg_max[4]
print("p =",p)

check_harrisonburg_max = [p - w]
print("checked Harrisonburg maximum value =",check_harrisonburg_max)

### Get the date the max increase occured ###
harrisonburg_max_case_increase_date = harrisonburg_max_data_point[0]
print("The maximum amount of cases recorded in Harrisonburg in one day was",harrisonburg_max_new_cases,"new cases on",harrisonburg_max_case_increase_date)




### Question 2, Part b: What date in Rockingham County? ###


### We arleady created a list of number of cases in Rockingham County ###
### Create a list of differences from the number of Harrisonburg cases list ###
rockingham_new_cases = [rockingham_number_of_cases_list[i+1] - rockingham_number_of_cases_list[i] for i in range(len(rockingham_number_of_cases_list)-1)]
print(rockingham_new_cases)

### Find the max of the Harrisonburg new cases list ###
rockingham_max_new_cases = max(rockingham_new_cases)
print("The max amount of new cases in Rockingham in a day is", rockingham_max_new_cases)

### locate the max location in the list ###
rockingham_max_index = rockingham_new_cases.index(rockingham_max_new_cases)
print("The maximum value of new cases in Rockingham occurs at the",rockingham_max_index, "datapoint of rockingham_new_cases")

### Since we know that the new cases list is just a list of terms from the Rockingham cases list, The max should occur on the date of the 665 term ###
## Find the 668th term of Rockingham cases ###
rockingham_max_data_point = rockingham_cases[665]
print(rockingham_max_data_point)
m = rockingham_max_data_point[4]
print("m =",m)

### Double check if it makes sense ###
term_after_rockingham_max = rockingham_cases[666]
print(term_after_rockingham_max)
q = term_after_rockingham_max[4]
print("q =",q)

check_rockingham_max = [q - m]
print("checked Rockingham maximum value =",check_rockingham_max)

### Get the date the max increase occured ###
rockingham_max_case_increase_date = rockingham_max_data_point[0]
print("The maximum amount of cases recorded in Rockingham County in one day was",rockingham_max_new_cases,"new cases on",rockingham_max_case_increase_date)




### Question 3, Part a: What was the worst seven-day period in Harrisonburg city for new COVID cases? (seven-day period when the number of new cases is maximal) ###


### Set the 7 day span ###
span = 7

### Make a list of the weekly sums of new cases in Harrisonburg ###
harrisonburg_weekly_new_cases = [sum(harrisonburg_new_cases[i : i + span])
for i in range(len(harrisonburg_new_cases) - span + 1)]

print(harrisonburg_weekly_new_cases)

### Find the max new cases in one week span ###
harrisonburg_weekly_max = max(harrisonburg_weekly_new_cases)
print(harrisonburg_weekly_max)

### Find out which data point the maximum occurs at ###
harrisonburg_weekly_max_location = harrisonburg_weekly_new_cases.index(harrisonburg_weekly_max)
print(harrisonburg_weekly_max_location)

harrisonburg_week_start_date = harrisonburg_cases[harrisonburg_weekly_max_location][0]
harrisonburg_week_final_date = harrisonburg_cases[harrisonburg_weekly_max_location + span][0]
print("Week start date Harrisonburg", harrisonburg_week_start_date)
print("Week final date Harrisonburg", harrisonburg_week_final_date)



### Question 3, Part b: What period in Rockingham County? (seven-day period when the number of new cases is maximal) ###

### Set the 7 day span ###
span = 7

### Make a list of the weekly sums of new cases in Rockingham County ###
rockingham_weekly_new_cases = [sum(rockingham_new_cases[i : i + span])
for i in range(len(rockingham_new_cases) - span + 1)]

print(rockingham_weekly_new_cases)

### Find the max new cases in one week span ###
rockingham_weekly_max = max(rockingham_weekly_new_cases)
print(rockingham_weekly_max)

### Find out which data point the maximum occurs at ###
rockingham_weekly_max_location = rockingham_weekly_new_cases.index(rockingham_weekly_max)
print(rockingham_weekly_max_location)

rockingham_week_start_date = rockingham_cases[rockingham_weekly_max_location][0]
rockingham_week_final_date = rockingham_cases[rockingham_weekly_max_location + span][0]
print("Week start date Rockingham County", rockingham_week_start_date)
print("Week final date Rockingham County", rockingham_week_final_date)


### Final Answers ####

print("Question 1: The first positive Covid case in Harrisonburg,VA occured on", first_harrisonburg_case_date,". The first positive Covid case in Rockingham County,VA occured on",first_rockingham_case_date,".")
print("Question 2: The greatest number of cases reported in one day in Harrisonburg,VA occured on",harrisonburg_max_case_increase_date,"with a total of",harrisonburg_max_new_cases,"new cases reported in one day. The greatest number of cases reported in one day in Rockingham County, VA occured on",rockingham_max_case_increase_date,"with a total of",rockingham_max_new_cases,"new cases reported in one day.")
print("Question 3: The worst seven-day period in Harrisonburg,VA for new Covid cases occured from",harrisonburg_week_start_date,"to",harrisonburg_week_final_date,"with a total of",harrisonburg_weekly_max,"new cases reported in a seven-day span.The worst seven-day period in Rockingham County,VA for new Covid cases occured from",rockingham_week_start_date,"to",rockingham_week_final_date,"with a total of",rockingham_weekly_max,"new cases reported in a seven-day span.")