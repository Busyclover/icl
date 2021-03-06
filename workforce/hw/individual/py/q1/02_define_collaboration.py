# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 12:14:07 2016

@author: Jleach1
"""

# %%
import timeit
import pandas as pd

# %%
collab = pd.read_csv('../../../../data/outputs/collaborators.csv')
inv_to_pat = pd.read_csv('../../../../data/outputs/inv_to_pats.csv')
d3_inv = pd.read_csv('../../../../data/outputs/d3_inv.csv')
d3_inv.dropna(inplace = True)

    # %% Collaboration 1 - total collaborators for all inventors on patent
# Get list of all distinct patents
all_patents = pd.unique(d3_inv.pnum)

# Set up list to hold total number of collaborators per patent
total_collaborators = []

start_time = timeit.default_timer()
# Loop over patents
for patent in all_patents:
    # Find the inventors on that patent
    inventors = d3_inv[d3_inv.pnum == patent].inv_num
    # Set up list to hold all collaborators for that patent
    all_collaborators = []
    
    # For each inventor on the patent
    for inventor in inventors:
        # Find their collaborators
        collaborators = collab[collab.inv1 == inventor].inv2
        
        # For each collaborator
        for collaborator in collaborators:
            # Add them to the list of all collaborators
            if collaborator not in all_collaborators:
                all_collaborators.append(collaborator)
            else:
                pass
    # Get the unique set of collaborators for all inventors on the patent
    all_collaborators = pd.unique(all_collaborators)
    # find out how many there are    
    n_collab = len(all_collaborators)
    # add that number to the set of total collaborators
    total_collaborators.append(n_collab)

elapsed = timeit.default_timer() - start_time         

patent_collaborators_1 = pd.DataFrame({'pnum': all_patents, 
                                       'collab1': total_collaborators})
                                       
patent_collaborators_1.to_csv("../../../../data/outputs/collab1.csv", index = False)                                       
                                       
# %% Collaboration 2 - patent overlap for all inventors in patent
inv_to_pat['pat_set'] = inv_to_pat.pnum_str.apply(lambda x: set(x.split(', ')))

intersections = []
for patent in all_patents:
    inventors = d3_inv[d3_inv.pnum == patent].inv_num
    if len(inventors) < 2:
        intersections.append(0)
    else:
        patents = inv_to_pat[inv_to_pat['inv_num'].isin(inventors)].pat_set
        intersect_size = len(set.intersection(*[x for x in patents]))
        intersections.append(intersect_size)
    
patent_collaborators_2 = pd.DataFrame({'pnum': all_patents,
                                       'collab2': intersections})    
                                       
patent_collaborators_2.to_csv("../../../../data/outputs/collab2.csv", index = False) 