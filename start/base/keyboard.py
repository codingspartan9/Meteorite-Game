import pygame

from base.events import Event, TimedEvent


class Keyboard:
    keys_to_letter = {pygame.K_a: "a", pygame.K_b: "b", pygame.K_c: "c", pygame.K_d: "d", pygame.K_e: "e", pygame.K_f: "f", pygame.K_g: "g", pygame.K_h: "h", pygame.K_i: "i", pygame.K_j: "j", pygame.K_k: "k", pygame.K_l: "l", pygame.K_m: "m", pygame.K_n: "n", pygame.K_o: "o", pygame.K_p: "p", pygame.K_q: "q", pygame.K_r: "r",pygame.K_s: "s", pygame.K_t: "t", pygame.K_u: "u", pygame.K_v: "v", pygame.K_w: "w", pygame.K_x: "x", pygame.K_y: "y", pygame.K_z: "z", pygame.K_1: "1", pygame.K_2: "2", pygame.K_3: "3", pygame.K_4: "4", pygame.K_5: "5", pygame.K_6: "6", pygame.K_7: "7", pygame.K_8: "8", pygame.K_9: "9", pygame.K_0: "0", pygame.K_LEFTPAREN: "(", pygame.K_RIGHTPAREN: ")", pygame.K_SPACE: " ", pygame.K_PERIOD: ".", pygame.K_COMMA: ",", pygame.K_LEFT: "", pygame.K_RIGHT: "", pygame.K_UP: "", pygame.K_DOWN: "", pygame.K_ESCAPE: "", pygame.K_SLASH: ""}
    key_events = []
    key_timed_events = []
    pygame_index_to_keyboard_index = {}
    mouse_clicked_event = Event()

    def __init__(self):
        keyboard_index = 0
        for pygame_index in self.keys_to_letter.keys():
            self.pygame_index_to_keyboard_index[pygame_index] = keyboard_index
            self.key_events.append(Event())
            self.key_timed_events.append(TimedEvent(0))

            keyboard_index += 1

    def get_keyboard_index(self, pygame_index):
        return self.pygame_index_to_keyboard_index[pygame_index]

    def get_key_timed_event(self, pygame_index):
        return self.key_timed_events[self.get_keyboard_index(pygame_index)]

    def get_key_event(self, pygame_index):
        return self.key_events[self.get_keyboard_index(pygame_index)]

    def run(self):
        keys_pressed = pygame.key.get_pressed()
        self.mouse_clicked_event.run(pygame.mouse.get_pressed()[0])

        for pygame_index in self.keys_to_letter.keys():
            key_was_pressed = keys_pressed[pygame_index]

            self.get_key_event(pygame_index).run(key_was_pressed)

            should_reset = not self.get_key_event(pygame_index).happened_last_cycle() and not key_was_pressed

            self.get_key_timed_event(pygame_index).run(should_reset, key_was_pressed)


