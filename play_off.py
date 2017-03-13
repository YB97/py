import random


def game(team1, team2):
    scores = [0, 1, 2, 3, 4, 5, 6, 7]
    score_team1, score_team2 = tuple(random.sample(scores, 2))
    winner = team1 if score_team1 > score_team2 else team2
    return score_team1, score_team2, winner


def out(temp, team):
    for i in range(len(temp[team])):
        print('{} {}:{} {}'.format(team, (temp[team])[i]['home_score'], temp[team][i]['away_score'],
                                   temp[team][i]['opposite']))
    if (len(temp[team]) == 3 and (temp[team])[2]['home_score'] > temp[team][2]['away_score']):
        print('---WINNER---')
    elif len(temp[team]) == 3:
        print('---2ND PLACE---')


def stage(stage_num, teams):
    winner = []
    for i in range(stage_num):
        player1 = random.choice(teams)
        teams.remove(player1)

        player2 = random.choice(teams)
        teams.remove(player2)

        score1, score2, win = game(player1, player2)

        games[player1].append({'home_score': score1, 'away_score': score2, 'opposite': player2})
        games[player2].append({'home_score': score2, 'away_score': score1, 'opposite': player1})

        winner.append(win)
        print('{} {}:{} {}'.format(player1, score1, score2, player2))
    return winner


winner_4 = []
winner_2 = []

team = ['Russia', 'Spain', 'Italy', 'USA', 'UK', 'Germany', 'Belguim', 'Japan']

games = dict()
for team_name in team:
    games[team_name] = []


print('\n---1/4 stage---')
winner_4 = stage(4, team)

print('\n---1/2 stage---')
winner_2 = stage(2, winner_4)


print('\n---Finale---')
winner = stage(1, winner_2)

print(games)
print('\nDo you wanna see exact team results? yes/no')
a = input()
if a.lower() == 'yes':
    print('So, what team?')
    res = input()
    out(games, res)
