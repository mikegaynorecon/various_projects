# Importing modules/classes

import requests
import pandas as pd
import numpy as np

# Creating reference country list:

url = 'http://dataservices.imf.org/REST/SDMX_JSON.svc/GenericMetadata/IFS'
data = requests.get(url).json()
data

## Functions

def get_ref_country_name_short():
    name_short = []
    for x in range(3,500):
        try:
            temp_data = data['GenericMetadata']['MetadataSet']['AttributeValueSet'][x]['ReportedAttribute'][1]['ReportedAttribute'][0]['Value']['#text']
            name_short.append(temp_data)
        except:
            pass
    return name_short

name_short = get_ref_country_name_short()

def get_ref_iso_code_3():
    iso_code_3 = []
    for x in range(3,500):
        try:
            temp_data = data['GenericMetadata']['MetadataSet']['AttributeValueSet'][x]['ReportedAttribute'][1]['ReportedAttribute'][5]['Value']['#text']
            iso_code_3.append(temp_data)
        except:
            pass
    return iso_code_3

iso_code_3 = get_ref_iso_code_3()



def get_ref_name_full():
    name_full = []
    for x in range(3,251):
        try:
            temp_data = data['GenericMetadata']['MetadataSet']['AttributeValueSet'][x]['ReportedAttribute'][1]['ReportedAttribute'][2]['Value']['#text']
            name_full.append(temp_data)
        except:
            pass
    return name_full

name_full = get_ref_name_full()



def get_ref_code_no():
    ref_number = []
    for x in range(3,500):
        try:
            temp_data = data['GenericMetadata']['MetadataSet']['AttributeValueSet'][x]['ReportedAttribute'][1]['ReportedAttribute'][1]['Value']['#text']
            ref_number.append(temp_data)
        except:
            pass
    return ref_number

ref_number = get_ref_code_no()

country_ref = pd.DataFrame(data=[iso_code_3,iso_code_2,name_full, name_short,ref_number])
country_ref = country_ref.transpose()
country_ref.columns = ['iso_code_3','iso_code_2','name_full','name_short','ref_number']
