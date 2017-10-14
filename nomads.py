from cmd import Cmd
from enum import Enum

class CliPrompt(Cmd):
	
	def do_quit(self, args):
		"""Quits the program"""
		print("Quitting...")
		raise SystemExit
		
	def do_length(self, args):
		"""Converts lengths into Sheppeys. Call with: length <distance> <unit>.\nUnits: km, miles."""
		self.unit={}
		self.unit["km"] = True
		self.unit["miles"] = False

		if len(args) == 0:
			print("Nothing selected")
			result = len_calc(self, 1)
			print("1 km is {:0.2f} Sheppeys".format(result))
		elif len(args) == 1:
			print("Please enter 2 arguments: <distance> <unit>.")
		else:
			if args.split(' ')[1] == "km":
				self.unit["km"] = True
				self.unit["miles"] = False
			elif args.split(' ')[1] in "miles":
				self.unit["km"] = False
				self.unit["miles"] = True
			result = len_calc(self, float(args.split(' ')[0]))
			print(str(args.split(' ')[0]) + " " + str(args.split(' ')[1]) + " is {:0.2f} Sheppeys".format(result))
			
	def do_volume(self, args):
		"""Converts volumes into Lambeys. Call with: volume <volume> <unit>.\nUnits: litres, mls, pints."""
		self.unit={}
		self.unit["litre"] = True
		self.unit["ml"] = False
		self.unit["pint"] = False

		if len(args) == 0:
			print("Nothing selected")
			result = vol_calc(self, 1)
			print("1 litre is {:0.2f} Lambeys".format(result))
		elif len(args) == 1:
			print("Please enter 2 arguments: <volume> <unit>.")
		else:
			if args.split(' ')[1] == "litres":
				self.unit["litre"] = True
				self.unit["ml"] = False
				self.unit["pint"] = False
			elif args.split(' ')[1] in "mls":
				self.unit["litre"] = False
				self.unit["ml"] = True
				self.unit["pint"] = False
			elif args.split(' ')[1] in "pints":
				self.unit["litre"] = False
				self.unit["ml"] = False
				self.unit["pint"] = True
			result = vol_calc(self, float(args.split(' ')[0]))
			print(str(args.split(' ')[0]) + " " + str(args.split(' ')[1]) + " is {:0.2f} Lambeys".format(result))
			
	def do_time(self, args):
		"""Converts times into Brew. Call with: time <time> <unit>.\nUnits: mins, hours, <t> hours <t> minutes."""
		self.unit={}
		self.unit["min"] = True
		self.unit["hour"] = False
		
		try:
			if args.split(' ')[1] in "hours" and args.split(' ')[3] in "minutes":
				mins = float(args.split(' ')[0])*60 + float(args.split(' ')[2])
				result = time_calc(self, mins)
				print(str(mins) + " minutes" + " is {:0.2f} Brews".format(result))
		except IndexError:
			if len(args) == 0:
				print("Nothing selected")
				result = time_calc(self, 4)
				print("4 minutes is {:0.2f} Brews".format(result))
			elif len(args) == 1:
				print("Please enter 2 arguments: <volume> <unit>.")
			else:
				if args.split(' ')[1] == "minutes":
					self.unit["min"] = True
					self.unit["hour"] = False
				elif args.split(' ')[1] in "hours":
					self.unit["min"] = False
					self.unit["hour"] = True
				result = time_calc(self, float(args.split(' ')[0]))
				print(str(args.split(' ')[0]) + " " + str(args.split(' ')[1]) + " is {:0.2f} Brews".format(result))

def len_calc(self, input):
	if self.unit.get("miles", False):
		return input * 0.86992
	elif self.unit.get("km", False):
		return input / 1.4
	else:
		raise TypeError
		
def vol_calc(self, input):
	if self.unit.get("litre", False):
		return (input * 1000) / 404
	elif self.unit.get("ml", False):
		return input / 404
	elif self.unit.get("pint", False):
		return (input * 568.2613) / 404
	else:
		raise TypeError
		
def time_calc(self, input):
	if self.unit.get("min", False):
		return input / 4
	elif self.unit.get("hour", False):
		return input * 15
	else:
		raise TypeError

if __name__ == "__main__":
	prompt = CliPrompt()
	prompt.prompt = ">"
	text = "The Nomadulator!\nA Converter for Nomad Standard Units (NSUs)."
	text += "\nSelect an option:\nlength: convert lengths.\n"
	text += "volume: convert volumes.\n"
	text += "time: converts times."
	
	prompt.cmdloop(text)