import glob
from models.bert import *
from intrinsic_bias.probability_based.weat import weat
from intrinsic_bias.probability_based.weat.data import  load_json

def run_experiment():
  BERT = BERT()
  list_test_json = glob.glob("../../../data/weat/*")
  for test_json in list_test_json:
    encs = load_json(test_json)

    encs_targ1 = BERT.encode(encs["targ1"]["examples"])
    encs_targ2 = BERT.encode(encs["targ2"]["examples"])
    encs_attr1 = BERT.encode(encs["attr1"]["examples"])
    encs_attr2 = BERT.encode(encs["attr2"]["examples"])

    encs["targ1"]["encs"] = encs_targ1
    encs["targ2"]["encs"] = encs_targ2
    encs["attr1"]["encs"] = encs_attr1
    encs["attr2"]["encs"] = encs_attr2
    weat.run_test(encs, n_samples=10000)
    
    print("-------------------------------------------------------------")