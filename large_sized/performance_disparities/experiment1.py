from datasets import load_dataset, Dataset
import tqdm
from models.openaigpt import *

def load_data():
    ds = load_dataset("heegyu/bbq", "Gender_identity")
    data = Dataset.from_dict(ds)

    return data

def generate_mcq_prompt(data):
    prompt = ""
    prompt += f"*Context: {data['context']}*\n"
    prompt += f"*Question: {data['question']}*\n\n"
    prompt += f"- A) {data['ans0']}\n"
    prompt += f"- B) {data['ans1']}\n"
    prompt += f"- C) {data['ans2']}\n"
    return prompt

def convert_char_to_int(num):
    conversion_dict = {0: "A)", 1: "B)", 2: "C)"}
    return conversion_dict.get(num, "Invalid number")

def run_experiment():
    OpenAIGPT = OpenAIGPT()
    data = load_data()

    male_disambig = [0 ,0]
    female_disambig = [0, 0]
    male_ambig = [0, 0]
    female_ambig = [0, 0]

    for sample_id, sample in enumerate(tqdm(data)):
        prompt = generate_mcq_prompt(data['test'])
        response = OpenAIGPT.ask([{"role": "system", "content": "Just answer A, B, or C"}, 
                                  {"role": "user", "content": prompt}])
        
        if data['test']['additional_metadata']['stereotyped_groups'][0] == "F":
            if data['test']['context_condition'] == "ambig":
                if convert_char_to_int(data['test']["label"]) in response:
                    female_ambig[0] += 1
                else:
                    female_ambig[1] += 1
            else:
                if convert_char_to_int(data['test']["label"]) in response:
                    female_disambig[0] += 1
                else:
                    female_disambig[1] += 1
        else:
            if data['test']['context_condition'] == "ambig":
                if convert_char_to_int(data['test']["label"]) in response:
                    male_ambig[0] += 1
                else:
                    male_ambig[1] += 1
            else:
                if convert_char_to_int(data['test']["label"]) in response:
                    male_disambig[0] += 1
                else:
                    male_disambig[1] += 1

    
    print("Accuracy for male samples in ambiguous context: ", male_ambig[0]/sum(male_ambig))
    print("Accuracy for female samples in ambiguous context: ", female_ambig[0]/sum(female_ambig))
    print("Accuracy for male samples in disambiguous context: ", male_disambig[0]/sum(male_disambig))
    print("Accuracy for female samples in disambiguous context: ", female_disambig[0]/sum(female_disambig))
            
        



