from tensorflow import keras
from . import config, utilis
import sys

def run(comment):
    comment=utilis.remove_emoji(comment)
    model = keras.models.load_model(config.SAVE_PATH)
    resultat=model.predict([comment])
    resultat=resultat.tolist()[0]
    i= resultat.index(max(resultat))
    return i+1
if __name__ == "__main__":
    run(sys.argv[1])