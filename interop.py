class interop:

	def __init__(self):
		self.targetsPreSubmit = []
		self.targetsSubmitted = []
		self.numSubmissions = 0
		self.numTargetsSubmitted = 0
		self.resonse = ""

	def submit_targets(self):
		self.check_for_duplicates()
		

	def check_for_duplicates(self):
		print "dummy duplicate check"