
# coding: utf-8

# In[1]:


import pandas as pd
import os


# In[23]:


tracker = pd.read_csv('ELS_RDoc_K01_Scan_Tracker_exclusion.csv')
total_subs = len(tracker)

#Find KidMid Usability
t1_kidmid_us = len(tracker[(tracker.t1_kidmid_usability == 1)
                           & (tracker.t1_dti_usability == 0)
                           & (tracker.t1x_dti_usability == 0)])  
                        
t1x_kidmid_us = len(tracker[(tracker.t1x_kidmid_usability == 1)
                           & (tracker.t1_dti_usability == 0)  
                           & (tracker.t1x_dti_usability == 0)])

tmidx_kidmid_us = len(tracker[(tracker.tmidx_kidmid_usability == 1)
                              & (tracker.tmidx_dti_usability == 0)  
                              & (tracker.tmid_dti_usability == 0)])

tmid_kidmid_us = len(tracker[(tracker.tmid_kidmid_usability == 1)
                             & (tracker.tmidx_dti_usability == 0)  
                             & (tracker.tmid_dti_usability == 0)])

kidmid_total = t1_kidmid_us + t1x_kidmid_us + tmidx_kidmid_us + tmid_kidmid_us

#Find DTI Usability
t1x_dti_us = len(tracker[(tracker.t1x_dti_usability == 1)
                        & (tracker.t1_kidmid_usability == 0)  
                        & (tracker.t1x_kidmid_usability == 0)])

t1_dti_us = len(tracker[(tracker.t1_dti_usability == 1)
                        & (tracker.t1x_kidmid_usability == 0)  
                        & (tracker.t1_kidmid_usability == 0)])

tmid_dti_us = len(tracker[(tracker.tmid_dti_usability == 1)
                           & (tracker.tmid_kidmid_usability == 0)  
                           & (tracker.tmidx_kidmid_usability == 0)])

tmidx_dti_us = len(tracker[(tracker.tmidx_dti_usability == 1)
                            & (tracker.tmid_kidmid_usability == 0)  
                            & (tracker.tmidx_kidmid_usability == 0)])

dti_total = t1x_dti_us + t1_dti_us + tmid_dti_us + tmidx_dti_us


# In[28]:


#Both usable
t1a_us = len(tracker[(tracker.t1_kidmid_usability == 1) 
                    & (tracker.t1_dti_usability == 1)
                    & (tracker.t1x_kidmid_usability == 0) 
                    & (tracker.t1x_dti_usability == 0) 
                    & (tracker.tmid_kidmid_usability == 0) 
                    & (tracker.tmid_dti_usability == 0)
                    & (tracker.tmidx_kidmid_usability == 0) 
                    & (tracker.tmidx_dti_usability == 0)])

t1b_us = len(tracker[(tracker.t1_kidmid_usability == 1) 
                    & (tracker.t1_dti_usability == 0)
                    & (tracker.t1x_kidmid_usability == 0) 
                    & (tracker.t1x_dti_usability == 1) 
                    & (tracker.tmid_kidmid_usability == 0) 
                    & (tracker.tmid_dti_usability == 0)
                    & (tracker.tmidx_kidmid_usability == 0) 
                    & (tracker.tmidx_dti_usability == 0)])
t1_us = t1a_us + t1b_us

t1xa_us = len(tracker[(tracker.t1x_kidmid_usability == 1) 
                     & (tracker.t1x_dti_usability == 1)
                     & (tracker.t1_kidmid_usability == 0) 
                     & (tracker.t1_dti_usability == 0) 
                     & (tracker.tmid_kidmid_usability == 0) 
                     & (tracker.tmid_dti_usability == 0)
                     & (tracker.tmidx_kidmid_usability == 0) 
                     & (tracker.tmidx_dti_usability == 0)])

t1xb_us = len(tracker[(tracker.t1x_kidmid_usability == 1) 
                     & (tracker.t1x_dti_usability == 0)
                     & (tracker.t1_kidmid_usability == 0) 
                     & (tracker.t1_dti_usability == 1) 
                     & (tracker.tmid_kidmid_usability == 0) 
                     & (tracker.tmid_dti_usability == 0)
                     & (tracker.tmidx_kidmid_usability == 0) 
                     & (tracker.tmidx_dti_usability == 0)])
t1x_us = t1xa_us + t1xb_us

tmida_us = len(tracker[(tracker.tmid_kidmid_usability == 1) 
                      & (tracker.tmid_dti_usability == 1)
                      & (tracker.t1_kidmid_usability == 0) 
                      & (tracker.t1_dti_usability == 0) 
                      & (tracker.t1x_kidmid_usability == 0) 
                      & (tracker.t1x_dti_usability == 0)
                      & (tracker.tmidx_kidmid_usability == 0) 
                      & (tracker.tmidx_dti_usability == 0)])

tmidb_us = len(tracker[(tracker.tmid_kidmid_usability == 1) 
                      & (tracker.tmid_dti_usability == 0)
                      & (tracker.t1_kidmid_usability == 0) 
                      & (tracker.t1_dti_usability == 1) 
                      & (tracker.t1x_kidmid_usability == 0) 
                      & (tracker.t1x_dti_usability == 0)
                      & (tracker.tmidx_kidmid_usability == 0) 
                      & (tracker.tmidx_dti_usability == 0)])
tmid_us = tmida_us + tmidb_us

tmidxa_us = len(tracker[(tracker.tmidx_kidmid_usability == 1) 
                       & (tracker.tmidx_dti_usability == 1)
                       & (tracker.t1_kidmid_usability == 0) 
                       & (tracker.t1_dti_usability == 0) 
                       & (tracker.tmid_kidmid_usability == 0) 
                       & (tracker.tmid_dti_usability == 0)
                       & (tracker.t1x_kidmid_usability == 0) 
                       & (tracker.t1x_dti_usability == 0)])

tmidxb_us = len(tracker[(tracker.tmidx_kidmid_usability == 1) 
                       & (tracker.tmidx_dti_usability == 0)
                       & (tracker.t1_kidmid_usability == 0) 
                       & (tracker.t1_dti_usability == 1) 
                       & (tracker.tmid_kidmid_usability == 0) 
                       & (tracker.tmid_dti_usability == 0)
                       & (tracker.t1x_kidmid_usability == 0) 
                       & (tracker.t1x_dti_usability == 0)])
tmidx_us = tmidxa_us + tmidxb_us

tmid_total = tmid_us + tmidx_us
t1_total = t1_us + t1x_us

total_usable = tmid_total + t1_total

subs_with_kidmid = kidmid_total + total_usable
subs_with_dti = dti_total + total_usable


# In[29]:



print('Out of {} subs, {} have kidmid data. {} were excluded because DTI was not usable at T1, T1x, Tmid, or Tmidx. Total: {}'.format(total_subs, subs_with_kidmid, kidmid_total, total_usable))
print('*****')
print('Out of {} subs, {} have DTI data. {} were excluded because kidmid was not usable at T1, T1x, Tmid, or Tmidx. Total: {}'.format(total_subs, subs_with_dti, dti_total, total_usable))
print('*****')
print('{} subs have both usable kidmid and usable dti at T1/T1x only'.format(t1_total))
print('*****')
print('{} subs have both usable kidmid and usable dti at Tmid/Tmidx only'.format(tmid_total))
print('*****')
print('A total of {} unique subs have both usable kidmid and usable dti'.format(total_usable))

