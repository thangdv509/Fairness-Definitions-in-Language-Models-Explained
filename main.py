import sys
from models.bert import *
from models.openaigpt import *
from models.llama2 import *
from intrinsic_bias.probability_based.weat import main as weat
from intrinsic_bias.probability_based.seat import main as seat
from intrinsic_bias.probability_based.ceat import main as ceat

#weat.run_experiment()