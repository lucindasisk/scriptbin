
# coding: utf-8

# In[45]:


import pandas as pd
import os
from numpy import nan
import glob
from datetime import date
from numpy import nan
today = str(date.today())


# In[2]:


home = '/Volumes/mooddata/ELS_RDoC/MetricWire/Survey Monitoring'
idmaster = pd.read_csv(home + '/Exported Data/ELS Stanford Stress Study-participants.csv')


# In[3]:


print('********')
print('Please make sure that there is only one version of each survey in the MetricWire/Surveys folder. ')
print('Otherwise, the script will pull all versions of that survey and things will get confusing.')
print('********')

x = glob.glob(home + '/Exported Data/Dail*Emotio*.csv')
for a in x:
    Emotion = pd.read_csv(str(a))

y = glob.glob(home + '/Exported Data/Si*Ev*.csv')
for a in y:
    SigEv = pd.read_csv(str(a))

w = glob.glob(home + '/Exported Data/Dail*Sleep*.csv')
for a in w:
    Sleep8am = pd.read_csv(str(a))

z = glob.glob(home + '/Exported Data/ELS*leep*.csv')
for a in z:
    ElsSleep = pd.read_csv(str(a))


# In[29]:


emo = Emotion[['Response Id', 'User Id', 'Survey Submitted Date']]
sigev = SigEv[['Response Id', 'User Id', 'Survey Submitted Date']]
sleep8 = Sleep8am[['Response Id', 'User Id', 'Survey Submitted Date']]
elssl = ElsSleep[['Response Id', 'User Id', 'Survey Submitted Date']]


# In[32]:


#Clean MW and ELS IDs
idmaster['ELS ID'] = idmaster['Name'].str.rstrip(' ELS-T3')
idmaster.rename({'Identifier':'MW ID'}, axis=1, inplace=True)
idmaster.replace('Not yet registered', nan, inplace=True)
ids = idmaster[['ELS ID', 'MW ID','Enrolled']].dropna().reset_index()


# In[34]:


alldf1 = pd.concat([emo,sigev,sleep8,elssl])
alldf1.rename({'User Id':'MW ID'}, axis=1, inplace=True)
alldf1['Date_Submitted'] = pd.to_datetime(alldf1['Survey Submitted Date'], dayfirst=True)
alldf = pd.merge(ids, alldf1, on='MW ID', how='outer').drop(['index'], axis=1)


# In[35]:


subject = input("Please enter the MetricWire ID for the subject you wish to check: ")


# In[48]:


userdf = alldf.groupby(['ELS ID','Date_Submitted','MW ID']).count().reset_index()
subdf = userdf.loc[userdf['ELS ID'] == (subject)].drop(['Survey Submitted Date', 'Enrolled'], axis=1)
subdf.rename({'Response Id':'Response Count'}, axis=1,inplace=True)
subdf.to_csv(home +'/Payment/{}_MetricWire_Completion_'.format(subject)+today+'.csv', index=False)

