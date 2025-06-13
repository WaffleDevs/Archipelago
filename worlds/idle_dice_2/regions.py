from typing import List, Dict, Tuple

from BaseClasses import Region, LocationProgressType as ProgType, MultiWorld
from .locations import ID2Location, card_unlocks
from worlds.generic.Rules import set_rule

all_regions = [
    "Menu",
    "Card Unlocks",
]


def get_regions(location_name_to_id: Dict[str, int], player: int, multiworld: MultiWorld) -> List[Region]:

    region_menu = Region("Menu", player, multiworld)
    region_card_unlocks = Region("Card Unlocks", player, multiworld)
    region_menu.connect(region_card_unlocks, "Ingame", lambda state: True)

    for card in card_unlocks:
        location = ID2Location(player, card, location_name_to_id[card], region_card_unlocks, ProgType.DEFAULT)
        region_card_unlocks.locations.append(location)
        set_rule(location, lambda state: state.has(card, player))

    return [region_menu, region_card_unlocks]
