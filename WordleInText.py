import random
import string

remaining_letters = set(string.ascii_uppercase)

wordlist = ['ABBEY', 'ABYSS', 'BACKS', 'BASIC', 'BEARS', 'RISKY', 'COALS', 'GRAPE', 'GRADE', 'SCORE', 'CLOUD', 'DUMPY', 'PINKY', 'STARE', 'CHOKE', 'SUSUS', 'GRRRL', 'SCARE', 'TRAIN', 'SUGAR', 'SCOOP', 'SHOOT', 'GROWN', 'SHOWN', 'WRYLY', 'CHILD', 'GHOST', 'SNOWY', 'RAINY', 'SHAPE', 'VIVID', 'LUNGE', 'GROUP', 'LUNGS', 'COLES', 'MANLY', 'GODLY', 'TRADE', 'WRONG', 'BRINK', 'BLINK', 'GAMER', 'GAMES', 'BONEY', 'EBONY', 'POUCH', 'SOGGY', 'FOGGY', 'MAMMA', 'MUMMY', 'DADDY', 'DANDY', 'ANGER', 'ANGRY', 'HAPPY', 'HIPPO', 'HIPPY', 'THOSE', 'THINK', 'LIVER', 'DODGE', 'DODGY', 'TASTE', 'WASTE', 'TASTY', 'CASTE', 'PASTE', 'STRAW', 'SHREW', 'BASIS', 'BASIC', 'TIGHT', 'RIGHT', 'MIGHT', 'FIGHT', 'LIGHT', 'MIDST', 'SHINE', 'STERN', 'COURT', 'CACTI', 'CHOMP', 'SKILL', 'TREES', 'FREED', 'FRIED', 'SUPER', 'DUPER', 'GRAIN', 'PLAIN', 'PLANE', 'EAGLE', 'EAGER', 'STAIN', 'STATE', 'RISKS', 'RESET', 'SETUP', 'SLANG', 'SPIED', 'SPIES', 'SPIER', 'FLIER', 'PLIER', 'PLIED', 'GORGE', 'LONER', 'LOWLY', 'STING', 'STINK', 'SLICK', 'FLICK', 'PRISM', 'RADIO', 'RADII', 'AUDIO', 'AVOID', 'CHAIN', 'SCARE', 'MONEY', 'HONEY', 'SHRUG', 'SHRUB', 'SPILL', 'SPILT', 'SUNNY', 'SILLY', 'PILLS', 'FILET', 'THOSE', 'THESE', 'WHOSE', 'CHART', 'FISHY', 'NINNY', 'FEWER', 'CHOSE', 'CHECK', 'CHICK', 'BRICK', 'SHIFT', 'ENTER', 'ENTRY', 'EMBER']
secret = random.choice(wordlist)

max_tries = 6
tries = 0

while tries < max_tries:
    guess = input("type a 5 letter word > ").upper()

    if len(guess) != 5:
        print("must be 5 letters")
        continue

    if guess not in wordlist:
        print("not in wordlist")
        continue

    tries += 1
    for ch in guess:
        if ch in remaining_letters:
            remaining_letters.remove(ch)

    result = []

    for i in range(5):
        if guess[i] == secret[i]:
            result.append("g")   # green
        elif guess[i] in secret:
            result.append("y")   # yellow
        else:
            result.append("w")   # wrong

    print("result:", " ".join(result))
    print("letters left:", " ".join(sorted(remaining_letters)))

    if guess == secret:
        print("u got it")
        break

if guess != secret:
    print("game over the word was", secret)
