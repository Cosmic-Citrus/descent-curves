import numpy as np
from paths_base_configuration import BaseAnalyticPathConfiguration



class AnalyticEllipticalPathConfiguration(BaseAnalyticPathConfiguration):

	def __init__(self):
		super().__init__()

	def __repr__(self):
		return "AnalyticEllipticalPathConfiguration()"

	def initialize_name(self):
		self._name = "Elliptical Path (one quadrant)"

	def initialize_path_key(self):
		self._path_key = "ellipse"

	def initialize_default_facecolor(self):
		self._default_facecolor = "red"

	def initialize_function_mapping(self):
		## center (h, k) ~ (xf, yi)
		## (x-h)^2 / a^2 + (y-k)^2 / b^2 = 1
		## ==> y = k ± b * sqrt(1 - (x-h)^2 / a^2)
		a = np.abs(
			self.xf - self.xi)
		b = np.abs(
			self.yi - self.yf)
		function_mapping = {
			"x-radius" : a,
			"y-radius" : b,
			}
		self._function_mapping = function_mapping

	def initialize_equation_as_string(self):
		a = self.function_mapping["x-radius"]
		b = self.function_mapping["y-radius"]
		fraction_label = r"\left(\frac{{x - {}}}{{{}}}\right)^2".format(
			self.get_formatted_numerical_value(
				self.xf),
			self.get_formatted_numerical_value(
				a),
			)
		equation_as_string = r"$f(x) = {} - {} \sqrt{{1 - {}}}$".format(
			self.get_formatted_numerical_value(
				self.yi),
			self.get_formatted_numerical_value(
				b),
			fraction_label,
			)
		self._equation_as_string = equation_as_string

	def get_y_of_x(self, x):
		a = self.function_mapping["x-radius"]
		b = self.function_mapping["y-radius"]
		y_of_x = self.yi - b * np.sqrt(1 - np.square((x - self.xf) / a))
		return y_of_x

	def get_derivative_of_y_wrt_x(self, x):
		a = self.function_mapping["x-radius"]
		b = self.function_mapping["y-radius"]
		dy_dx = b * (x - self.xf) / (np.square(a) * np.sqrt(1 - np.square((x - self.xf)/a)))
		return dy_dx

##