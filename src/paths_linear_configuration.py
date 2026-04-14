import numpy as np
from paths_base_configuration import BaseAnalyticPathConfiguration



class AnalyticLinearPathConfiguration(BaseAnalyticPathConfiguration):

	def __init__(self):
		super().__init__()

	def __repr__(self):
		return "AnalyticLinearPathConfiguration()"

	def initialize_name(self):
		self._name = "Linear Path"

	def initialize_path_key(self):
		self._path_key = "line"

	def initialize_default_facecolor(self):
		self._default_facecolor = "steelblue"

	def initialize_function_mapping(self):
		## dy/dx = y' = m = f'(x)
		## ==> y = mx + b = f(x)
		dy = self.yf - self.yi
		dx = self.xf - self.xi
		m = dy / dx
		bi = self.yi - m * self.xi
		bf = self.yf - m * self.xf
		b = np.mean([
			bi,
			bf])
		function_mapping = {
			"slope" : m,
			"y-intercept" : b,
			}
		self._function_mapping = function_mapping

	def initialize_equation_as_string(self):
		m = self.function_mapping["slope"]
		b = self.function_mapping["y-intercept"]
		equation_as_string = r"$f(x) = {} x + {}$".format(
			self.get_formatted_numerical_value(
				m),
			self.get_formatted_numerical_value(
				b),
			)
		self._equation_as_string = equation_as_string

	def get_y_of_x(self, x):
		m = self.function_mapping["slope"]
		b = self.function_mapping["y-intercept"]
		y_of_x = m * x + b
		return y_of_x

	def get_derivative_of_y_wrt_x(self, x):
		dy_dx = self.function_mapping["slope"]
		return dy_dx

##