#!/usr/bin/env python
# coding: utf-8

# In[1]:


from spmf import Spmf
import pandas as pd
from gspan_mining.config import parser
from gspan_mining.main import main


# In[2]:


spmf = Spmf("GSPAN", input_filename="F://BIO_1//seminar//Bouns2//enzymes_graph.txt",
            output_filename="F://BIO_1//seminar//Bouns2//output.txt",
            spmf_bin_location_dir="F://BIO_1//seminar//Bouns2" ,arguments=[.4, 5,"true","true","true"])
spmf.run()


# In[5]:


df = pd.read_csv('F:\\BIO_1\\seminar\\Bouns2\\enzymes_graph.txt', delimiter = "\t")
df.to_csv(r'F:\\BIO_1\\seminar\\Bouns2\\enzymes_graph_data.csv')


# In[6]:


print (df)


# In[7]:


read_file = pd.read_csv (r'F:\\BIO_1\\seminar\\Bouns2\\enzymes_graph.txt')
read_file.to_csv (r'F:\\BIO_1\\seminar\\Bouns2\\output.csv', index=None)


# In[8]:


args_str = '-s 2 -d True -l 5 -p True -w True F:\\BIO_1\\seminar\\Bouns2\\enzymes_graph.txt'
FLAGS, _ = parser.parse_known_args(args=args_str.split())


# In[11]:


gs = main(FLAGS)


# In[15]:


for g in main(FLAGS).graphs.values():
    g.plot()


# In[13]:



spmf.to_pandas_dataframe(pickle=True)
spmf.to_csv("newoutput.csv")


# In[ ]:




