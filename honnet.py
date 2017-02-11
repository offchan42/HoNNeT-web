from keras.models import load_model
from operator import itemgetter
import pickle
import numpy as np

AVAIL_HEROES = 260 # actually 134 but extra for future
HEROES_NAME_FILE = 'heroes_name.pkl'
MODEL_FILE = 'honnet_brain.h5'

with open(HEROES_NAME_FILE, 'rb') as f:
    heroes_dict = pickle.load(f)

def load():
    model = load_model(MODEL_FILE)
    model.summary()
    return model


def hero_id_to_name(hero_id):
    return heroes_dict[hero_id]['disp_name']

def vectorize_matches(matches, include_Y=True):
    legion_vec = np.zeros([len(matches), AVAIL_HEROES])
    hellbourne_vec = np.zeros([len(matches), AVAIL_HEROES])
    if include_Y:
        winner = np.zeros([len(matches), 1])
        concede = np.zeros([len(matches), 1])
        secs = np.zeros([len(matches), 1])
    for m, match in enumerate(matches):
        for hero_id in match['legion']:
            legion_vec[m, hero_id] = 1.
        for hero_id in match['hellbourne']:
            hellbourne_vec[m, hero_id] = 1.
        if include_Y:
            if match['winner']:
                winner[m, 0] = 1.
            if match['concedes']:
                concede[m, 0] = 1.
            secs[m, 0] = match['secs']
    x = np.concatenate([legion_vec, hellbourne_vec], axis=1)
    if include_Y:
        y = np.concatenate([winner, concede, secs], axis=1)
    return (x, y) if include_Y else x

# returns a hero that maximize win probability in a given team
# if 'optimal' is false, it will return a hero that minimize win probability
def optimal_hero_choice(model, match, hellbourne_side=False, as_list=True, as_name=True, optimal=True):
    legion = match['legion']
    hellbourne = match['hellbourne']
    team_ids = hellbourne if hellbourne_side else legion
    hypothesis = []
    for id in set(heroes_dict.keys()) - set(legion + hellbourne): # all choosable hero ids
        team_ids.append(id)
        x = vectorize_matches([match], include_Y=False)
        team_ids.pop()
        p = model.predict(x, verbose=0)[0]
        hero = id
        if as_name:
            hero = hero_id_to_name(hero)
        hypothesis.append((hero, p[0, 1 if hellbourne_side else 0]))
    extrema = max if optimal else min
    return sorted(hypothesis, key=itemgetter(1), reverse=optimal) if as_list else extrema(hypothesis, key=itemgetter(1))

# turn a list of legion and hellbourne into a dictionary
def to_match_dict(leg, hell):
    return {'legion': leg, 'hellbourne': hell}

def humanize(xrow):
    legion, hellbourne = [], []
    for i, el in enumerate(xrow):
        if el:
            if i < AVAIL_HEROES:
                name = hero_id_to_name(i)
                legion.append(name)
            else:
                name = hero_id_to_name(i - AVAIL_HEROES)
                hellbourne.append(name)
    return {'legion': legion, 'hellbourne': hellbourne}

if __name__ == '__main__':
    load()
