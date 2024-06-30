
from medium_sized.intrinsic_bias.probability_based.lbps.data import *
from medium_sized.intrinsic_bias.probability_based.lbps.lbps import *
from models.bert import *

def run_experiment():
    df = load_data()
    BERT=BERT()

    outcomes = []
    for p in df["Job Title cleaned"].unique().astype(np.str):
        outcome = bias_score("GGG is a XXX", ["he", "she"], p, BERT.tokenizer, BERT.model)
        outcome["profession"] = p

        outcomes.append(outcome)

    bias_outcomes = pd.DataFrame(outcomes).describe()

    print("Mean: ", bias_outcomes["gender_fill_bias_prior_corrected"]["mean"])
    print("Standard Deviation: ", bias_outcomes["gender_fill_bias_prior_corrected"]["std"])