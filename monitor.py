from driver import start, load_urls

undermine_url = "https://theunderminejournal.com/#malganis/item/%d"
armory_url = "https://us.battle.net/wow/en/vault/character/auction/browse?itemId=%d&start=0&end=40&sort=unitBuyout&reverse=false"
alt_armory_url = "https://us.battle.net/wow/en/vault/character/auction/browse?reverse=false&sort=unitBuyout&maxLvl=-1&itemId=%d&minLvl=-1&filterId=-1&start=0&qual=1&end=40"
import items

sel = start()
opened_items = [items.savage_blood, items.temporal_crystal, items.raw_talbuk_meat, items.raw_riverbeast_meat]
urls_to_open = map(lambda x: undermine_url % x.id, opened_items)
load_urls(sel, urls_to_open)

#urls_to_open = map(lambda x: undermine_url % x, items.draenor_boe_epics)
#load_urls(sel, urls_to_open)

# buy monitoring:
#armory_monitor = [items.blackrock_ore, items.true_iron_ore, items.temporal_crystal, items.savage_blood, items.raw_riverbeast_meat, items.everburning_candle.id]
#armory_urls = map(lambda x: armory_url % x.id, armory_monitor)
#load_urls(sel, armory_urls)
#load_urls(sel, [armory_url % items.true_iron_ore.id])

#[k for k in map(lambda x: alt_armory_url % x, items.draenor_herbs)]
#load_urls(sel, [armory_url % items.true_iron_ore.id])
#sel.get(armory_url % items.draenor_herbs[0])

# items = reload(items)


"https://us.battle.net/wow/en/vault/character/auction/browse?reverse=false&sort=unitBuyout&maxLvl=-1&itemId=%d&minLvl=-1&filterId=-1&start=0&qual=1&end=40"

#flytrap
#https://us.battle.net/wow/en/vault/character/auction/browse?reverse=false&sort=unitBuyout&maxLvl=-1&itemId=109126&minLvl=-1&filterId=-1&start=0&qual=1&end=40
109127

