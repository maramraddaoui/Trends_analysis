from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
import config
import sys

def filter(comment, labels):
    tokenizer = AutoTokenizer.from_pretrained("Jean-Baptiste/camembert-ner")
    model = AutoModelForTokenClassification.from_pretrained("Jean-Baptiste/camembert-ner")
    nlp = pipeline('ner', model=model, tokenizer=tokenizer, aggregation_strategy="simple")
    label=False
    for word in comment.split():
      if word in labels:
        label=True
    if label==True:
        one_name=True
        for x in nlp(comment):
            if (x['entity_group']== 'ORG' or x['entity_group']== 'PER') and x['word'] not in labels:
                one_name=False
        if one_name==True:
            return True
        else:
            return False
    else:
        return False

def run(comment):
    partis_nb=0
    resultat=[]
    for partis in config.partis.items():
        if filter(comment, partis[1])== True:
            partis_nb+=1
            resultat.append(partis[0])
    if partis_nb==1:
        return resultat[0]
    else:
        return 0

if __name__ == "__main__":
    run(sys.argv[1])