#%%

import pandas as pd
from collections import Counter
field_prod_data_path = '../data/CNS_Field_Production.csv'
cns_gas_train_data_path = '../data/CNS_gas_train.csv'
cns_oil_data_path = '../data/CNS rock samples.csv'
cns_rock_samples_path = '../data/CNS rock samples.csv'
field_prod_data = pd.read_csv(field_prod_data_path)

cns_gas_train_data = pd.read_csv(cns_gas_train_data_path)
cns_gas_train_data


X_cols = ['Country', 'WELL_NAME', 'OGA Well Name', 'WH_SITETYPE', 'WH_FIELD',
       'WH_BLOCK', 'WH_LAT', 'WH_LONG', 'WH_COORD_SYS', 'WH_OPERATOR',
       'WH_SPUD_DATE', 'WH_SPUD_YEAR', 'WH_COMP_DATE', 'WH_TD_M',
       'WH_DR_ELEV_M', 'WH_DEPTH_REF', 'WH_WATER_DEPTH_M', 'SAMPLE_ID',
       'SH_DEPTH_TOP_FT', 'SH_DEPTH_BOT_FT', 'SH_SAMPLE_TYPE',
       'SH_SAMPLE_SUB_TYPE', 'SH_ORIG', 'SH_ORIG_DESC', 'SH_TREATMENT',
       'SH_TREATMENT_DESC', 'SH_LITH', 'SH_AGE', 'SH_AGE_BOT', 'SH_FORM',
       'SH_FORM_BOT', 'SH_CDATE', 'SH_COMMENT', 'SAMPLE_ID_GM',
       'SAMPLE_ID_GDB', 'SAMPLE_ID_SAM', 'EXT_SAMPLE_VENDOR', 'SAMPLE_ID_EXT',
       'GAS_METHOD', 'GAS_LAB', 'GAS_ACQ_DATE', 'GAS_TOTAL_CONCENTRATION',
       'GAS_AIR',  'GAS_C2', 'C2_UNSAT', 'C3_UNSAT',
         'C4_UNSAT', 'GAS_NEOC5',
       'C5_UNSAT', 'GAS_NC5_PLUS', 'GAS_C6PLUS', 'GAS_O2', 'GAS_CO2', 'GAS_H2',
       'GAS_H2S', 'GAS_HE', 'GAS_N2', 'D_G_METHOD', 'D_G_LAB', 'D_G_DATA_TYPE',
       'D_G_ACQ_DATE', 'CSIA_CONC_C1', 'CSIA_NC1', 'CSIA_NC2', 'CSIA_NC3',
       'CSIA_IC4', 'CSIA_NC4', 'CSIA_NEOC5', 'CSIA_IC5', 'CSIA_NC5',
       'CSIA_ETHENE', 'CSIA_PROPENE', 'DC_G_CO2', 'DO_G_CO2', 'DS_G_H2S',
       'DD_G_H2', 'DN_G_N2', 'DD_G_GAS', 'DD_G_NC1', 'DD_G_NC2', 'DD_G_NC3',
       'DD_G_IC4', 'DD_G_NC4', 'DD_G_IC5', 'DD_G_NC5']



y_cols = ['GAS_C1', 'GAS_C2', 'GAS_C3', 'GAS_IC4', 'GAS_NC4', 'GAS_IC5', 'GAS_NC5']