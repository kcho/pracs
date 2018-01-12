import pandas as pd
import numpy as np
import sys


B = pd.read_csv('Behrens.csv', sep='\t', lineterminator='\r')
cols=list(B)
#print(cols)

B = B.rename(columns={'Left seed\rTotal track no.': 'Mask_L_tot', 'Right seed\rTotal track no.': 'Mask_R_tot'})

L_col = [col for col in B if col.startswith('L')]
R_col = [col for col in B if col.startswith('R')]
#print(cols)
#print(L_col)

B['Num_L_tot'] = B[L_col].sum(axis=1)
B['Num_R_tot'] = B[R_col].sum(axis=1)

for lcol in L_col:
    B['perc_'+lcol] = B[lcol]/B['Mask_L_tot']

L_perc = [col for col in B if col.startswith('perc_L')]
Left_B = B.loc[:, B.columns.isin(list(L_perc))]
subject = B[['Subject']]
Left_B = subject.join(Left_B)

Order_LeftB = Left_B.set_index('Subject')
np.argsort(-Order_LeftB.values, axis=1)
Order_LeftB.columns[np.argsort(-Order_LeftB.values, axis=1)]
Results_Order_LeftB=pd.DataFrame(Order_LeftB.columns[np.argsort(-Order_LeftB.values, axis=1)], index=Order_LeftB.index)
Results_Order_LeftB.to_csv('Results_Order_LeftB.csv')


for column in Results_Order_LeftB.columns:
    Results_Order_LeftB[column].value_counts().reset_index().to_csv('count_LeftB.csv', mode='a')






for rcol in R_col:
    B['perc_'+rcol] = B[rcol]/B['Mask_R_tot']

R_perc = [col for col in B if col.startswith('perc_R')]

Right_B =  B.loc[:, B.columns.isin(list(R_perc))]
Right_B = subject.join(Right_B)

Order_RightB =  Right_B.set_index('Subject')
np.argsort(-Order_RightB.values, axis=1)
Order_RightB.columns[np.argsort(-Order_RightB.values, axis=1)]
Results_Order_RightB=pd.DataFrame(Order_RightB.columns[np.argsort(-Order_RightB.values, axis=1)], index=Order_RightB.index)
Results_Order_RightB.to_csv('Results_Order_RightB.csv')
for column in Results_Order_RightB.column:
         Results_Order_RightB[column].value_counts().reset_index().to_csv('count_RightB.csv', mode='a')










M=pd.read_csv('Morel.csv', sep='\t', lineterminator='\r')
L_col = [col for col in M if col.startswith('L')]
R_col = [col for col in M if col.startswith('R')]
for lcol in L_col:
    M['perc_'+lcol] = M[lcol]/M['L_TOT']
for rcol in R_col:
    M['perc_'+rcol] = M[rcol]/M['R_TOT']
L_perc = [col for col in M if col.startswith('perc_L')]
R_perc = [col for col in M if col.startswith('perc_R')]
Left_M = M.loc[:, M.columns.isin(list(L_perc))]
Right_M = M.loc[:, M.columns.isin(list(R_perc))]
subject = M[['Subject']]
Left_M = subject.join(Left_M)
Right_M = subject.join(Right_M)

Order_LeftM = Left_M.set_index('Subject')
np.argsort(-Order_LeftM.values, axis=1)
Order_LeftM.columns[np.argsort(-Order_LeftM.values, axis=1)]
Results_Order_LeftM=pd.DataFrame(Order_LeftM.columns[np.argsort(-Order_LeftM.values, axis=1)], index=Order_LeftM.index)
Results_Order_LeftM.to_csv('Results_Order_LeftM.csv')
for column in Results_Order_LeftM.columns:
    Results_Order_LeftM[column].value_counts().reset_index().to_csv('count_LeftM.csv', mode='a')

Order_RightM = Right_M.set_index('Subject')
np.argsort(-Order_RightM.values, axis=1)
Order_RightM.columns[np.argsort(-Order_RightM.values, axis=1)]
Results_Order_RightM=pd.DataFrame(Order_RightM.columns[np.argsort(-Order_RightM.values, axis=1)], index=Order_RightM.index)
Results_Order_RightM.to_csv('Results_Order_RightM.csv')
for column in Results_Order_RightM.columns:
    Results_Order_RightM[column].value_counts().reset_index().to_csv('count_RightM.csv', mode='a')
