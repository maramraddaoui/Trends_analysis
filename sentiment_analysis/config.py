#train
PRETRAINED_MODEL = "moussaKam/barthez-sentiment-classification"
PRETRAINED_TOKENIZER = "moussaKam/barthez"
TRAINING_FILE = "/home/maram/PFE/Analyse des tendances/sentiment_analysis/french_tweets.csv"
SAVE_PATH="/home/maram/PFE/Analyse des tendances/sentiment_analysis/model"

OUTPUT_DIR="./"
NUM_EPOCHS=2
TRAIN_BATCH_SIZE=16
VAL_BATCH_SIZE=64
WARMUP_STEPS=580
LEARNING_RATE=5e-5
WEIGHT_DECAY=0.01
LOGGING_DIR='./logs'
LOGGING_STEPS=10

#inference
FINETUNED_MODEL_PATH= "/home/maram/PFE/Analyse des tendances/sentiment_analysis/model"
FINETUNED_TOKENIZER_PATH= "/home/maram/PFE/Analyse des tendances/sentiment_analysis/model"
