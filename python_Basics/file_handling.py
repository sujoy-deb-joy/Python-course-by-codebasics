# from csv import reader
player_scores = {}
with open('scores.csv', 'r') as file:
    # reader = reader(file)
    for lines in file:
        # print(lines)
        player, score = lines.split(',')
        score = int(score)
        if player in player_scores:
            player_scores[player].append(score)
        else:
            player_scores[player] = [score]

# print(player_scores)

for player, score_list in player_scores.items():
    # print(player, score_list)
    min_score = min(score_list)
    max_score = max(score_list)
    average_score = sum(score_list) / len(score_list)
    print(f"{player} Min score ==> {min_score} max score ==> {max_score} average score ==> {average_score}")
