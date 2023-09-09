from src.settings import screen
from src.app import current_user
import src.menus.parents_menu as p
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
    figure = create_graph(current_user[0], p.current_subject[0])
    canvas = agg.FigureCanvasAgg(figure)
    canvas.draw()
    renderer = canvas.get_renderer()
    raw_data = renderer.tostring_rgb()

    size = canvas.get_width_height()

    surface = pygame.image.fromstring(raw_data, size, "RGB")

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill('black')

        # Blit the Matplotlib plot onto the Pygame screen
        screen.blit(surface, (150, 120))

        # Update the display
        pygame.display.flip()
