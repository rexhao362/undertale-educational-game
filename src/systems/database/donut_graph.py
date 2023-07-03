import matplotlib.pyplot as plt
from json import load


def draw_graph(user, subject):
    with open('save_file.json', flag='r') as f:
        # loads values from database
        data = load(f)
        subject_data = data[user][subject]
        labels, values = list(subject_data.items())

        # draw pie chart
        colours = ['yellowgreen', 'light coral']
        explode = (0, 0)
        plt.pie(values, explode=explode, labels=labels, colors=colours,
                autopct='%1.1f%%')

        # draw a circle at the center of pie to make it look like a donut
        circle = plt.Circle((0, 0), 0.7, color='white')
        fig = plt.gcf()
        fig.gca().add_artist(circle)

        # Set aspect ratio to be equal so that pie is drawn as a circle.
        plt.axis('equal')
        plt.show()
