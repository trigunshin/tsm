class DE:
	def __init__(self, reagent_per_craft, reagent_price, name="None"):
		self.reagent_per_craft = reagent_per_craft
		self.reagent_price = reagent_price
		self.name = name
		# DE constants
		self.dust_per_shard = 20
		self.base_dust_per_de = 10
		self.shard_percent = .13
		self.dust_percent = 1 - self.shard_percent

	def _results_per_destroy(self):
		return self.dust_percent * self.base_dust_per_de + self.shard_percent * self.dust_per_shard
	
	def price(self):
		# use a function to allow editing of the object
		reagent_per_result = self.reagent_per_craft / self._results_per_destroy()
		break_even = (reagent_per_result * self.reagent_price)
		return break_even

	def p(self):
		return self.price()/100/100

class Ore(DE):
	def __init__(self, reagent_price):
		# ignore 30/30 crafts, they can be reflected in price
		DE.__init__(self, 60, reagent_price, 'ore')

class Ink(DE):
	def __init__(self, reagent_price):
		DE.__init__(self, 20, self.ink_price(reagent_price), 'ink')

	def ink_price(self, average_herb_cost):
		# price * 5 herbs / 2.3 inks (err on underestimating x3 ink proc)
		return average_herb_cost * 5 / 2.3

def info():
	# note: 1000 ore ~= 200 dust
	o_90 = Ore(9000)
	o_80 = Ore(8000)
	o_70 = Ore(7000)
	o_60 = Ore(6000)
	ores = [o_90, o_80, o_70, o_60]

	i15 = Ink(15000)
	i105 = Ink(10500)
	i1 = Ink(10000)
	i09 = Ink(9000)
	inks = [i15, i105, i1, i09]

	for cur in [ores, inks]:
		for reagent, result in [(d.reagent_price, d.p()) for d in cur]:
			print 'name:%s\treagent: %i\tresult_cost:%f' % (d.name, reagent, result)


# starflower @ 

# note: 1000 ore ~= 200 dust
o_90 = Ore(9000)
o_80 = Ore(8000)
o_70 = Ore(7000)
o_60 = Ore(6000)

possibilities = [o_90, o_80, o_70, o_60]
[d.p() for d in possibilities]

i15 = Ink(15000)
i105 = Ink(10500)
i1 = Ink(10000)
i09 = Ink(9000)
inks = [i15, i1, i09]
[d.p() for d in inks]
