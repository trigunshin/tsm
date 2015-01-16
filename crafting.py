
def hexweave_bag_base(earth_price):
	return 10 * earth_price
def hexweave_bag(hexweave_bag_price, earth_price, **kwargs):
	return (hexweave_bag_price - hexweave_bag_base(earth_price))/100
def hexweave_essence_base(blood_price, water_price):
	return 15 * blood_price + 30 * water_price
def hexweave_essence(hexweave_essence_price, blood_price, water_price, **kwargs):
	return (hexweave_essence_price - hexweave_essence_base(blood_price, water_price)) /150
def greater_hexweave_essence_base(blood_price, air_price):
	return 15 * blood_price + 40 * air_price
def greater_hexweave_essence(greater_hexweave_essence_price, blood_price, air_price, **kwargs):
	return (greater_hexweave_essence_price - greater_hexweave_essence_base(blood_price, air_price)) /200

tailoring = {
	'misc': {
		'bag': hexweave_bag,
	},
	'armor': {
		'essence': hexweave_essence,
		'greater_essence': greater_hexweave_essence
	}
}


def truesteel_essence_base(blood_price, earth_price):
	return 15 * blood_price+ 30 * earth_price
def truesteel_essence(truesteel_essence_price, blood_price, earth_price, **kwargs):
	return (truesteel_essence_price - truesteel_essence_base(blood_price, earth_price)) /150
def greater_truesteel_essence_base(blood_price, fire_price):
	return 15 * blood_price+ 40 * fire_price
def greater_truesteel_essence(greater_truesteel_essence_price, blood_price, fire_price, **kwargs):
	return (greater_truesteel_essence_price - greater_truesteel_essence_base(blood_price, fire_price)) /200
def steelforged_essence_base(blood_price, earth_price):
	return 15 * blood_price+ 30 * earth_price
def steelforged_essence(steelforged_essence_price, blood_price, earth_price, **kwargs):
	return (steelforged_essence_price - steelforged_essence_base(blood_price, earth_price)) /150
def greater_steelforged_essence_base(blood_price, fire_price):
	return 15 * blood_price+ 40 * fire_price
def greater_steelforged_essence(greater_steelforged_essence_price, blood_price, fire_price, **kwargs):
	return (greater_steelforged_essence_price - greater_steelforged_essence_base(blood_price, fire_price)) /200
blacksmithing = {
	"weapons":{
		"essence": steelforged_essence,
		"greater_essence": greater_steelforged_essence
	},
	"armor": {
		"essence": truesteel_essence,
		"greater_essence": greater_truesteel_essence
	}
}

def inferno_tarot_base(blood_price, water_price):
	return 15 * blood_price + 30 * water_price
def inferno_tarot(inferno_tarot_price, blood_price, water_price, **kwargs):
	return (inferno_tarot_price - inferno_tarot_base(blood_price, water_price)) /150
def molten_tarot_base(blood_price, earth_price):
	return 15 * blood_price + 40 * earth_price
def molten_tarot(molten_tarot_price, blood_price, earth_price, **kwargs):
	return (molten_tarot_price - molten_tarot_base(blood_price, earth_price)) /200
def mystical_crystal_base(blood_price, water_price):
	return 15 * blood_price + 30 * water_price
def mystical_crystal(mystical_crystal_price, blood_price, water_price, **kwargs):
	return (mystical_crystal_price - mystical_crystal_base(blood_price, water_price)) /150
def glorious_crystal_base(blood_price, earth_price):
	return 15 * blood_price + 40 * earth_price
def glorious_crystal(glorious_crystal_price, blood_price, earth_price, **kwargs):
	return (glorious_crystal_price - glorious_crystal_base(blood_price, earth_price)) /200
inscription = {
	"weapons":{
		"essence": mystical_crystal,
		"greater_essence": glorious_crystal
	},
	"trinkets": {
		"essence": inferno_tarot,
		"greater_essence": molten_tarot
	}
}

priceme = [
	("wep_essence", blacksmithing['weapons']['essence']),
	("greater_wep_essence", blacksmithing['weapons']['greater_essence']),
	("armor_essence", blacksmithing['armor']['essence']),
	("greater_armor_essence", blacksmithing['armor']['greater_essence']),

	("bag", tailoring['misc']['bag']),
	("armor_essence", tailoring['armor']['essence']),
	("greater_armor_essence", tailoring['armor']['greater_essence']),

	("wep_essence", inscription['weapons']['essence']),
	("greater_wep_essence", inscription['weapons']['greater_essence']),
	("trinket_essence", inscription['trinkets']['essence']),
	("greater_trinket_essence", inscription['trinkets']['greater_essence']),
]
mats = dict(
	water_price=3000.,
	fire_price=3100.,
	air_price=4300.,
	earth_price=7000.,
	blood_price=80000.,

	hexweave_bag_price=600000.,
	hexweave_essence_price=2800000,
	greater_hexweave_essence_price=3000000,

	truesteel_essence_price=3000000,
	greater_truesteel_essence_price=3000000,
	steelforged_essence_price=3000000,
	greater_steelforged_essence_price=3000000,

	mystical_crystal_price=3100000.,
	glorious_crystal_price=4000000.,
	inferno_tarot_price=2700000.,
	molten_tarot_price=3100000.)
format_string = "{:<30} {: ^11.3f}"
for name, cur in priceme:
	print format_string.format(name, cur(**mats)/100)
	#print name, "\t\t\t\t", cur(**mats)/100
