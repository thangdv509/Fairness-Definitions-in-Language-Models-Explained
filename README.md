# Fairness Definitions in Language Models Explained

This is the artifact for the paper [Fairness Definitions in Language Models Explained](). This artifact supplies the tools and implementation guidelines to reproduce and apply fairness definitions discussed in our paper. 

Authors: Thang Viet Doan, Zhibo Chu, Zichong Wang and Wenbin Zhang

## Installation

Install required packages/libraries:

```shell script
$ pip install -r requirements.txt
```
For [GPT](https://openai.com/api/) and [Llama](https://www.together.ai/), access keys are required for API requests. Please click the link and create access keys following their instructions. After obtaining the access credentials, fill them in  `api_key.py`.

```shell script
OPENAI_KEY = "you openai key" # for OpenAI GPT
TOGETHERAPI_KEY = "your togetherapi key" # for Llama2 
```

## Reproducing The Paper

This section is organized according to the section in our paper 

### Fairness definitions for medium-sized language models

**Intrinsic bias** 

* Similarity-based bias. 
  * weat
  * seat
  * ceat 
  
```shell script
$ python main.py medium intrinsic similarity <metric_name>
```

* Probability-based bias.
  * disco
  * lbps
  * cbs
  * ppl
  * cps
  * cat
  * aul
  * aula
    
```shell script
$ python main.py medium intrinsic probability <metric_name>
```

**Extrinsic bias**

* Classification
* Question answering

```shell script
$ python main.py medium extrinsic <task_name>
```

### Fairness definitions for large-sized language models

* Demographic Representation
* Stereotypical Association
* Counterfactual Fairness
* Performance Disparities
  
```shell script
$ python main.py large <strategy_name> <experiment_number>
```
