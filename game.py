

class Game:

    def selected_winner(self, player_move, ai_move):
        
        if player_move == 'Rock' and ai_move == 'Scissors':
            return 1
        elif player_move == 'Rock' and ai_move == 'Paper':
            return -1
        elif player_move == 'Rock' and ai_move == 'Lizard':
            return 1
        elif player_move == 'Rock' and ai_move == 'Spock':
            return -1
        elif player_move == 'Scissors' and ai_move == 'Rock':
            return -1
        elif player_move == 'Scissors' and ai_move == 'Spock':
            return -1
        elif player_move == 'Scissors' and ai_move == 'Paper':
            return 1
        elif player_move == 'Scissors' and ai_move == 'Lizard': 
            return 1
        elif player_move == 'Spock' and ai_move == 'Scissors':
            return 1
        elif player_move == 'Spock' and ai_move == 'Rock':
            return 1
        elif player_move == 'Spock' and ai_move == 'Lizard':
            return -1
        elif player_move == 'Spock' and ai_move == 'Paper':
            return -1
        elif player_move == 'Lizard' and ai_move == 'Paper':
            return 1
        elif player_move == 'Lizard' and ai_move == 'Spock':
            return 1
        elif player_move == 'Lizard' and ai_move == 'Rock':
            return -1 
        elif player_move == 'Lizard' and ai_move == 'Scissors':
            return -1
        elif player_move == 'Paper' and ai_move == 'Spock':
            return 1
        elif player_move == 'Paper' and ai_move == 'Rock':
            return 1
        elif player_move == 'Paper' and ai_move == 'Scissors':
            return -1
        elif player_move == 'Paper' and ai_move == 'Lizard':
            return -1
        else:
            return 0