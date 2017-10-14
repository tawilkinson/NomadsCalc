from cmd import Cmd
from enum import Enum

class CliPrompt(Cmd):
	
	def do_quit(self, args):
		"""Quits the program"""
		print("Quitting...")
		raise SystemExit
		
	def do_length(self, args):
		"""Converts lengths into Sheppeys. Call with: length <distance> <unit>. Units: km, miles."""
		self.unit={}
		self.unit["km"] = True
		self.unit["miles"] = False

		if len(args) == 0:
			print("Nothing selected")
			print("1 km is " + str(len_calc(self, 1)) + " Sheppeys")
		elif len(args) == 1:
			print("Please enter 2 arguments: <distance> <unit>.")
		else:
			if args.split(' ')[1] == "km":
				self.unit["km"] = True
				self.unit["miles"] = False
			elif args.split(' ')[1] in "miles":
				self.unit["km"] = False
				self.unit["miles"] = True
			result = len_calc(self, int(args.split(' ')[0]))
			print(str(args.split(' ')[0]) + " " + str(args.split(' ')[1]) + " is " + str(result) + " Sheppeys")
			
	def do_volume(self, args):
		"""Converts volumes into Lambeys. Call with: volume <volume> <unit>. Units: litres, mls, pints."""
		self.unit={}
		self.unit["litre"] = True
		self.unit["ml"] = False
		self.unit["pint"] = False

		if len(args) == 0:
			print("Nothing selected")
			print("1 litre is " + str(vol_calc(self, 1)) + " Lambeys")
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
			result = vol_calc(self, int(args.split(' ')[0]))
			print(str(args.split(' ')[0]) + " " + str(args.split(' ')[1]) + " is " + str(result) + " Lambeys")

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

if __name__ == "__main__":
	prompt = CliPrompt()
	prompt.prompt = ">"
	text = "The Nomadulator!\nA Converter for Nomad Standard Units (NSUs)."
	text += "\nSelect an option:\nlength: convert lengths.\n"
	text += "volume: convert volumes."
	
	prompt.cmdloop(text)