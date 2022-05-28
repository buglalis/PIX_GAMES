import sys
sys.path.insert(0, "../GAME")
from GAME import *
from PING_PONG_ENGINE import *

class Ping_Pong(Game):
    def __init__(self):
        super().__init__(Ping_Pong_engine(), width = PARAMS.WINDOW_WIDTH.value, height = PARAMS.WINDOW_HEIGHT.value, name = "Ping Pong💀")
        self.condition = status.MENU
        self.menu = Menu()

    def start(self):
        self.test()
        # self.set_menu()
        super().start()


    def game_cycle(self):
        # print(self.condition)
        self.UI_pg.fill((24, 59, 100))
        match self.condition:
            case(status.START):
                self.set_menu()
                self.condition = status.MENU

            case(status.MENU):
                self.menu_update()

            case(status.START_GAME):
                self.engine.GAME()
                self.condition = status.GAME

            case(status.ROUND_R):
                self.engine.new_round(right = True)
                self.condition = status.GAME

            case(status.ROUND_L):
                self.engine.new_round(left = True)
                self.condition = status.GAME

            case(status.GAME_OVER):
                self.engine.pause()
                self.game_final()

            case(status.PAUSE_FL):
                self.game_final()

            case(status.TEST):
                # self.test()
                pass

        self.engine.check_final()

    # MENU
    def set_menu(self):
        self.menu.button = Button(
        # Mandatory Parameters
        self.UI_pg.screen,  # Surface to place button on
        POS.BUTTON_POS.value.x,  # X-coordinate of top left corner
        POS.BUTTON_POS.value.y,   # Y-coordinate of top left corner
        PARAMS.BUTTON_W.value,  # Width
        PARAMS.BUTTON_H.value,  # Height
        text = 'START',  # Text to display
        fontSize = 50,  # Size of font
        margin = 20,  # Minimum distance between text/image and edge of button
        # inactiveColour=(200, 50, 0),  # Colour of button when not being interacted with
        # hoverColour=(150, 0, 0),  # Colour of button when being hovered over
        pressedColour = (0, 200, 20),  # Colour of button when being clicked
        radius = 20, # Radius of border corners (leave empty for not curved)
        onClick = lambda: self.set_condition(status.START_GAME)  # Function to call when clicked on
        )

    def menu_update(self):
        self.UI_pg.fill(COLORS.MENU_COLOR.value)
        pygame_widgets.update(pygame.event.get())

    def game_final(self):
            # self.engine.game_final()
            # self.game_final_update()
            self.UI_pg.text("GAME OVER", FONTS.BIG_FONT.value, POS.TEXT_GAME_OVER.value.pos(), color = COLORS.TEXT_GAME_OVER_COLOR.value)
            if self.check_any_pressed_key():
                self.condition = status.START
                self.engine.clear()

    def set_condition(self, condition):
        self.condition = condition


    # EVENTS
    def goal_l(self, event):
        if event.type == EVENTS.GOAL_L.value and event.type != EVENTS.FINAL.value:
            self.condition = status.ROUND_L

    def goal_r(self, event):
        if event.type == EVENTS.GOAL_R.value and event.type != EVENTS.FINAL.value:
            self.condition = status.ROUND_R

    def final(self, event):
        if event.type == EVENTS.FINAL.value:
            self.condition = status.GAME_OVER

    def events(self):
        super().events(self.goal_l, self.goal_r, self.final)

    # TESTS
    def test(self):
        self.condition = status.TEST
        self.engine.TEST()
