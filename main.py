import sys
from models.bert import *
from models.openaigpt import *
from models.llama2 import *

from medium_sized.intrinsic_bias.similarity_based.weat import main as weat
from medium_sized.intrinsic_bias.similarity_based.seat import main as seat
from medium_sized.intrinsic_bias.similarity_based.ceat import main as ceat


from medium_sized.intrinsic_bias.probability_based.lbps import main as lbps
#weat.run_experiment()