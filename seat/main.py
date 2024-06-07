import weat
from data import (
    load_json, load_encodings, save_encodings, load_jiant_encodings,
)
import glob
import bert


# Our primary claim is that the associations revealed by relative nearness scores between categories match human biases and stereotypes strongly (i.e., low p-values and high effect sizes) and across many categories
list_test_json = glob.glob("./tests/seat/*")
for test_json in list_test_json:
  encs = load_json(test_json)
 
  model, tokenizer = bert.load_model()
  encs
  encs_targ1 = bert.encode(model, tokenizer, encs["targ1"]["examples"])
  encs_targ2 = bert.encode(model, tokenizer, encs["targ2"]["examples"])
  encs_attr1 = bert.encode(model, tokenizer, encs["attr1"]["examples"])
  encs_attr2 = bert.encode(model, tokenizer, encs["attr2"]["examples"])

  encs["targ1"]["encs"] = encs_targ1
  encs["targ2"]["encs"] = encs_targ2
  encs["attr1"]["encs"] = encs_attr1
  encs["attr2"]["encs"] = encs_attr2
  esize, pval = weat.run_test(encs, n_samples=10000)
  
  print("-------------------------------------------------------------")

