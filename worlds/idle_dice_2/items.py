from typing import Dict

from BaseClasses import Item, ItemClassification as IClass

card_items: Dict[str, IClass] = {
    "Card: 1": IClass.progression, # Have 104 Draws at once
    #"Card: 2": IClass.progression, # 
    #"Card: 3": IClass.progression, # 
    #"Card: 4": IClass.progression, # 
    #"Card: 5": IClass.progression, # 
    #"Card: 6": IClass.progression, # 
    #"Card: 7": IClass.progression, # 
    #"Card: 8": IClass.progression, # 
    #"Card: 9": IClass.progression, # 
    #"Card: 10": IClass.progression, # 
    "Card: 11": IClass.useful, # Earn a total of 1e33 money
    "Card: 12": IClass.useful, # Earn a total of 1e36 money
    "Card: 13": IClass.useful, # Earn a total of 1e39 money
    "Card: 14": IClass.useful, # Earn a total of 1e42 money
    "Card: 15": IClass.useful, # Earn a total of 1e45 money
    "Card: 16": IClass.progression, # Complete 2 decks in 1 minute in a run
    "Card: 17": IClass.progression, # Complete 3 decks in under 1 minute in a run
    "Card: 18": IClass.progression, # Complete the Unascended Challenge
    "Card: 19": IClass.progression, # Draw a total of 320 cards
    "Card: 20": IClass.progression, # Complete 1 deck in 9.38 seconds
    "Card: 21": IClass.useful, # Earn a total of 1e63 money
    "Card: 22": IClass.useful, # Earn a total of 1e66 money
    "Card: 23": IClass.useful, # Earn a total of 1e69 money
    "Card: 24": IClass.useful, # Earn a total of 1e72 money
    "Card: 25": IClass.useful, # Earn a total of 1e75 money
    "Card: 26": IClass.progression, # Complete the Back to Basic Challenge
    "Card: 31": IClass.progression, # Earn a total of 1e93 money
    "Card: 32": IClass.progression, # Earn a total of 1e96 money
    "Card: 33": IClass.progression, # Earn a total of 1e99 money
    "Card: 34": IClass.progression, # Earn a total of 1e102 money
    "Card: 35": IClass.progression, # Earn a total of 1e105 money
    "Card: 41": IClass.progression, # Earn a total of 1e123 money
    "Card: 42": IClass.progression, # Earn a total of 1e126 money
    "Card: 43": IClass.progression, # Earn a total of 1e129 money
    "Card: 44": IClass.progression, # Earn a total of 1e132 money
    "Card: 45": IClass.progression, # Earn a total of 1e135 money
    "Card: 52": IClass.progression, # Complete 1 deck with 100+ cards
    "Card: 69": IClass.progression, # Have 32 gold levels
    "Card: 111": IClass.progression, # Get 1e223 money in a single roll
    "Card: 222": IClass.progression, # Get 1e445 money in a single roll
    "Card: 333": IClass.progression, # Get 1e667 money in a single roll
    "Card: 360": IClass.progression, # Have a total of 2500 Wheel spins
    "Card: 404": IClass.progression, # Complete 1k decks in a run
    "Card: 420": IClass.progression, # Complete 4 decks in 1 minute in a run
    "Card: 444": IClass.progression, # Get 1e889 money in a single roll
    "Card: 524": IClass.progression, # Complete two deck with 100+ cards
    "Card: 555": IClass.progression, # Get 1e1111 money in a single roll
    "Card: 666": IClass.progression, # Beat the Cursed Challenge
    "Card: 777": IClass.progression, # Have 0 dice rows
    "Card: 778": IClass.progression, # Complete 3 decks with 100+ cards
    #"Card: A": IClass.progression, # 
    "Card: ASS": IClass.progression, # Complete 45 decks in one run
    "Card: B": IClass.progression, # Have 10 ore gain
    "Card: C": IClass.progression, # Complete the Unwheeled Challenge
    "Card: C++": IClass.progression, # Have a total of 256 Gold levels
    "Card: CC": IClass.progression, # Beat the Decay Challenge
    "Card: CD": IClass.progression, # Roll 0 points 64 times in a row
    "Card: D": IClass.progression, # Complete 20 decks in a run
    "Card: D4": IClass.progression, # Complete 8 decks in 6.59 seconds in a run
    "Card: D6": IClass.progression, # Earn a total of 10k dust
    "Card: D8": IClass.progression, # Earn a total of 100k dust
    "Card: D10": IClass.progression, # Have 100 ore gain
    "Card: D12": IClass.progression, # Earn a total of 10T dust
    "Card: D20": IClass.progression, # Earn a total of 1M dust
    "Card: DP": IClass.progression, # Complete 4 decks in 5.53 seconds in a run
    "Card: E": IClass.progression, # Upgrade dice a total of 10m times
    "Card: F": IClass.progression, # Complete 4 decks in a run
    "Card: G": IClass.progression, # Complete 3 decks in a run
    "Card: GG": IClass.progression, # Have 1024 gild levels
    "Card: H": IClass.progression, # 100M total Dust
    "Card: I": IClass.progression, # 1B total Dust
    #"Card: J": IClass.progression, # 
    "Card: JA": IClass.progression, # Have 64 Challenge Multi
    "Card: JK": IClass.progression, # Complete the Joker Challenge
    #"Card: K": IClass.progression, # 
    "Card: M": IClass.progression, # Complete 35 decks in one run
    "Card: N": IClass.progression, # Complete 30 decks in one run
    "Card: O": IClass.progression, # Complete 25 decks in a run
    "Card: P": IClass.progression, # Complete 2 decks in a run
    "Card: PG": IClass.progression, # Roll 0 points 16 times in a row
    "Card: PI": IClass.progression, # Complete 5 decks in one run
    "Card: PP": IClass.progression, # Complete 15 decks in a run
    #"Card: Q": IClass.progression, # 
    "Card: R": IClass.progression, # Complete 1 deck in 300 seconds in a run
    "Card: S": IClass.progression, # Complete 40 decks in one run
    "Card: T": IClass.progression, # Complete 2 decks in 1200 seconds in a run
    "Card: T2": IClass.progression, # Complete 4 decks in 2400 seconds in a run
    "Card: T3": IClass.progression, # Complete 5 decks in 1 minute in a run
    "Card: T4": IClass.progression, # Complete 6 decks in a run
    "Card: U": IClass.progression, # 10M total Dust
    "Card: V": IClass.progression, # 100B total Dust
    "Card: W": IClass.progression, # Have a total of 125k Wheel spins
    "Card: WC": IClass.progression, # Complete a deck with only one wheel spin
    "Card: WWW": IClass.progression, # Have a total of 6.25m Wheel spins
    "Card: X": IClass.progression, # Complete 10 decks in 1 run
    "Card: Y": IClass.progression, # 10B total Dust
    "Card: Z": IClass.progression, # Gain a x2.8 Streak Multi
    "Card: ZZZ": IClass.progression, # Roll 0 points 512 times in a row
}

class ID2Item(Item):
    game = "Idle Dice 2"
