from typing import Dict, Tuple, Optional

from BaseClasses import LocationProgressType as ProgType, Location, Region, LocationProgressType

card_unlocks: Dict[str, Tuple[str, ProgType]] = {
    "Unlock Card: 1": ("Card Unlocks", ProgType.PRIORITY ), # Have 104 Draws at once
    #"Unlock Card: 2": ("Card Unlocks", ProgType.PRIORITY ), # 
    #"Unlock Card: 3": ("Card Unlocks", ProgType.PRIORITY ), # 
    #"Unlock Card: 4": ("Card Unlocks", ProgType.PRIORITY ), # 
    #"Unlock Card: 5": ("Card Unlocks", ProgType.PRIORITY ), # 
    #"Unlock Card: 6": ("Card Unlocks", ProgType.PRIORITY ), # 
    #"Unlock Card: 7": ("Card Unlocks", ProgType.PRIORITY ), # 
    #"Unlock Card: 8": ("Card Unlocks", ProgType.PRIORITY ), # 
    #"Unlock Card: 9": ("Card Unlocks", ProgType.PRIORITY ), # 
    #"Unlock Card: 10": ("Card Unlocks", ProgType.PRIORITY ), # 
    "Unlock Card: 11": ("Card Unlocks", ProgType.DEFAULT ), # Earn a total of 1e33 money
    "Unlock Card: 12": ("Card Unlocks", ProgType.PRIORITY ), # Earn a total of 1e36 money
    "Unlock Card: 13": ("Card Unlocks", ProgType.PRIORITY ), # Earn a total of 1e39 money
    "Unlock Card: 14": ("Card Unlocks", ProgType.PRIORITY ), # Earn a total of 1e42 money
    "Unlock Card: 15": ("Card Unlocks", ProgType.PRIORITY ), # Earn a total of 1e45 money
    "Unlock Card: 16": ("Card Unlocks", ProgType.PRIORITY ), # Complete 2 decks in 1 minute in a run
    "Unlock Card: 17": ("Card Unlocks", ProgType.PRIORITY ), # Complete 3 decks in under 1 minute in a run
    "Unlock Card: 18": ("Card Unlocks", ProgType.PRIORITY ), # Complete the Unascended Challenge
    "Unlock Card: 19": ("Card Unlocks", ProgType.PRIORITY ), # Draw a total of 320 cards
    "Unlock Card: 20": ("Card Unlocks", ProgType.PRIORITY ), # Complete 1 deck in 9.38 seconds
    "Unlock Card: 21": ("Card Unlocks", ProgType.PRIORITY ), # Earn a total of 1e63 money
    "Unlock Card: 22": ("Card Unlocks", ProgType.PRIORITY ), # Earn a total of 1e66 money
    "Unlock Card: 23": ("Card Unlocks", ProgType.PRIORITY ), # Earn a total of 1e69 money
    "Unlock Card: 24": ("Card Unlocks", ProgType.PRIORITY ), # Earn a total of 1e72 money
    "Unlock Card: 25": ("Card Unlocks", ProgType.PRIORITY ), # Earn a total of 1e75 money
    "Unlock Card: 26": ("Card Unlocks", ProgType.PRIORITY ), # Complete the Back to Basic Challenge
    "Unlock Card: 31": ("Card Unlocks", ProgType.PRIORITY ), # Earn a total of 1e93 money
    "Unlock Card: 32": ("Card Unlocks", ProgType.PRIORITY ), # Earn a total of 1e96 money
    "Unlock Card: 33": ("Card Unlocks", ProgType.PRIORITY ), # Earn a total of 1e99 money
    "Unlock Card: 34": ("Card Unlocks", ProgType.PRIORITY ), # Earn a total of 1e102 money
    "Unlock Card: 35": ("Card Unlocks", ProgType.PRIORITY ), # Earn a total of 1e105 money
    "Unlock Card: 41": ("Card Unlocks", ProgType.PRIORITY ), # Earn a total of 1e123 money
    "Unlock Card: 42": ("Card Unlocks", ProgType.PRIORITY ), # Earn a total of 1e126 money
    "Unlock Card: 43": ("Card Unlocks", ProgType.PRIORITY ), # Earn a total of 1e129 money
    "Unlock Card: 44": ("Card Unlocks", ProgType.PRIORITY ), # Earn a total of 1e132 money
    "Unlock Card: 45": ("Card Unlocks", ProgType.PRIORITY ), # Earn a total of 1e135 money
    "Unlock Card: 52": ("Card Unlocks", ProgType.PRIORITY ), # Complete 1 deck with 100+ cards
    "Unlock Card: 69": ("Card Unlocks", ProgType.PRIORITY ), # Have 32 gold levels
    "Unlock Card: 111": ("Card Unlocks", ProgType.PRIORITY ), # Get 1e223 money in a single roll
    "Unlock Card: 222": ("Card Unlocks", ProgType.PRIORITY ), # Get 1e445 money in a single roll
    "Unlock Card: 333": ("Card Unlocks", ProgType.PRIORITY ), # Get 1e667 money in a single roll
    "Unlock Card: 360": ("Card Unlocks", ProgType.PRIORITY ), # Have a total of 2500 Wheel spins
    "Unlock Card: 404": ("Card Unlocks", ProgType.PRIORITY ), # Complete 1k decks in a run
    "Unlock Card: 420": ("Card Unlocks", ProgType.PRIORITY ), # Complete 4 decks in 1 minute in a run
    "Unlock Card: 444": ("Card Unlocks", ProgType.PRIORITY ), # Get 1e889 money in a single roll
    "Unlock Card: 524": ("Card Unlocks", ProgType.PRIORITY ), # Complete two deck with 100+ cards
    "Unlock Card: 555": ("Card Unlocks", ProgType.PRIORITY ), # Get 1e1111 money in a single roll
    "Unlock Card: 666": ("Card Unlocks", ProgType.PRIORITY ), # Beat the Cursed Challenge
    "Unlock Card: 777": ("Card Unlocks", ProgType.PRIORITY ), # Have 0 dice rows
    "Unlock Card: 778": ("Card Unlocks", ProgType.PRIORITY ), # Complete 3 decks with 100+ cards
    #"Unlock Card: A": ("Card Unlocks", ProgType.PRIORITY ), # 
    "Unlock Card: ASS": ("Card Unlocks", ProgType.PRIORITY ), # Complete 45 decks in one run
    "Unlock Card: B": ("Card Unlocks", ProgType.PRIORITY ), # Have 10 ore gain
    "Unlock Card: C": ("Card Unlocks", ProgType.PRIORITY ), # Complete the Unwheeled Challenge
    "Unlock Card: C++": ("Card Unlocks", ProgType.PRIORITY ), # Have a total of 256 Gold levels
    "Unlock Card: CC": ("Card Unlocks", ProgType.PRIORITY ), # Beat the Decay Challenge
    "Unlock Card: CD": ("Card Unlocks", ProgType.PRIORITY ), # Roll 0 points 64 times in a row
    "Unlock Card: D": ("Card Unlocks", ProgType.PRIORITY ), # Complete 20 decks in a run
    "Unlock Card: D4": ("Card Unlocks", ProgType.PRIORITY ), # Complete 8 decks in 6.59 seconds in a run
    "Unlock Card: D6": ("Card Unlocks", ProgType.PRIORITY ), # Earn a total of 10k dust
    "Unlock Card: D8": ("Card Unlocks", ProgType.PRIORITY ), # Earn a total of 100k dust
    "Unlock Card: D10": ("Card Unlocks", ProgType.PRIORITY ), # Have 100 ore gain
    "Unlock Card: D12": ("Card Unlocks", ProgType.PRIORITY ), # Earn a total of 10T dust
    "Unlock Card: D20": ("Card Unlocks", ProgType.PRIORITY ), # Earn a total of 1M dust
    "Unlock Card: DP": ("Card Unlocks", ProgType.PRIORITY ), # Complete 4 decks in 5.53 seconds in a run
    "Unlock Card: E": ("Card Unlocks", ProgType.PRIORITY ), # Upgrade dice a total of 10m times
    "Unlock Card: F": ("Card Unlocks", ProgType.PRIORITY ), # Complete 4 decks in a run
    "Unlock Card: G": ("Card Unlocks", ProgType.PRIORITY ), # Complete 3 decks in a run
    "Unlock Card: GG": ("Card Unlocks", ProgType.PRIORITY ), # Have 1024 gild levels
    "Unlock Card: H": ("Card Unlocks", ProgType.PRIORITY ), # 100M total Dust
    "Unlock Card: I": ("Card Unlocks", ProgType.PRIORITY ), # 1B total Dust
    #"Unlock Card: J": ("Card Unlocks", ProgType.PRIORITY ), # 
    "Unlock Card: JA": ("Card Unlocks", ProgType.PRIORITY ), # Have 64 Challenge Multi
    "Unlock Card: JK": ("Card Unlocks", ProgType.PRIORITY ), # Complete the Joker Challenge
    #"Unlock Card: K": ("Card Unlocks", ProgType.PRIORITY ), # 
    "Unlock Card: M": ("Card Unlocks", ProgType.PRIORITY ), # Complete 35 decks in one run
    "Unlock Card: N": ("Card Unlocks", ProgType.PRIORITY ), # Complete 30 decks in one run
    "Unlock Card: O": ("Card Unlocks", ProgType.PRIORITY ), # Complete 25 decks in a run
    "Unlock Card: P": ("Card Unlocks", ProgType.PRIORITY ), # Complete 2 decks in a run
    "Unlock Card: PG": ("Card Unlocks", ProgType.PRIORITY ), # Roll 0 points 16 times in a row
    "Unlock Card: PI": ("Card Unlocks", ProgType.PRIORITY ), # Complete 5 decks in one run
    "Unlock Card: PP": ("Card Unlocks", ProgType.PRIORITY ), # Complete 15 decks in a run
    #"Unlock Card: Q": ("Card Unlocks", ProgType.PRIORITY ), # 
    "Unlock Card: R": ("Card Unlocks", ProgType.PRIORITY ), # Complete 1 deck in 300 seconds in a run
    "Unlock Card: S": ("Card Unlocks", ProgType.PRIORITY ), # Complete 40 decks in one run
    "Unlock Card: T": ("Card Unlocks", ProgType.PRIORITY ), # Complete 2 decks in 1200 seconds in a run
    "Unlock Card: T2": ("Card Unlocks", ProgType.PRIORITY ), # Complete 4 decks in 2400 seconds in a run
    "Unlock Card: T3": ("Card Unlocks", ProgType.PRIORITY ), # Complete 5 decks in 1 minute in a run
    "Unlock Card: T4": ("Card Unlocks", ProgType.PRIORITY ), # Complete 6 decks in a run
    "Unlock Card: U": ("Card Unlocks", ProgType.PRIORITY ), # 10M total Dust
    "Unlock Card: V": ("Card Unlocks", ProgType.PRIORITY ), # 100B total Dust
    "Unlock Card: W": ("Card Unlocks", ProgType.PRIORITY ), # Have a total of 125k Wheel spins
    "Unlock Card: WC": ("Card Unlocks", ProgType.PRIORITY ), # Complete a deck with only one wheel spin
    "Unlock Card: WWW": ("Card Unlocks", ProgType.PRIORITY ), # Have a total of 6.25m Wheel spins
    "Unlock Card: X": ("Card Unlocks", ProgType.PRIORITY ), # Complete 10 decks in 1 run
    "Unlock Card: Y": ("Card Unlocks", ProgType.PRIORITY ), # 10B total Dust
    "Unlock Card: Z": ("Card Unlocks", ProgType.PRIORITY ), # Gain a x2.8 Streak Multi
    "Unlock Card: ZZZ": ("Card Unlocks", ProgType.PRIORITY ), # Roll 0 points 512 times in a row
}

location_table: Dict[str, Tuple[str, ProgType]] = {
    **card_unlocks,
}


class ID2Location(Location):
    game = "Idle Dice 2"

    def __init__(self, player: int, name: str, address: Optional[int], region: Region,
                 progress_type: LocationProgressType):
        super(ID2Location, self).__init__(player, name, address, region)
        self.progress_type = progress_type
