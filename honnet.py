from keras.models import load_model

def load():
    model = load_model('honnet_brain.h5')
    print(model)
    return model

if __name__ == '__main__':
    load()
