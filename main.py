import sys
from models.bert import *
from models.openaigpt import *
from models.llama2 import *

from medium_sized.intrinsic_bias.similarity_based.weat import main as weat
from medium_sized.intrinsic_bias.similarity_based.seat import main as seat
from medium_sized.intrinsic_bias.similarity_based.ceat import main as ceat


from medium_sized.intrinsic_bias.probability_based.lbps import main as lbps

from large_sized.demographic_representation.experiment2 import main as dr_exp2
from large_sized.demographic_representation.experiment3 import main as dr_exp3

from large_sized.performance_disparities.experiment1 import main as pd_exp1
from large_sized.performance_disparities.experiment2 import main as pd_exp2
from large_sized.performance_disparities.experiment3 import main as pd_exp3

pd_exp1.run_experiment()