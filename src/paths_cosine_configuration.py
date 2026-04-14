import numpy as np
from paths_base_configuration import BaseAnalyticPathConfiguration



class AnalyticCosinePathConfiguration(BaseAnalyticPathConfiguration):

	def __init__(self):
		super().__init__()

	def __repr__(self):
		return "AnalyticCosinePathConfiguration()"

	def initialize_name(self):
		self._name = "Cosine Path (half-period)"

	def initialize_path_key(self):
		self._path_key = "cosine"

	def initialize_default_facecolor(self):
		self._default_facecolor = "mediumorchid"

	def initialize_function_mapping(self):
		##
		## f(x) = a cos(b (x-c)) + d
		## a ~ amplitude
		## b ~ coefficient
		## c ~ phase-shift
		## d ~ vertical-shift
		## ==> f'(x) = -ab sin(b (x-c))
		##
		# a = (self.yf - self.yi) / 2
		# period = 2 * abs(
		# 	self.xf - self.xi)
		# b = np.pi / period
		# c = -1 * self.xi / b
		# d = (self.yf + self.yi) / 2
		##
		a = (self.yf - self.yi) / 2
		period = 2 * abs(
			self.xf - self.xi)
		b = 2 * np.pi / period
		c = float(
			self.xi + period / 2)
		d = (self.yf + self.yi) / 2
		function_mapping = {
			"amplitude" : a,
			"inverse-period scale" : b,
			"phase shift" : c,
			"vertical shift" : d,
			}
		self._function_mapping = function_mapping

	def initialize_equation_as_string(self):
		a = self.function_mapping["amplitude"]
		b = self.function_mapping["inverse-period scale"]
		c = self.function_mapping["phase shift"]
		d = self.function_mapping["vertical shift"]
		equation_as_string = r"$f(x) = {} cos({} (x-{})) + {}$".format(
			self.get_formatted_numerical_value(
				a),
			self.get_formatted_numerical_value(
				b),
			self.get_formatted_numerical_value(
				c),
			self.get_formatted_numerical_value(
				d),
			)
		self._equation_as_string = equation_as_string

	def get_y_of_x(self, x):
		a = self.function_mapping["amplitude"]
		b = self.function_mapping["inverse-period scale"]
		c = self.function_mapping["phase shift"]
		d = self.function_mapping["vertical shift"]
		y_of_x = a * np.cos(b * (x - c)) + d
		return y_of_x

	def get_derivative_of_y_wrt_x(self, x):
		a = self.function_mapping["amplitude"]
		b = self.function_mapping["inverse-period scale"]
		c = self.function_mapping["phase shift"]
		d = self.function_mapping["vertical shift"]
		dy_dx = -1 * a * b * np.sin(b * (x - c))
		return dy_dx

##