class Item:
	def __init__(self, item_id, item_name):
		self.id = item_id
		self.name = item_name

class Craftables
	def __init__(self):
		pass

cord_of_winsome_sorrows = Item(119336, "Cord of Winsome Sorrows")
everburning_candle = Item(118880, "Everburning Candle")

savage_blood = Item(118472, "Savage Blood")

sorcerous_air = Item(113264, "Sorcerous Air")
sorcerous_earth = Item(113263, "Sorcerous Earth")
sorcerous_water = Item(113262, "Sorcerous Water")
sorcerous_fire = Item(113261, "Sorcerous Fire")

temporal_crystal = Item(113588, "Temporal Crystal")
luminous_shard = Item(111245, "Luminous Shard")
draenic_dust = Item(109693, "Draenic Dust")

blackrock_ore = Item(109118, "Blackrock Ore")
true_iron_ore = Item(109119, "True Iron Ore")

raw_talbuk_meat = Item(109132, "Raw Talbuk Meat")
rylak_egg = Item(109133, "Rylak Egg")
raw_elekk_meat = Item(109134, "Raw Elekk Meat")
raw_riverbeast_meat = Item(109135, "Raw Riverbeast Meat")
raw_boar_meat = Item(109136, "Raw Boar Meat")

# buy @ like 30g?
imperfect_draenethyst_fragment = Item(10593, "Imperfect Draenethyst Fragment")
flawless_draenethyst_sphere = Item(8244, "Flawless Draenethyst Sphere")

talador_orchid = Item(109129, "Talador Orchid")
nagrand_arrowbloom = Item(109128, "Nagrand Arrowbloom")
starflower = Item(109127, "Starflower")
gorgrond_flytrap = Item(109126, "Gorgrond Flytrap")
fireweed = Item(109125, "Fireweed")
frostweed = Item(109124, "Frostweed")

draenor_boe_epic_ids = [113593,113602,113610,113632,113865,113882,113932,113959,118808,118810,118812,118814,118816,118840,118842,118844,118846,118848,118851,118852,118862,118864,118866,118868,118870,118872,118874,118876,118878,118880,118882,118884,118885,118886,118887,118888,118889,118890,118891,118892,118893,118894,118895,118896,119331,119332,119333,119334,119335,119336,119337,119338,119339,119340,119341,119342,119343,119344,119345,119346,119347,120077]
draenor_herbs = [talador_orchid, nagrand_arrowbloom, starflower, gorgrond_flytrap, fireweed, frostweed]


draenor_ores = [blackrock_ore.id, true_iron_ore.id]
draenor_enchanting = [temporal_crystal.id, luminous_shard.id, draenic_dust.id]
sorcerous = [c.id for c in [sorcerous_air, sorcerous_earth, sorcerous_fire, sorcerous_water]]