import pygame_menu

# Create a custom theme to add a background image
custom_theme = pygame_menu.themes.THEME_DARK.copy()
image = pygame_menu.baseimage.BaseImage(
    image_path='./assets/pictures/backgrounds/menu_bg.png',
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL
)
custom_theme.background_color = image
custom_theme.font = pygame_menu.font.FONT_8BIT
