class interop:

	def __init__(self):
		self.targetsPreSubmit = []
		self.targetsSubmitted = []
		self.numSubmissions = 0
		self.numTargetsSubmitted = 0

	def submit_all_targets(self):
		self.check_for_edits()
		self.check_for_duplicates()
		
		for targ in targetsPreSubmit:
			self.submit_single_target(targ)

	def submit_single_target(self, targ):
		print "submitting single target"

	def submit_edits(self, targ):
		print "special submission rules for submitting targ"

	def check_for_edits(self):
		print "if target is edit, special condition necessary"
		for targ in targetsPreSubmit:
			if True:
				submit_edits(self, targ)

	def check_for_duplicates(self):
		print "dummy duplicate check"