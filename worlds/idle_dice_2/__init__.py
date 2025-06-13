from typing import List, Mapping, Any

from BaseClasses import MultiWorld, Item, Region
from worlds.AutoWorld import WebWorld, World
from .items import ID2Item, card_items
from .locations import card_unlocks, location_table
from .options import ID2Options
from .regions import get_regions


class ID2Web(WebWorld):
    rich_text_options_doc = True
    theme = "partyTime"


class ID2World(World):
    """
    Idle Dice 2 is a sequel to the popular dice simulation game Idle Dice, developed by Lutsgames. 
    It expands on the gameplay of its predecessor and adds more features such as more dice, more cards, and the ability to create your own deck.
    """
    game = "Idle Dice 2"
    options_dataclass = ID2Options
    options: ID2Options
    topology_present = True
    web = ID2Web() 
    base_id = 2238180 # Steam app ID for ID2
    item_name_to_id = {name: id for id, name in enumerate(card_items.keys(), base_id)}
    location_name_to_id = {name: id for id, name in enumerate(location_table.keys(), base_id)}

    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)

    def create_item(self, name: str) -> Item:
        return ID2Item(name, card_items[name], self.item_name_to_id[name], self.player)
    
    def create_regions(self) -> None:
        self.multiworld.regions.extend(get_regions(self.location_name_to_id, self.player, self.multiworld))

    def create_items(self) -> None:
        self.multiworld.itempool.extend([self.create_item(key) for key in card_items])

    def fill_slot_data(self) -> Mapping[str, Any]:
        return self.options.as_dict("do_you_like_waffles")