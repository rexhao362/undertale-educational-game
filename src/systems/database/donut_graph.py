from src.main import screen
from src.run_game import current_user, current_subject
from json import load
import pygame
import matplotlib.backends.backend_agg as agg
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")


def create_graph(user, subject):
    with open('save_file.json', 'r') as f:
        # loads values from database
        data = load(f)
        subject_data = data[user][subject]
        labels, values = zip(*subject_data.items())

    # draw pie chart
    # hex codes for yellowgreen and light coral
    colours = ['#9ACD32', '#f08080']
    explode = (0, 0)
    plt.pie(values, explode=explode, labels=labels, colors=colours,
            autopct='%1.1f%%')

    # draw a circle at the center of pie chart
    circle = plt.Circle((0, 0), 0.7, color='white')
    figure = plt.gcf()
    figure.gca().add_artist(circle)

    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis('equal')

    return figure


def donut_graph_draw():
    figure = create_graph(current_user[0], current_subject[0])
    canvas = agg.FigureCanvasAgg(figure)
    canvas.draw()
    renderer = canvas.get_renderer()
    raw_data = renderer.tostring_rgb()

    size = canvas.get_width_height()

    surf = pygame.image.fromstring(raw_data, size, "RGB")
    screen.blit(surf, (600, 400))
