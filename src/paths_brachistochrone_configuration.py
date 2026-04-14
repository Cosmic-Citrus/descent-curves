import numpy as np
from scipy.optimize import fsolve
from paths_base_configuration import BaseAnalyticPathConfiguration



class AnalyticBrachistochronePathConfiguration(BaseAnalyticPathConfiguration):

	def __init__(self):
		super().__init__()

	def __repr__(self):
		return "AnalyticBrachistochronePathConfiguration()"

	def initialize_name(self):
		self._name = "Brachistochrone Path"

	def initialize_path_key(self):
		self._path_key = "brachistochrone"

	def initialize_default_facecolor(self):
		self._default_facecolor = "black"

	def initialize_parametric_status(self):
		self._is_parametric = True

	def initialize_function_mapping(self):
		## start from rest at cusp at theta_i=0
		## solve for theta_f: (1 - cos(theta_f)) / (theta_f - sin(theta_f)) = dy / dx
		dy = self.yf - self.yi
		dx = self.xf - self.xi
		theta_i = 0
		objective = lambda theta_f : (1 - np.cos(theta_f)) / (theta_f - np.sin(theta_f)) + dy / dx
		theta_f = fsolve(
			objective,
			np.pi)[0]
		radius = np.abs(
			dy / (1 - np.cos(theta_f)))
		function_mapping = {
			"radius" : radius,
			"theta" : (theta_i, theta_f),
			}
		self._function_mapping = function_mapping

	def initialize_equation_as_string(self):
		radius = self.function_mapping["radius"]
		x_of_theta = r"$x(\theta) = {} + {} * (\theta - sin\theta)$".format(
			self.get_formatted_numerical_value(
				self.xi),
			self.get_formatted_numerical_value(
				radius),
			)
		y_of_theta = r"$y(\theta) = {} - {} * (1 - cos\theta)$".format(
			self.get_formatted_numerical_value(
				self.yi),
			self.get_formatted_numerical_value(
				radius),
			)
		equation_as_string = "{}, {}".format(
			x_of_theta,
			y_of_theta)
		self._equation_as_string = equation_as_string

	def get_y_of_x(self, x, theta=None):
		if theta is None:
			theta = self.get_theta_of_tau()
		elif not isinstance(theta, np.ndarray):
			raise ValueError("invalid type(theta): {}".format(type(theta)))
		x_of_theta = self.get_x_of_theta(
			theta=theta)
		y_of_theta = self.get_y_of_theta(
			theta=theta)
		y_of_x = np.interp(
			x,
			x_of_theta,
			y_of_theta)
		return y_of_x

	def get_derivative_of_y_wrt_x(self, x, theta=None):
		## slope of cycloid: dy/dx = (dy/dt)/(dx/dt) = -sin(t)/(1-cos(t))
		if theta is None:
			theta = self.get_theta_of_tau()
		elif not isinstance(theta, np.ndarray):
			raise ValueError("invalid type(theta): {}".format(type(theta)))
		x_of_theta = self.get_x_of_theta(
			theta=theta)
		theta_interp = np.interp(
			x,
			x_of_theta,
			theta)
		if theta_interp > 1e-9:
			dy_dx = -1 * np.sin(theta_interp) / (1 - np.cos(theta_interp))
		else:
			dy_dx = 1e-9
		return dy_dx

	def get_theta_of_tau(self, number_sample_positions=100):
		(theta_i, theta_f) = self.function_mapping["theta"]
		theta = np.linspace(
			theta_i,
			theta_f,
			number_sample_positions)
		return theta

	def get_y_of_theta(self, theta, r=None):
		if r is None:
			r = self.function_mapping["radius"]
		elif not isinstance(r, (int, float)):
			raise ValueError("invalid type(r): {}".format(type(r)))
		y = self.yi - r * (1 - np.cos(theta))
		return y

	def get_x_of_theta(self, theta, r=None):
		if r is None:
			r = self.function_mapping["radius"]
		elif not isinstance(r, (int, float)):
			raise ValueError("invalid type(r): {}".format(type(r)))
		x = self.xi + r * (theta - np.sin(theta))
		return x

	def get_x_of_tau(self, number_sample_positions=100):
		theta = self.get_theta_of_tau(
			number_sample_positions=number_sample_positions)
		x = self.get_x_of_theta(
			theta=theta)
		return x

##