from flask import Flask, render_template, request
import honnet
import numpy as np

TIMES_SERVED = 0

app = Flask(__name__)
model = honnet.load()
TEAM_NAMES = ['Legion', 'Hellbourne']

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
        legion_prob=round(100 * prediction[0][0,0], 2),
        hellbourne_prob=round(100 * prediction[0][0,1], 2),
        concede_prob=round(100 * prediction[1][0,0], 2),
        lasting_minutes=round(prediction[2][0,0] / 60),
        heroes_id_dict=honnet.heroes_id_dict,
        winner=TEAM_NAMES[np.argmax(prediction[0][0,:])],
        loser=TEAM_NAMES[np.argmin(prediction[0][0,:])],
    )

if __name__ == '__main__':
    app.run()
