import matplotlib.pyplot as plt
from json import load

def draw_graph(user, subject):
    with open('save_file.json', flag='r') as f:
        data = load(f)
        subject_data = data[user][subject]
        labels, values = list(subject_data.items())
        


