import random


def game(team1, team2):
    scores = [0, 1, 2, 3, 4, 5, 6, 7]
    score_team1, score_team2 = tuple(random.sample(scores, 2))
    winner = team1 if score_team1 > score_team2 else team2
    return score_team1, score_team2, winner


def stage(stage_num, teams):
    winner = []
    for i in range(stage_num):
        player1 = random.choice(teams)
        teams.remove(player1)
        player2 = random.choice(teams)
        teams.remove(player2)
        score1, score2, win = game(player1, player2)
        winner.append(win)
        print('{} {}:{} {}'.format(player1, score1, score2, player2))
    return winner



winner_4 = []
winner_2 = []


team1 = 'Russia'
team2 = 'Spain'
team3 = 'Italy'
team4 = 'USA'
team5 = 'UK'
team6 = 'Germany'
team7 = 'Belguim'
team8 = 'Japan'

team = [team1, team2, team3, team4, team5, team6, team7, team8]

stage_num = 4
print('\n---1/4 stage---')
winner_4 = stage(stage_num, team)

print('\n---1/2 stage---')
winner_2  = stage(2, winner_4)

print('\n---Finale---')
winner = stage(1, winner_2)


