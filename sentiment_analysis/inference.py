from transformers import  AutoTokenizer, AutoModelForSequenceClassification, pipeline
import config
import clean_data
import sys


def run(comment):
    model= AutoModelForSequenceClassification.from_pretrained(config.FINETUNED_MODEL_PATH)
    tokenizer = AutoTokenizer.from_pretrained(config.FINETUNED_TOKENIZER_PATH)
    comment=clean_data.clean(comment)
    analyse=pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
    resultat=analyse(comment)
    if resultat[0]['label']=='Positive' and resultat[0]['score']>0.7:
        return resultat[0]['score'], 1
    elif resultat[0]['label']=='Negative' and resultat[0]['score']>0.7:
        return resultat[0]['score'], 0
    else:
        return resultat[0]['score'], 2
    
if __name__ == "__main__":
    run(sys.argv[1])