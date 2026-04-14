import numpy as np
from paths_base_configuration import BaseAnalyticPathConfiguration



class AnalyticParabolicPathConfiguration(BaseAnalyticPathConfiguration):

	def __init__(self):
		super().__init__()

	def __repr__(self):
		return "AnalyticParabolicPathConfiguration()"

	def initialize_name(self):
		self._name = "Parabolic Path (symmetric half)"

	def initialize_path_key(self):
		self._path_key = "parabola"

	def initialize_default_facecolor(self):
		self._default_facecolor = "limegreen"

	def initialize_function_mapping(self):
		## f(x) = a (x - h)^2 + k; (h, k) = (xf, yf)
		## ==> a = (yi - yf) / (xi - xf)^2
		a = (self.yi - self.yf) / np.square(self.xi - self.xf)
		function_mapping = {
			"leading coefficient" : a,
			}
		self._function_mapping = function_mapping

	def initialize_equation_as_string(self):
		a = self.function_mapping["leading coefficient"]
		equation_as_string = r"$f(x) = {} (x - {})^2 + {}$".format(
			self.get_formatted_numerical_value(
				a),
			self.get_formatted_numerical_value(
				self.xf),
			self.get_formatted_numerical_value(
				self.yf),
			)
		self._equation_as_string = equation_as_string

	def get_y_of_x(self, x):
		a = self.function_mapping["leading coefficient"]
		y_of_x = a * np.square(x - self.xf) + self.yf
		return y_of_x

	def get_derivative_of_y_wrt_x(self, x):
		a = self.function_mapping["leading coefficient"]
		dy_dx = 2 * a * (x - self.xf)
		return dy_dx

##