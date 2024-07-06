from medium_sized.intrinsic_bias.similarity_based.weat import main as weat
from medium_sized.intrinsic_bias.similarity_based.seat import main as seat
from medium_sized.intrinsic_bias.similarity_based.ceat import main as ceat

from medium_sized.intrinsic_bias.probability_based.lbps import main as lbps

from large_sized.demographic_representation.experiment1 import main as dr_exp1
from large_sized.demographic_representation.experiment2 import main as dr_exp2
from large_sized.demographic_representation.experiment3 import main as dr_exp3

from large_sized.stereotypical_association.experiment1 import main as sa_exp1
from large_sized.stereotypical_association.experiment2 import main as sa_exp2
from large_sized.stereotypical_association.experiment3 import main as sa_exp3

from large_sized.counterfactual_fairness.experiment1 import main as cf_exp1
from large_sized.counterfactual_fairness.experiment2 import main as cf_exp2

from large_sized.performance_disparities.experiment1 import main as pd_exp1
from large_sized.performance_disparities.experiment2 import main as pd_exp2
from large_sized.performance_disparities.experiment3 import main as pd_exp3

import sys

def print_invalid_command():
    print("Invalid command!")

if sys.argv[1] == "medium":
    if sys.argv[2] == "intrinsic":
        if sys.argv[3] == "similarity":
            if sys.argv[4] == "weat":
                weat.run_experiment()
            elif sys.argv[4] == "seat":
                seat.run_experiment()
            elif sys.argv[4] == "ceat":
                ceat.run_experiment()
            else: 
                print_invalid_command()

        elif sys.argv[3] == "probability":
            if sys.argv[4] == "lbps":
                pass
            else: 
                print_invalid_command()

        else: 
            print_invalid_command()

    elif sys.argv[2] == "extrinsic":
        pass
    
    else:
        print_invalid_command()

elif sys.argv[1] == "large":
    if sys.argv[2] == "dr":
        if sys.argv[3] == "exp1":
            dr_exp1.run_experiment()
        elif sys.argv[3] == "exp2":
            dr_exp2.run_experiment()
        elif sys.argv[3] == "exp3":
            dr_exp3.run_experiment()
        else: 
            print_invalid_command()

    if sys.argv[2] == "sa":
        if sys.argv[3] == "exp1":
            sa_exp1.run_experiment()
        elif sys.argv[3] == "exp2":
            sa_exp2.run_experiment()
        elif sys.argv[3] == "exp3":
            sa_exp3.run_experiment()
        else: 
            print_invalid_command()

    if sys.argv[2] == "cf":
        if sys.argv[3] == "exp1":
            cf_exp1.run_experiment()
        elif sys.argv[3] == "exp2":
            cf_exp2.run_experiment()
        else: 
            print_invalid_command()
        
    if sys.argv[2] == "pd":
        if sys.argv[3] == "exp1":
            pd_exp1.run_experiment()
        elif sys.argv[3] == "exp2":
            pd_exp2.run_experiment()
        elif sys.argv[3] == "exp3":
            pd_exp3.run_experiment()
        else: 
            print_invalid_command()

else :
    print_invalid_command()
