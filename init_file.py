from main_menu.menu_options import displaying_the_name_of_the_game, selecting_an_action_option, \
    data_analysis_for_compilance_with_the_guidelines, go_to_the_selected_option

displaying_the_name_of_the_game()
while True:
    go_to_the_selected_option(data_analysis_for_compilance_with_the_guidelines(selecting_an_action_option()))
