import pandas as pd
import xlrd
import openpyxl
from pandas import ExcelWriter
from odict import odict
od=odict()
writer=ExcelWriter(r'/home/zach/Documents/Excel/export.xlsx')
LOD_List=odict(['PFMOAA_LOD',0.011],['R_EVE_LOD',0.0107],['Byproduct_5_LOD',0.0067],['Byproduct_4_LOD',0.0073],['PMPA_LOD',.0048],['PFO2HXA_LOD',0.0048],['PEPA_LOD',0.0235],['NVHOS_LOD',0.0114],['PFECA_B_LOD',0.0035],['PFO3OA_LOD',0.0092],['HFPO_DA_LOD',0.0117],['PES_LOD',0.0012],['PFECA_G_LOD',0.0062],['PFO4DA_LOD',0.0082],['Hydro_EVE_Acid_LOD',0.0020],['EVE_Acid_LOD',0.0052],['Byproduct_6_LOD',0.0012],['PFO5DA_LOD',0.0070],['Byproduct_2_LOD',0.0073],['Byproduct_1_LOD',0.0094])
Compound_List=["PFMOAA","R-EVE","Byproduct 5","Byproduct 4","PMPA","PFO2HxA","PEPA","NVHOS","PFECA_B","PFO3OA","HFPO-DA","PES","PFECA_G","PFO4DA","Hydro-EVE Acid","EVE-Acid","Byproduct 6","PFO5DA","Byproduct 2","Byproduct 1"]
data=pd.read_excel(r'/home/zach/Documents/Excel/LOD_correction.xlsx','Sheet4')
data.set_index('Response',inplace=True)
def parse_compound(T3Compound,T3Compound_LOD):
    T3Compound_parse=data.loc[data['Compound']==T3Compound]
    T3Compound_report=T3Compound_parse.loc[T3Compound_parse['Concentration']>T3Compound_LOD,['File Name','Compound','Concentration']]
    return T3Compound_report
'''PFMOAA_parse=data.loc[data['Compound']=='PFMOAA']
PFMOAA_report=PFMOAA_parse.loc[PFMOAA_parse['Concentration']>PFMOAA_LOD,['File Name','Compound','Concentration']]
PFMOAA_report.set_index('File Name',inplace=True)
R_EVE_parse=data.loc[data['Compound']=='R-EVE']
R_EVE_report=R_EVE_parse.loc[R_EVE_parse['Concentration']>R_EVE_LOD,['File Name','Compound','Concentration']]
R_EVE_report.set_index('File Name',inplace=True)'''
Combined_report=pd.concat([parse_compound(Compound_List[1],LOD_List[1]),parse_compound(Compound_List[2],LOD_List[2])])
#Combined_report=pd.concat([parse_compound("PFMOAA",PFMOAA_LOD),parse_compound("R-EVE",R_EVE_LOD),parse_compound("Byproduct 5",Byproduct_5_LOD),parse_compound("Byproduct 4",Byproduct_4_LOD),parse_compound("PMPA",PMPA_LOD),parse_compound("PFO2HxA",PFO2HXA_LOD),parse_compound("PEPA",PEPA_LOD),parse_compound("NVHOS",NVHOS_LOD),parse_compound("PFECA_B",PFECA_B_LOD),parse_compound("PFO3OA",PFO3OA_LOD),parse_compound("HFPO-DA",HFPO_DA_LOD),parse_compound("PES",PES_LOD),parse_compound("PFECA_G",PFECA_G_LOD),parse_compound("PFO4DA",PFO4DA_LOD),parse_compound("Hydro-EVE Acid",Hydro_EVE_Acid_LOD),parse_compound("EVE-Acid",EVE_Acid_LOD),parse_compound("Byproduct 6",Byproduct_6_LOD),parse_compound("PFO5DA",PFO5DA_LOD),parse_compound("Byproduct 2",Byproduct_2_LOD),parse_compound("Byproduct 1",Byproduct_1_LOD)])
export_excel=Combined_report.to_excel (writer,index='Response', header=True)
writer.save()
print(Combined_report)