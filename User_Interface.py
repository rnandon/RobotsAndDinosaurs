# User Interface class: Handles all interactions with terminal and user
class User_Interface:
    def __init__(self, menu_width, menu_height, border_thickness):
        self.border_character = '*'
        self.separator = '||'
        self.menu_width = menu_width
        self.menu_height = menu_height
        self.border_thickness = border_thickness
        self.main_pad = '\t\t'
        self.secondary_pad = '\t\t\t'
        self.end = '\n'

    def display_welcome(self):
        welcome_screen = self.get_welcome_screen()
        welcome_options = self.get_welcome_options()
        print(welcome_screen)
        user_selection = self.verify_inputs(welcome_options, ['y', 'n'])
        return user_selection

    def display_game_screen(self, options):
        game_screen = self.get_game_screen()
        game_options = self.get_game_options()
        print(game_screen)
        user_selection = self.verify_inputs(game_options, options)
        return user_selection

    def display_winners(self):
        winner_screen = self.get_winner_screen()
        print(winner_screen)
        return 0

    def get_welcome_screen(self):
        pass

    def get_game_screen(self):
        pass

    def get_game_options(self):
        pass

    def get_winner_screen(self):
        pass

    def verify_inputs(self, message, options):
        valid_selection = False
        user_input = ""

        while not valid_selection:
            user_input = input(message).lower()
            if user_input in options:
                valid_selection = True

        return user_input