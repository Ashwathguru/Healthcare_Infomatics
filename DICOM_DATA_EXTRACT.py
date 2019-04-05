#!/usr/bin/env python
# coding: utf-8

# In[31]:


import pydicom
import dicom
import os
import numpy
from matplotlib import pyplot, cm


# In[47]:


PathDicom = "D:\HI\DCM_DIR"
lstFilesDCM = []  # create an empty list
for dirName, subdirList, fileList in os.walk(PathDicom):
    for filename in fileList:
        if ".dcm" in filename.lower():  # check whether the file's DICOM
            lstFilesDCM.append(os.path.join(filename))
#print(lstFilesDCM)
file = open("DCM_IMAGE_DATA.txt","w")
file.write('##################################'+'\n')
for file_name in lstFilesDCM:
    file.write('########################################################'+'\n')
    file.write('FILE_NAME :'+file_name+'\n')
    g=pydicom.filereader.dcmread("000000.dcm")
    file.write('##############DETAILS####################'+'\n')
    file.write(str(g)+'\n')
    
file.write('#######################################END OF REPORT'+'\n')
file.close()


# In[ ]:




