import random

quotes = ["Nobody exists on purpose. Nobody belongs anywhere. Everybody is going to die. Come watch TV?",
          "Weddings are basically funerals with cake.",
          "I'm sorry, Morty. It's a bummer. In reality you're as dumb as they come.",
          "It's fine, Morty. Everything's fine. There an infinite number of realities, Morty and in a few dozen of those, I got lucky and turned everything back to normal.",
          "Do you really expect the smartest person in the universe to still use toilets, Morty?",
          "They're robots Morty! It's okay to shoot them! They're just robots!",
          "You're not gonna believe this, because it usually never happens, but I made a mistake.",
          "Life is effort, and I'll stop when I die.",
          "I don't get it, and I don't need to.",
          "If I've learned one thing, it's that before you get anywhere in life, you gotta stop listening to yourself.",
          "Well then get your shit together. Get it all together and put it in a backpack, all your shit, so it's together. ...and if you gotta take it somewhere, take it somewhere ya know? Take it to the shit store and sell it, or put it in a shit museum. I don't care what you do, you just gotta get it together... Get your shit together.",
          "As you know, Morty, I've got a lot of enemies in the universe that consider my genius a threat. Galactic terrorists, a few sub-galactic dictators, most of the entire intergalactic government."]

authors = ["Voltaire", "Montesquieu", "Simone de Beauvoir", "Hannah Arendt", "Colette", "George Sand", "Charles Baudelaire", "Marie Curie", "Ada Lovelace", "Alfred de Musset", "Olympe de Gouges"]

#get a random number in a list
def random_pick(list):
    random_num = random.randint(0, len(list) - 1)
    return list[random_num]

#generate the output sentence
def generate_quote(author, quote):
    return '{0} once said: "{1}"\n'.format(author, quote)

#user can generate a random quote by pressing any key but 'B'/'b'
user_input = input('Press any key to get a really cool quote, press B to quit.')

#as long as the user does not press 'B' or 'b' to quit the program, it will keep generating a new quote whenever a key is pressed
while user_input != 'B' and user_input != 'b':
    print(generate_quote(random_pick(authors), random_pick(quotes)))
    user_input = input('Press any key to get another cool quote, press B to quit.\n')
