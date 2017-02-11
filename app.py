from flask import Flask, render_template, request
import honnet

app = Flask(__name__)
model = honnet.load()

def extract_elements(params):
    if params:
        return [int(x) for x in params.split(',')]
    else:
        return []

@app.route('/', methods=['POST', 'GET'])
def index():
    legion = extract_elements(request.args.get('legion'))
    hellbourne = extract_elements(request.args.get('hellbourne'))
    print('Legion:', legion)
    print('Hellbourne:', hellbourne)
    match = honnet.to_match_dict(legion, hellbourne)
    vector = honnet.vectorize_matches([match], include_Y=False)
    prediction = model.predict(vector)
    print('Prediction:', prediction)
    print(len(honnet.heroes_id_dict))
    return render_template(
        'index.html',
        legion=legion,
        hellbourne=hellbourne,
        prediction=prediction,
        heroes_id_dict=honnet.heroes_id_dict
    )

if __name__ == '__main__':
    app.run()
