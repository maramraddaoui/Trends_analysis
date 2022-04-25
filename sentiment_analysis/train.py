from transformers import Trainer, TrainingArguments, AutoTokenizer, AutoModelForSequenceClassification
from sklearn.model_selection import train_test_split
import pandas as pd
from dataset import Dataset 
import config
import clean_data


def run():
    df=pd.read_csv(config.TRAINING_FILE)
    
    comments=[]
    for comment in df.text.tolist():
        comments.append(clean_data.clean(comment))
    labels=df.label.tolist()
    
    train_texts, val_texts, train_labels, val_labels = train_test_split(comments, labels, test_size=.2)
    
    model=AutoModelForSequenceClassification.from_pretrained(config.PRETRAINED_MODEL)
    tokenizer=AutoTokenizer.from_pretrained(config.PRETRAINED_TOKENIZER)
    
    model.train() 
    train_encodings=tokenizer(train_texts, truncation=True, padding=True)
    val_encodings=tokenizer(val_texts, truncation=True, padding=True)
    train_dataset=Dataset(train_encodings, train_labels)
    val_dataset=Dataset(val_encodings, val_labels)
    
    training_args=TrainingArguments(
    output_dir=config.OUTPUT_DIR,
    num_train_epochs=config.NUM_EPOCHS,
    per_device_train_batch_size=config.TRAIN_BATCH_SIZE,
    per_device_eval_batch_size=config.VAL_BATCH_SIZE,
    warmup_steps=config.WARMUP_STEPS,
    learning_rate=config.LEARNING_RATE,
    weight_decay=config.WEIGHT_DECAY,
    logging_dir=config.LOGGING_DIR,
    logging_steps=config.LOGGING_STEPS
    )
    
    trainer=Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=val_dataset  
    )
    trainer.train()

    model.save_pretrained(config.SAVE_PATH)
    tokenizer.save_pretrained(config.SAVE_PATH)

if __name__ == "__main__":
    run()