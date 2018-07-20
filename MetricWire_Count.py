
# coding: utf-8

# In[1]:


import pandas as pd
import os
import glob


# In[2]:


date = input("Please enter the date the CSVs were pulled, e.g. 20180717:  ")

x = glob.glob('Daily Emotion-' + date + '*.csv')
for a in x:
    Emotion = pd.read_csv(str(a))

y = glob.glob('Significant Events-' + date + '*.csv')
for a in y:
    SigEv = pd.read_csv(str(a))

w = glob.glob('Daily Sleep 8am Survey-' + date + '*.csv')
for a in w:
    Sleep8am = pd.read_csv(str(a))

z = glob.glob('ELS Sleep-' + date + '*.csv')
for a in z:
    ElsSleep = pd.read_csv(str(a))


# In[3]:


subject = input("Please enter the MetricWire ID for the subject you wish to check: ")

surveys = Emotion, SigEv, Sleep8am, ElsSleep
print(' ')
print('***********************************************************************************')
print("** Daily Emotion Trigger: 'This survey asks about your emotion throughout the day.'")
print("** Significant Events Trigger: 'Significant Events'" )
print("** Daily Sleep 8 AM Trigger: 'Please answer these few questions about how you slept last night.'")
print("** ELS Sleep Trigger: 'ONCE Trigger'")
print('***********************************************************************************')

for survey in surveys:
    trigger = survey['Trigger Name'].loc[0]
    print(' ')
    print('***********************************************************************************')
    print('Trigger: {}'.format(trigger))
    print('***********************************************************************************')
    print(' ')
    user_subset = survey.loc[survey['User Id'] == subject]
    num_surveys = len(user_subset)
    dates = user_subset['Survey Submitted Date'].to_string()
    print('User {} completed {} surveys on the following days: \n{}'.format(subject, num_surveys, dates))


# In[ ]:
