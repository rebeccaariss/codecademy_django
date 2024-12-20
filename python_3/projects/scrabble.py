letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# ✅ Given the provided table, create a dictionary that maps players to the list of words they've played:
player_to_words = {'player1': ['BLUE', 'TENNIS', 'EXIT'], 'wordNerd': ['EARTH', 'EYES', 'MACHINE'], 'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'], 'Prof Reader': ['ZAP', 'COMA', 'PERIOD']}

# ✅ Initialize empty dictionary for scoring points:
player_to_points = {}

# ✅ Make the letter_to_points dictionary able to handle lowercase inputs as well:
lowercase_letters = [letter.lower() for letter in letters]

for letter in lowercase_letters:
  letters.append(letter)

points = [point for point in points * 2]

# ✅ Combine the provided 'letters' and 'points' lists into a dictionary with letters mapped to their respective point values:
letter_to_points = {key:value for key, value in zip(letters, points)}

# ✅ Update 'letter_to_points' dictionary to account for blank tiles:
letter_to_points[" "] = 0

# ✅ Looping through a given word, return its point value:
def score_word(word):
  point_total = 0

  for letter in word:
    if letter in letter_to_points:
      point_total += letter_to_points[letter]
    else:
      point_total += 0

  return point_total

# ✅ Test function:
# brownie_points = score_word("BROWNIE")
# print(brownie_points)

# ✅ Create a function to update all player point totals when called, looping over 1) players/word lists ('.items') and 2) over each word in the words list:
def update_point_totals():
  # '.items', not '.values', returns tuples with key/value pairs:
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points

# ✅ Create a function that represents a "play", appending the word to the player's word list and calling the update_point_totals function for the latest score:
def play_word(player, word):
  player_to_words[player].append(word)
  update_point_totals()

# ✅ Test for plays & points (including lowercase letters):
play_word('player1', 'HORSE')
print(f'\n{player_to_words}')
print(player_to_points)

play_word('player1', 'BLUE')
print(f'\n{player_to_words}')
print(player_to_points)

play_word('player1', 'peach pie')
print(f'\n{player_to_words}')
print(player_to_points)

#------------------------------------------------------------------------------------------------

# *️⃣ Scrabble project completed for Codecademy's "Learn Python 3" course:
# https://www.codecademy.com/learn/learn-python-3

#------------------------------------------------------------------------------------------------