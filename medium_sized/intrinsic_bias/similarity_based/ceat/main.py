import numpy as np
import datetime
import os
from medium_sized.intrinsic_bias.similarity_based.ceat.ceat import *
from medium_sized.intrinsic_bias.similarity_based.ceat.generate_ebd_bert import *

def run_experiment():
    if not os.path.exists("./bertweat1.pickle"):
        generate()

    f = open('../../../../data/ceat/data.json')
    data = json.load(f)

    ceat_groups = [
        [data.flowers,data.insects,data.pleasant,data.unpleasant], 
        [data.instruments, data.weapons, data.pleasant, data.unpleasant], 
        [data.european_3,data.african_3,data.pleasant_3,data.unpleasant_3], 
        [data.european_4,data.african_4,data.pleasant_3,data.unpleasant_3], 
        [data.european_4,data.african_4,data.pleasant_5,data.unpleasant_5],
        [data.male,data.female,data.career,data.family], 
        [data.math,data.arts,data.male_term,data.female_term],
        [data.science,data.arts_8,data.male_term_8,data.female_term_8],
        [data.mental_disease,data.physical_disease,data.temporary,data.permanent],
        [data.young_name,data.old_name,data.pleasant_5,data.unpleasant_5],
        [data.african_female,data.european_male,data.af_bias,data.em_bias_foraf], 
        [data.african_female,data.european_male,data.af_unique_bias,data.em_unique_bias_foraf],
        [data.mexican_female,data.european_male,data.lf_bias,data.em_bias_forlf],
        [data.mexican_female,data.european_male,data.lf_unique_bias,00]
    ]

    e_lst = []
    p_lst = []
    for e in range(1,15):
        e_lst.append([])
        p_lst.append([])
        print(e)
        for m in ["bert"]:
            print(m)
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))

            pes,  p_value = ceat_meta(ceat_groups = ceat_groups, model=m,test=e,N=1000)
            print("PES is {}:".format(pes))
            print("P-value is {}:".format(p_value))
            e_lst[e-1].append(pes)
            e_lst[e-1].append(p_value)
            print(" ")
        
    e_ary = np.array(e_lst)
    p_ary = np.array(p_lst)

    np.savetxt("e_1000.csv", e_ary, delimiter=",")