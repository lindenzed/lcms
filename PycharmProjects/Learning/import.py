import pandas as pd
import xlrd
import openpyxl
from pandas import ExcelWriter
writer=ExcelWriter(r'/home/zach/Documents/Excel/export.xlsx')
LOD_List=0.011,0.0107,0.0067,0.0073,.0048,0.0048,0.0235,0.0114,0.0035,0.0092,0.0117,0.0012,0.0062,0.0082,0.0020,0.0052,0.0012,0.0070,0.0073,0.0094
Compound_List=["PFMOAA","R-EVE","Byproduct 5","Byproduct 4","PMPA","PFO2HxA","PEPA","NVHOS","PFECA_B","PFO3OA","HFPO-DA","PES","PFECA_G","PFO4DA","Hydro-EVE Acid","EVE-Acid","Byproduct 6","PFO5DA","Byproduct 2","Byproduct 1"]
data=pd.read_excel(r'/home/zach/Documents/Excel/LOD_correction.xlsx','Sheet4')
Compound_Counter=0
Append=pd.DataFrame({'File Name':[], 'Compound':[],'Concentration':[]})
def parse_compound(T3Compound,T3Compound_LOD):
    T3Compound_parse=data.loc[data['Compound']==T3Compound]
    T3Compound_report=T3Compound_parse.loc[T3Compound_parse['Concentration']>T3Compound_LOD,['File Name','Compound','Concentration']]
    return T3Compound_report
for Compounds in Compound_List:
    Append=Append.append(parse_compound(Compound_List[Compound_Counter], LOD_List[Compound_Counter]))
    Compound_Counter+=1
Append.set_index('File Name',inplace=True)
export_excel=Append.to_excel (writer,header=True)
writer.save()
print(Append)
