from flask import Flask, render_template, request
import honnet

TIMES_SERVED = 0

app = Flask(__name__)
model = honnet.load()

@app.route('/', methods=['POST', 'GET'])
def index():
    global TIMES_SERVED
    legion = honnet.extract_hero_ids(request.args.get('legion'))
    hellbourne = honnet.extract_hero_ids(request.args.get('hellbourne'))
    print('Legion:', legion)
    print('Hellbourne:', hellbourne)
    match = honnet.to_match_dict(legion, hellbourne)
    vector = honnet.vectorize_matches([match], include_Y=False)
    prediction = model.predict(vector)
    print('Prediction:', prediction)
    TIMES_SERVED += 1
    print('Times Served:', TIMES_SERVED)
    return render_template(
        'index.html',
        legion=legion,
        hellbourne=hellbourne,
        prediction=prediction,
        heroes_id_dict=honnet.heroes_id_dict
    )

if __name__ == '__main__':
    app.run()
