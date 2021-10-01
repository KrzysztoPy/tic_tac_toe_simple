from main_menu.menu_options.static_text.start_game_text import restrict_name_is_empty_or_null
import random

symbols_to_play = ('X', 'Y')


class New_match:
    __first_player = ['', '']
    __second_player = ['', '']

    @property
    def first_player(self):
        return self.__first_player

    @first_player.setter
    def first_player(self, data, position):
        self.__first_player[position] = data


    def set_player_name(self):
        while True:
            player_name = self.which_player_name_is_correct_with_name_restriction(input())
            if player_name is not None:
                return player_name

    @staticmethod
    def which_player_name_is_correct_with_name_restriction(player_name):
        if player_name == '' or player_name is None:
            restrict_name_is_empty_or_null()
            return None
        else:
            return player_name

    # def draw_who_play_x_and_who_o(self):
    #     if random.randint(0, 1):
    #         print(starting_x_o_txt(symbols_to_play[0]))
    #         first_player = symbols_to_play[0]
    #         second_player = symbols_to_play[1]
    #     else:
    #         print(starting_x_o_txt(symbols_to_play[1]))
    #         first_player = symbols_to_play[1]
    #         second_player = symbols_to_play[0]

    def draw_who_starts(self):
        pass
