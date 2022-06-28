import pygame.display


class Window:
    screens = []
    window = None
    background_color = None
    title = None

    def __init__(self, length, height, background_color, title):
        self.window = pygame.display.set_mode((length, height))
        pygame.display.set_caption(title)
        self.background_color = background_color

    def add_screen(self, screen):
        self.screens.append(screen)

    def display_screen(self, screen):
        for other_screen in self.screens:
            other_screen.is_visible = False

        screen.is_visible = True

    def run(self):
        self.window.fill(self.background_color)
        
        for screen in self.screens:
            if screen.is_visible:
                screen.run()
                screen.render_background()

            else:
                continue

            for component in screen.get_components():
                component.run()
                component.render()

        pygame.display.update()

    def get_window(self):
        return self.window


