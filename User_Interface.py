# User Interface class: Handles all interactions with terminal and user
class User_Interface:
    def __init__(self, menu_width, options_width, border_thickness):
        # Basic definitions
        self.border_character = '*'
        self.separator = '||'
        self.menu_width = menu_width
        self.options_width = options_width
        self.border_thickness = border_thickness

        # Custom widths
        self.between_border_space = menu_width - (2 * border_thickness)
        self.left_cell_width = (self.between_border_space - len(self.separator)) // 2
        self.right_cell_width = self.between_border_space - len(self.separator) - self.left_cell_width

        # Creating custom string blocks
        self.main_pad = '\t\t'
        self.secondary_pad = '\t\t\t'
        self.end = '\n'
        self.left_main_border = f'{self.main_pad}{self.border_character * self.border_thickness}'
        self.right_main_border = f'{self.border_character * self.border_thickness}{self.end}'
        self.left_secondary_border = f'{self.secondary_pad}{self.border_character * self.border_thickness}'
        self.right_secondary_border = self.right_main_border
        self.main_full_bar = f'{self.main_pad}{self.border_character * self.menu_width}{self.end}'
        self.main_empty_bar = f'{self.left_main_border}{" " * self.between_border_space}{self.right_main_border}'
        self.secondary_full_bar = f'{self.secondary_pad}{self.border_character * self.options_width}{self.end}'

    def display_welcome(self, game_name):
        welcome_screen = self.get_welcome_screen(game_name)
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

    def get_welcome_screen(self, game_name):
        # Top of welcome screen w/ 2 empty lines before game name
        welcome_screen = f'{self.main_full_bar}'
        welcome_screen += f'{self.main_empty_bar}'
        welcome_screen += f'{self.main_full_bar}'
        welcome_screen += f'{self.main_empty_bar}'
        welcome_screen += f'{self.main_empty_bar}'

        # Add each part of the game name on a new line
        for part in game_name:
            line_content = self.center_value_in_space(part, self.between_border_space)
            welcome_screen += f'{self.left_main_border}{line_content}{self.right_main_border}'

        # Two empty lines followed by two full width bars of the border character
        welcome_screen += f'{self.main_empty_bar}'
        welcome_screen += f'{self.main_empty_bar}'
        welcome_screen += f'{self.main_full_bar}'
        welcome_screen += f'{self.main_full_bar}'

        return welcome_screen
        
    def get_game_screen(self, screen_title, left_cell_title, left_cell_data, right_cell_title, right_cell_data):
        # Find the number of columns in each 'cell' of the screen
        left_cell_width = (self.menu_width - (2 * self.border_thickness) - len(self.separator)) // 2
        right_cell_width = self.menu_width - left_cell_width - (len(self.separator) // 2) - self.border_thickness

         # Get the content for the title row
        title_row_width = self.menu_width - (2 * self.border_thickness)
        title_row = self.center_value_in_space(screen_title, title_row_width)

        # Title bar
        game_screen = f'{self.main_full_bar}'
        game_screen += f'{self.left_main_border}{title_row}{self.right_main_border}'
        game_screen += f'{self.main_full_bar}'
        
        # Note - this section will handle left and right cells simultaneously
        # Cell titles
        left_cell_title_label = self.center_value_in_space(left_cell_title, left_cell_width)
        right_cell_title_label = self.center_value_in_space(right_cell_title, right_cell_width)
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
        
        # Game screen closure
        game_screen += f'{self.left_main_border}{self.center_value_in_space(self.separator, self.between_border_space)}{self.right_main_border}'
        game_screen += f'{self.main_full_bar}'
        game_screen += f'{self.main_full_bar}'

        return game_screen


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
                left_formatted.append(self.center_value_in_space(f'NAME: {left_current_data.name}', self.left_cell_width))
                status_line = f'   HEALTH: {left_current_data.get_health()}   POWER: {left_current_data.get_power()}'
                left_formatted.append(f'{status_line}{" " * (len(status_line) - self.left_cell_width)}')
            else:
                left_formatted.append(" " * self.left_cell_width)
                left_formatted.append(" " * self.left_cell_width)

            # Right cell formatting
            if right_current_data:
                right_formatted.append(self.center_value_in_space(f'NAME: {right_current_data.name}', self.right_cell_width))
                status_line = f'   HEALTH: {right_current_data.get_health()}   ENERGY: {right_current_data.get_power()}'
                right_formatted.append(f'{status_line}{" " * (len(status_line) - self.right_cell_width)}')
            else:
                right_formatted.append(" " * self.right_cell_width)
                right_formatted.append(" " * self.right_cell_width)

        return (left_formatted, right_formatted)

    def get_welcome_options(self):
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

    def center_value_in_space(self, value, total_width):
        left_pad = (total_width - len(value)) // 2
        right_pad = total_width - left_pad - len(value)
        return f'{" " * left_pad}{value}{" " * right_pad}'

    def tests(self):
        print("Testing internal variables")
        print(self.left_main_border)
        print(self.left_secondary_border)
        print(self.right_main_border)
        print(self.right_secondary_border)
        print(self.main_full_bar)
        print(self.main_empty_bar)

        self.display_welcome(['WELCOME TO', 'ROBOTS', 'VS.', 'DINOSAURS'])

