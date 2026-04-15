import pickle

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def predict_message(msg):
    msg_vector = vectorizer.transform([msg])
    return model.predict(msg_vector)[0]