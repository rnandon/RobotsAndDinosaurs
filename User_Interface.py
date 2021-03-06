###        IMPORTS
### ================================
from time import sleep

# User Interface class: Handles all interactions with terminal and user
class User_Interface:
    ###        INIT METHODS
    ### ======================================================================
    def __init__(self, menu_width=80, options_width=64, border_thickness=3):
        # Basic definitions
        self.border_character = '*'
        self.separator = '||'
        self.menu_width = menu_width
        self.options_width = options_width
        self.border_thickness = border_thickness

        self.build_custom_strings()

    def build_custom_strings(self):
        # Custom widths
        self.main_between_border_space = self.menu_width - (2 * self.border_thickness)
        self.secondary_between_border_space = self.options_width - (2 * self.border_thickness)
        self.left_cell_width = (self.main_between_border_space - len(self.separator)) // 2
        self.right_cell_width = self.main_between_border_space - len(self.separator) - self.left_cell_width

        # Creating custom string blocks
        self.main_pad = '\t\t'
        self.secondary_pad = '\t\t\t'
        self.end = '\n'
        self.left_main_border = f'{self.main_pad}{self.border_character * self.border_thickness}'
        self.right_main_border = f'{self.border_character * self.border_thickness}{self.end}'
        self.left_secondary_border = f'{self.secondary_pad}{self.border_character * self.border_thickness}'
        self.right_secondary_border = self.right_main_border
        self.main_full_bar = f'{self.main_pad}{self.border_character * self.menu_width}{self.end}'
        self.main_empty_bar = f'{self.left_main_border}{" " * self.main_between_border_space}{self.right_main_border}'
        self.secondary_full_bar = f'{self.secondary_pad}{self.border_character * self.options_width}{self.end}'
        self.secondary_empty_bar = f'{self.left_secondary_border}{" " * self.options_width}{self.right_secondary_border}'

    ###        DISPLAY METHODS
    ### ======================================================================
    def display_welcome(self, game_name):
        welcome_screen = self.get_welcome_screen(game_name)
        welcome_options = self.get_welcome_options()
        print(welcome_screen)
        user_selection = self.verify_inputs(welcome_options, ['y', 'n'])
        return user_selection

    def display_game_screen(self, options_name, options, left_combatants, right_combatants, screen_title="BATTLEFIELD", left_cell_title="ROBOTS", right_cell_title="DINOSAURS"):
        # Turn data into displayable options and selection values
        formatted_options = self.get_option_values(options)
        valid_selections = formatted_options[0]
        option_texts = formatted_options[1]

        # Format game screen and options menu
        game_screen = self.get_game_screen(screen_title, left_cell_title, left_combatants, right_cell_title, right_combatants)
        game_options = self.get_game_options(options_name, option_texts)

        # Display the screen and get user input back
        print(game_screen)
        user_selection = self.verify_inputs(game_options, valid_selections)
        selected_value = options[int(user_selection) - 1]
        return selected_value

    def display_winners(self, team_name, winners):
        winner_screen = self.get_winner_screen(team_name, winners)
        print(winner_screen)
        return 0

    def display_attack(self, attack_name, damage_dealt, attacker, defender):
        message = f'{self.main_pad}{attacker.name} uses {attack_name} to hit {defender.name} for {damage_dealt} damage!!!'
        print(message)
        sleep(1)

    def display_restart(self):
        restart_screen = self.get_restart_screen()
        user_selection = self.verify_inputs(restart_screen, ['y', 'n'])
        return user_selection

    def display_exit(self):
        exit_screen = self.get_exit_screen()
        print(exit_screen)

    ###        STRING FORMATTING METHODS
    ### =======================================================================
    def get_welcome_screen(self, game_name):
        # Top of welcome screen w/ 2 empty lines before game name
        welcome_screen = f'{self.main_full_bar}'
        welcome_screen += f'{self.main_empty_bar}'
        welcome_screen += f'{self.main_full_bar}'
        welcome_screen += f'{self.main_empty_bar}'
        welcome_screen += f'{self.main_empty_bar}'

        # Add each part of the game name on a new line
        for part in game_name:
            line_content = self.center_value_in_space(part, self.main_between_border_space)
            welcome_screen += f'{self.left_main_border}{line_content}{self.right_main_border}'

        # Two empty lines followed by two full width bars of the border character
        welcome_screen += f'{self.main_empty_bar}'
        welcome_screen += f'{self.main_empty_bar}'
        welcome_screen += f'{self.main_full_bar}'
        welcome_screen += f'{self.main_full_bar}'

        return welcome_screen

    def get_welcome_options(self):
        # Top of options, single full bar + title line
        welcome_options = f'{self.secondary_full_bar}'
        welcome_options += f'{self.left_secondary_border}{self.center_value_in_space("ARE YOU READY TO BEGIN?", self.secondary_between_border_space)}{self.right_secondary_border}'
        
        # Options
        welcome_options += f'{self.left_secondary_border}{self.center_value_in_space("Y/N", self.secondary_between_border_space)}{self.right_secondary_border}'

        # Bottom of options, single full bar and push input area over
        welcome_options += f'{self.secondary_full_bar}'
        welcome_options += f'{self.end}{self.end}{self.secondary_pad}'

        return welcome_options
        
    def get_game_screen(self, screen_title, left_cell_title, left_cell_data, right_cell_title, right_cell_data):
        # Get the content for the title row
        title_row_width = self.menu_width - (2 * self.border_thickness)
        title_row = self.center_value_in_space(screen_title, title_row_width)

        # Title bar - Title row between two full bars
        game_screen = f'{self.main_full_bar}'
        game_screen += f'{self.left_main_border}{title_row}{self.right_main_border}'
        game_screen += f'{self.main_full_bar}'
        
        # Note - this section will handle left and right cells simultaneously
        # Cell titles - cell title row followed by full bar
        left_cell_title_label = self.center_value_in_space(left_cell_title, self.left_cell_width)
        right_cell_title_label = self.center_value_in_space(right_cell_title, self.right_cell_width)
        cell_titles = f'{left_cell_title_label}{self.separator}{right_cell_title_label}'
        game_screen += f'{self.left_main_border}{cell_titles}{self.right_main_border}'
        game_screen += f'{self.main_full_bar}'

        # Extract and format data for each cell
        formatted_data = self.format_cell_data(left_cell_data, right_cell_data)
        left_cell = formatted_data[0]
        right_cell = formatted_data[1]

        # Fill cells with data
        for i in range(len(left_cell)):
            current_row = f'{self.left_main_border}{left_cell[i]}{self.separator}{right_cell[i]}{self.right_main_border}'
            game_screen += current_row
        
        # Game screen bottom - empty row with divider followed by two full bars
        game_screen += f'{self.left_main_border}{self.center_value_in_space(self.separator, self.main_between_border_space)}{self.right_main_border}'
        game_screen += f'{self.main_full_bar}'
        game_screen += f'{self.main_full_bar}'

        return game_screen

    def get_game_options(self, option_name, options):
        # Top of options, single full bar + title line
        game_options = f'{self.secondary_full_bar}'
        game_options += f'{self.left_secondary_border}{self.center_value_in_space(option_name, self.secondary_between_border_space)}{self.right_secondary_border}'

        # Format and add options
        for i in range(len(options)):
            option = options[i]
            current_line = f'{self.left_secondary_border}{self.center_value_in_space(option, self.secondary_between_border_space)}{self.right_secondary_border}'
            game_options += current_line

        # Bottom of options, single full bar and push input area over
        game_options += f'{self.secondary_full_bar}'
        game_options += f'{self.end}{self.end}{self.secondary_pad}'

        return game_options

    def get_winner_screen(self, team_name, winners):
        # Top of screen
        winner_screen = f'{self.main_full_bar}'
        winner_screen += f'{self.left_main_border}{self.center_value_in_space("WINNERS", self.main_between_border_space)}{self.right_main_border}'
        winner_screen += f'{self.main_full_bar}'
        winner_screen += f'{self.main_empty_bar}'

        # Winning team and winner names
        winner_screen += f'{self.left_main_border}{self.center_value_in_space(team_name, self.main_between_border_space)}{self.right_main_border}'
        winner_screen += f'{self.main_empty_bar}'
        for winner in winners:
            current_line = f'{self.left_main_border}{self.center_value_in_space(winner.name, self.main_between_border_space)}{self.right_main_border}'
            winner_screen += current_line

        # Bottom of screen
        winner_screen += f'{self.main_empty_bar}'
        winner_screen += f'{self.main_full_bar}'
        winner_screen += f'{self.main_full_bar}'

        return winner_screen

    def get_restart_screen(self):
        # Top of screen, full bar + empty bar
        restart_screen = f'{self.main_full_bar}'
        restart_screen += f'{self.main_empty_bar}'

        # Middle of screen, format message into empty lines
        restart_message = ['WOULD YOU', 'LIKE TO', 'PLAY AGAIN?', 'Y/N']
        for part in restart_message:
            current_line = f'{self.left_main_border}{self.center_value_in_space(part, self.main_between_border_space)}{self.right_main_border}'
            restart_screen += current_line

        # Bottom of screen, empty bar + full bar
        restart_screen += f'{self.main_empty_bar}'
        restart_screen += f'{self.main_full_bar}'

        return restart_screen

    def get_exit_screen(self):
        # Top of screen, full bar + empty bar
        exit_screen = f'{self.main_full_bar}'
        exit_screen += f'{self.main_empty_bar}'

        # Middle of screen, format message into empty lines
        exit_message = ['THANKS', 'FOR', 'PLAYING!']
        for part in exit_message:
            current_line = f'{self.left_main_border}{self.center_value_in_space(part, self.main_between_border_space)}{self.right_main_border}'
            exit_screen += current_line

        # Bottom of screen, empty bar + full bar
        exit_screen += f'{self.main_empty_bar}'
        exit_screen += f'{self.main_full_bar}'

        return exit_screen

    def get_option_values(self, data):
        options = []
        # Using numeric selection values, used for list indices after verification
        selections = [f'{i+1}' for i in range(len(data))]

        # Add each option to the list
        for i in range(len(data)):
            current_option = f'{i + 1}: {data[i].name}'
            options.append(current_option)

        return (selections, options)

    ###        AUXILIARY METHODS
    ### ======================================================================
    def format_cell_data(self, left_data, right_data):
        max_data_length = max(len(left_data), len(right_data)) # Make sure to account for different lengths of data
        left_data_length = len(left_data)
        right_data_length = len(right_data)

        left_formatted = []
        right_formatted = []

        for i in range(max_data_length):
            # Avoid going out of range
            left_current_data = ''
            right_current_data = ''
            if i < left_data_length:
                left_current_data = left_data[i]
            if i < right_data_length:
                right_current_data = right_data[i]

            # Left cell formatting
            if left_current_data:
                # Format data if there is some
                left_formatted.append(self.center_value_in_space(f'NAME: {left_current_data.name}', self.left_cell_width))
                status_line = f'   HEALTH: {left_current_data.get_health()}   POWER: {left_current_data.get_resource()}'
                left_formatted.append(f'{status_line}{" " * (self.left_cell_width - len(status_line))}')
            else:
                # Fill with empty lines
                left_formatted.append(" " * self.left_cell_width)
                left_formatted.append(" " * self.left_cell_width)

            # Right cell formatting
            if right_current_data:
                # Format data if there is some
                right_formatted.append(self.center_value_in_space(f'NAME: {right_current_data.name}', self.right_cell_width))
                status_line = f'   HEALTH: {right_current_data.get_health()}   ENERGY: {right_current_data.get_resource()}'
                right_formatted.append(f'{status_line}{" " * (self.right_cell_width - len(status_line))}')
            else:
                # Fill with empty lines
                right_formatted.append(" " * self.right_cell_width)
                right_formatted.append(" " * self.right_cell_width)

        return (left_formatted, right_formatted)

    def verify_inputs(self, message, options):
        # Take in array of valid options and reprompt the user until a valid option is selected
        valid_selection = False
        user_input = ""

        while not valid_selection:
            user_input = input(message).lower()
            if user_input in options:
                valid_selection = True

        return user_input

    def center_value_in_space(self, value, total_width):
        # Format value to be centered in line
        left_pad = (total_width - len(value)) // 2
        right_pad = total_width - left_pad - len(value)
        return f'{" " * left_pad}{value}{" " * right_pad}'

    ###        TESTING
    ### ======================================================================
    def tests(self):
        print("Testing internal variables")
        print(self.left_main_border)
        print(self.left_secondary_border)
        print(self.right_main_border)
        print(self.right_secondary_border)
        print(self.main_full_bar)
        print(self.main_empty_bar)

        self.display_welcome(['WELCOME TO', 'ROBOTS', 'VS.', 'DINOSAURS'])

# test = User_Interface()
# test.tests()