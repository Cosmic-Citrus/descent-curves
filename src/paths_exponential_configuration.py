import numpy as np
from paths_base_configuration import BaseAnalyticPathConfiguration



class AnalyticExponentialPathConfiguration(BaseAnalyticPathConfiguration):

	def __init__(self):
		super().__init__()

	def __repr__(self):
		return "AnalyticExponentialPathConfiguration()"

	def initialize_name(self):
		self._name = "Exponential Path"

	def initialize_path_key(self):
		self._path_key = "exponential"

	def initialize_default_facecolor(self):
		self._default_facecolor = "darkorange"

	def initialize_function_mapping(self):
		## f(x) = a exp(- b x)
		## ==> yf / yi = exp(b * (xi - xf))
		try:
			b = np.log(self.yf / self.yi) / (self.xi - self.xf)
		except ZeroDivisionError:
			raise ValueError("a different initial_position is needed to generate an exponential path")
		a = np.mean([
			self.yi * np.exp(b * self.xi),
			self.yf * np.exp(b * self.xf)])
		function_mapping = {
			"initial amplitude" : a,
			"decay constant" : b,
			}
		self._function_mapping = function_mapping

	def initialize_equation_as_string(self):
		a = self.function_mapping["initial amplitude"]
		b = self.function_mapping["decay constant"]
		equation_as_string = r"$f(x) = {} exp(- {} x)$".format(
			self.get_formatted_numerical_value(
				a),
			self.get_formatted_numerical_value(
				b),
			)
		self._equation_as_string = equation_as_string

	def get_y_of_x(self, x):
		a = self.function_mapping["initial amplitude"]
		b = self.function_mapping["decay constant"]
		y_of_x = a * np.exp(-1 * b * x)
		return y_of_x

	def get_derivative_of_y_wrt_x(self, x):
		a = self.function_mapping["initial amplitude"]
		b = self.function_mapping["decay constant"]
		dy_dx = -1 * b * self.get_y_of_x(x)
		return dy_dx

##