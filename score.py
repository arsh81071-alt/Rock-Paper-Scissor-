def update_score(winner, player_score, computer_score):
    if winner == "player":
        player_score += 1
    elif winner == "computer":
        computer_score += 1
    return player_score, computer_score
update_score("player", 0,0)