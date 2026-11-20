"""
CULMINATING ASSIGNMENT 2: RSI

Create a program which will provide answers to the tasks posed in the assignment description.

For this assignment, you will start from scratch with this blank template.
It is your reponsibility to include all necessary program components in this file.
Your code needs to be successful as well as sufficiently commented/documented to receive full credit.

The relevant data file is named "all_participant_data_rsi.csv" and is located in data > drop-jump.

All file paths need to be relative and execute from this file's directory;
the Visual Studio Code setting "Python > Terminal: Execute in File Dir" 
must be enabled in File > Preferences > Settings.

See Canvas for additional requirements.
"""
### Setup ###
### Relative Path Setup ###
relative_path = "../../data/drop-jump/all_participant_data_rsi.csv"

### Test Relative Path Setup ###
if FileExistsError(relative_path):
    print("Can locate drop-jump data")
else:
    print("Cannot locate drop-jump data")

### Import Required Libraries ###
import numpy as np
from scipy import stats
from scipy.stats import norm, expon
import matplotlib
import matplotlib.pyplot as plt
import platform
import pandas as pd

### Task 1: For the new dataset of RSI values (all_participant_data_rsi.csv), ###
### conduct a paired t-test comparing all the force plate and accelerometer RSI values. ###
### Cleary report the t-value, p-value, null and alternative hypotheses, ###
### and decide whether the null hypothesis can be rejected or not ###

### Conduct a paired t-test comparing all the force plate and accelerometer RSI values ###
w = pd.read_csv(relative_path)
t_statistic, p_value = stats.ttest_rel(w['force_plate_rsi'], w['accelerometer_rsi'])

### display the t-value and p-value ###
print(f"t-statistic: {t_statistic}")
print(f"p-value: {p_value}")

### Test with the alpha value of 0.05 ###
alpha = 0.05
if p_value < alpha:
    print("significant difference between the two groups, reject the null hypothesis")
else:
    print("no significant difference between the two groups, fail to reject the null hypothesis")

### Task 2: For the RSI values gathered using an accelerometer, ###
### fit a normal distribution and conduct a CHI2 goodness of fit test. ###
### Clearly print out the chi2 stat, p-value, and indication of whether its a good fit or not. ###
### Plot a histogram of the accelerometer data with the normal distribution curve overlaid. ###

### Get a list of the accelerometer RSI values ###
accelerometer_rsi = w['accelerometer_rsi'].values
print(f"Accelerometer RSI values: {accelerometer_rsi}")

def fit_normal(accelerometer_rsi):
    """
    Fit samples to a normal distribution
    :param accelerometer_rsi: A numpy array of samples
    :return: A tuple (mean, standard deviation) of the fitted normal distribution
    """
    fitted_mean = norm.fit(accelerometer_rsi)[0]
    fitted_std = norm.fit(accelerometer_rsi)[1]
    return fitted_mean, fitted_std

fitted_mean, fitted_std = fit_normal(accelerometer_rsi)
print("Fitted mean =", fitted_mean, "Fitted std =", fitted_std)

### Plot the normal distribution ###
x = np.linspace(start=-2, stop=2, num=31)
plt.plot(x, norm.pdf(x, loc=fitted_mean, scale=fitted_std), label='Fitted Normal')
plt.title('Fitted Normal Distribution for RSI of Accelerometer')
plt.xlabel('X')
plt.ylabel('RSI')
plt.legend()
plt.show()

### Conduct a CHI2 Goodness of Fit Test ###
chi_stat, chi_p_value = stats.chisquare(accelerometer_rsi)
print("Chi2 = ", chi_stat)
print("p-value = ", chi_p_value)

if chi_p_value < alpha:
    print("Reject the null hypothesis, the data does not fit a normal distribution")
else:
    print("Fail to reject the null hypothesis, the data fits a normal distribution")

### Plot a histogram of the accelerometer data with the normal distribution curve overlaid ###
plt.hist(accelerometer_rsi, bins=10, density=True, alpha=0.3, color='green', label='Histogram of RSI')
plt.plot(x, norm.pdf(x, loc=fitted_mean, scale=fitted_std), label='Fitted Normal')
plt.title('Fitted Normal Distribution for RSI of Accelerometer')
plt.xlabel('X')
plt.ylabel('RSI')
plt.legend()
plt.show()

### Task 3: From the force plate and accerlerometer-based RSI data for all participants, ###
### create and print() a dataframe containing only the trials from Participant 'F'. ###
### Calculate the 95% confidence intervals for Participant F's RSI for both the force plate and accelerometer measurements. ###

### Create a dataframe containing only the trials from Participant 'F' ###
participant_f_data = w[(w['trial'] == 'F_trial_1') | (w['trial'] == 'F_trial_2') | (w['trial'] == 'F_trial_3') | (w['trial'] == 'F_trial_4') | (w['trial'] == 'F_trial_5') | (w['trial'] == 'F_trial_6') | (w['trial'] == 'F_trial_7') | (w['trial'] == 'F_trial_8') | (w['trial'] == 'F_trial_9') | (w['trial'] == 'F_trial_10')]
print("Participant F's Data:")
print(participant_f_data)

### Calculate the 95% confidence intervals for Participant F's RSI for both the force plate and accelerometer measurements ###
def confidence_interval(participant_f_data, confidence=0.95):
    """
    Calculate the confidence interval for a given dataset
    :param participant_f_data: A numpy array of samples for Participant F
    :param confidence: The desired confidence level (default is 0.95)
    :return: A tuple (lower_bound, upper_bound) of the confidence interval
    """
    n = len(participant_f_data)
    mean = np.mean(participant_f_data)
    std_err = stats.sem(participant_f_data)
    h = std_err * stats.t.ppf((1 + confidence) / 2, n - 1)
    return float(mean - h), float(mean + h)

print("95% Confidence Interval for Force Plate RSI:", confidence_interval(participant_f_data['force_plate_rsi']))
print("95% Confidence Interval for Accelerometer RSI:", confidence_interval(participant_f_data['accelerometer_rsi']))

### Finished with testing ###
print("Project Complete!")