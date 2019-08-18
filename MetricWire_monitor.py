
# coding: utf-8

# In[18]:


import pandas as pd
import os
import glob
from datetime import date, timedelta
import time
from numpy import nan
today = str(date.today())


# In[19]:


home='/Volumes/mooddata/ELS_RDoC/MetricWire/Survey Monitoring'
idmaster = pd.read_csv(home + '/Exported Data/ELS Stanford Stress Study-participants.csv')
    
x = glob.glob(home +'/Exported Data/Dail*Emotio*.csv')
for a in x:
    Emotion = pd.read_csv(str(a))
    Emotion['Survey_Emotion'] ='Emotion'
y = glob.glob(home +'/Exported Data/Si*Ev*.csv')
for a in y:
    SigEv = pd.read_csv(str(a))
    SigEv['Survey_SigEv'] = 'Signif. Events'
w = glob.glob(home +'/Exported Data/Dail*Sleep*.csv')
for a in w:
    Sleep8am = pd.read_csv(str(a))
    Sleep8am['Survey_Sleep8AM']='Sleep8AM'
z = glob.glob(home +'/Exported Data/ELS*leep*.csv')
for a in z:
    ElsSleep = pd.read_csv(str(a))
    ElsSleep['Survey_ELSSleep'] = 'ELS Sleep'


# In[20]:


#Clean MW and ELS IDs
idmaster['ELS ID'] = idmaster['Name'].str.rstrip(' ELS-T3')
idmaster.rename({'Identifier':'MW ID'}, axis=1, inplace=True)
idmaster.replace('Not yet registered', nan, inplace=True)
ids = idmaster[['ELS ID', 'MW ID','Enrolled']].dropna().reset_index()


# In[21]:


emo = Emotion[['Response Id', 'User Id', 'Survey Submitted Date','Survey_Emotion']]
sigev = SigEv[['Response Id', 'User Id', 'Survey Submitted Date', 'Survey_SigEv']]
sleep8 = Sleep8am[['Response Id', 'User Id', 'Survey Submitted Date', 'Survey_Sleep8AM']]  
elssl = ElsSleep[['Response Id', 'User Id', 'Survey Submitted Date', 'Survey_ELSSleep']]

alldf1 = pd.concat([emo,sigev,sleep8,elssl])
alldf1['Submit_Date'] = pd.to_datetime(alldf1['Survey Submitted Date'], dayfirst=True)
alldf = alldf1.rename(columns={'User Id':'MW ID', 'Response Id': 'Num_Responses'}).groupby('MW ID').count().reset_index()   
finaldf = pd.merge(ids,alldf, on='MW ID', how = 'outer').drop('index', axis=1)


# In[22]:


users = finaldf['MW ID']


# In[23]:


#Get date of earliest submission

start = []
end = []
def get_start_date(user, df):
    userdf1 = df.loc[df['User Id'] == user].sort_values(by='Submit_Date', ascending=True)
    try:
        date1 = userdf1.iloc[0,1]
        startinf = [user, date1]
        start.append(startinf)
    except:
        print('Could not index {}.'.format(user))
    userdf2 = df.loc[df['User Id'] == user].sort_values(by='Submit_Date', ascending=False)
    try:
        date2 = userdf2.iloc[0,1]
        endinf = [user, date2]
        end.append(endinf)
    except:
         print(' ')


# In[24]:


for user in users:
    get_start_date(user, alldf1)


# In[25]:


#Create df and column for start of surveys
sdf = pd.DataFrame(start, columns=['MW ID', 'First_Survey'])
sdf['First Survey'] = pd.to_datetime(sdf['First_Survey'], dayfirst=True)

#Create df and column for end of surveys
edf = pd.DataFrame(end, columns=['MW ID', 'Last_Survey'])
edf['Last Survey'] = pd.to_datetime(edf['Last_Survey'], dayfirst=True)

#Merge start & end columns
startend = pd.merge(sdf, edf, on='MW ID', how = 'outer').drop(['First_Survey', 'Last_Survey'], axis=1)  

#Add to final df
final1 = pd.merge(finaldf, startend, on='MW ID', how = 'outer').drop(['Survey Submitted Date', 'Submit_Date'], axis=1)

#Convert enrolled date to DT, count days since enrolled
final1['Enrolled DT'] = pd.to_datetime(final1['Enrolled'], dayfirst=True)
final1['Days Since Enrolled'] = (date.today()-final1['Enrolled DT'])
final = final1.drop('Enrolled', axis=1)
final.sort_values(by='Enrolled DT', ascending = False, inplace=True)

#Write to CSV
final.to_csv(home+'/Monitoring/MetricWire_Monitoring_'+today+'.csv', index=False)


