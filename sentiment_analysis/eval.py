from transformers import AutoTokenizer, AutoModelForSequenceClassification
from torch.utils.data import DataLoader
import torch
import pandas as pd
from dataset import Dataset 
import config
import clean_data

def run():
    tokenizer=AutoTokenizer.from_pretrained(config.SAVE_PATH)
    model = AutoModelForSequenceClassification.from_pretrained(config.SAVE_PATH)
    model.eval()

    df=pd.read_csv(config.TEST_FILE)
    
    comments=[]
    for comment in df.text.tolist():
        comments.append(clean_data.clean(comment))
    labels=df.label.tolist()

    test_encodings=tokenizer(comments, truncation=True, padding=True)
    test_dataset=Dataset(test_encodings, labels) 

    accuracy = 0.0
    total = 0.0
    test_loader=DataLoader(test_dataset, batch_size=16, shuffle=True)    
    with torch.no_grad():
        for batch in test_loader:
            input_ids=batch['input_ids']
            attention_mask=batch['attention_mask']
            labels=batch['labels']
            outputs=model(input_ids, attention_mask=attention_mask, labels=labels)
            predictions=F.softmax(outputs.logits, dim=1)
            pred= torch.argmax(predictions, dim=1)
            total += labels.size(0)
            accuracy += (pred == labels).sum().item()
        accuracy = (100 * accuracy / total)

    return accuracy

if __name__ == "__main__":
    run()