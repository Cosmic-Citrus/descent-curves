import numpy as np
from scipy.integrate import quad
from plotter_base_configuration import BasePlotterConfiguration


class BasestPathConfiguration(BasePlotterConfiguration):

	def __init__(self):
		super().__init__()
		self._name = None
		self._path_key = None
		self._function_mapping = None
		self._equation_as_string = None
		self._default_facecolor = None
		self._g_acceleration = None
		self._initial_position = None
		self._final_position = None
		self._xi = None
		self._yi = None
		self._xf = None
		self._yf = None
		self._is_analytic = None
		self._is_parametric = None
		self._arc_length = None
		self._elapsed_duration = None

	@property
	def name(self):
		return self._name
	
	@property
	def path_key(self):
		return self._path_key

	@property
	def function_mapping(self):
		return self._function_mapping
	
	@property
	def equation_as_string(self):
		return self._equation_as_string
	
	@property
	def default_facecolor(self):
		return self._default_facecolor

	@property
	def g_acceleration(self):
		return self._g_acceleration
	
	@property
	def initial_position(self):
		return self._initial_position
	
	@property
	def final_position(self):
		return self._final_position
	
	@property
	def xi(self):
		return self._xi
	
	@property
	def yi(self):
		return self._yi
	
	@property
	def xf(self):
		return self._xf
	
	@property
	def yf(self):
		return self._yf

	@property
	def is_analytic(self):
		return self._is_analytic
	
	@property
	def is_parametric(self):
		return self._is_parametric

	@property
	def arc_length(self):
		return self._arc_length

	@property
	def elapsed_duration(self):
		return self._elapsed_duration

	@staticmethod
	def get_y_of_x(*args, **kwargs):
		raise ValueError("this method should be over-written by a child class")

	@staticmethod
	def get_derivative_of_y_wrt_x(*args, **kwargs):
		raise ValueError("this method should be over-written by a child class")

	@staticmethod
	def get_arc_length(*args, **kwargs):
		raise ValueError("this method should be over-written by a child class")

	@staticmethod
	def get_elapsed_duration(*args, **kwargs):
		raise ValueError("this method should be over-written by a child class")

	@staticmethod
	def get_path_label(*args, **kwargs):
		raise ValueError("this method should be over-written by a child class")

	@staticmethod
	def initialize_name(*args, **kwargs):
		raise ValueError("this method should be over-written by a child class")

	@staticmethod
	def initialize_path_key(*args, **kwargs):
		raise ValueError("this method should be over-written by a child class")

	@staticmethod
	def initialize_function_mapping(*args, **kwargs):
		raise ValueError("this method should be over-written by a child class")

	@staticmethod
	def initialize_equation_as_string(*args, **kwargs):
		raise ValueError("this method should be over-written by a child class")

	@staticmethod
	def initialize_default_facecolor(*args, **kwargs):
		raise ValueError("this method should be over-written by a child class")

	@staticmethod
	def initialize_analytic_status(*args, **kwargs):
		raise ValueError("this method should be over-written by a child class")

	@staticmethod
	def initialize_parametric_status(*args, **kwargs):
		raise ValueError("this method should be over-written by a child class")

	def initialize_gravitational_acceleration(self, g_acceleration):
		if g_acceleration is None:
			g_acceleration = 1
		elif not isinstance(g_acceleration, (int, float)):
			raise ValueError("invalid type(g_acceleration): {}".format(type(g_acceleration)))
		self._g_acceleration = g_acceleration

	def initialize_boundary_coordinates(self, xi, yi, xf, yf):
		names_and_values = (
			("xi", xi),
			("xf", xf),
			("yi", yi),
			("yf", yf))
		for name_and_value in names_and_values:
			(name, value) = name_and_value
			if not isinstance(value, (int, float)):
				raise ValueError("invalid type({}): {}".format(name, type(value)))
		if xi == xf:
			raise ValueError("xi and xf should not be equal")
		if yi == yf:
			raise ValueError("yi and yf should not be equal")
		initial_position = np.array([
			xi,
			yi])
		final_position = np.array([
			xf,
			yf])
		self._initial_position = initial_position
		self._final_position = final_position
		self._xi = xi
		self._yi = yi
		self._xf = xf
		self._yf = yf

	def initialize_arc_length(self):
		arc_length = self.get_arc_length()
		self._arc_length = arc_length

	def initialize_elapsed_duration(self):
		elapsed_duration = self.get_elapsed_duration()
		self._elapsed_duration = elapsed_duration

class BasePathLabelConfiguration(BasestPathConfiguration):

	def __init__(self):
		super().__init__()

	def get_path_label(self, label_methods=None, is_include_boundary_labels=False, label_delim=None):
		label_getter_mapping = self.get_label_mapping()
		modified_label_methods = self.get_autocorrected_label_methods(
			label_methods=label_methods)
		modified_label_delim = self.get_autocorrected_string_delimiter(
			label_delim=label_delim)
		partial_labels = list()
		for label_method in modified_label_methods:
			if label_method not in label_getter_mapping.keys():
				raise ValueError("invalid label_method in label_methods: {}".format(label_method))
			get_partial_label = label_getter_mapping[label_method]
			partial_label = get_partial_label()
			partial_labels.append(
				partial_label)
		path_label = modified_label_delim.join(
			partial_labels)
		return path_label

	def get_label_mapping(self):
		label_getter_mapping = {
			"name" : self.get_name_label,
			"path key" : self.get_path_key_label,
			"equation" : self.get_equation_label,
			"arc-length" : self.get_arc_length_label,
			"elapsed duration" : self.get_elapsed_duration_label,
			}
		return label_getter_mapping

	def get_name_label(self):
		name_label = str(
			self.name)
		return name_label

	def get_path_key_label(self):
		path_key_label = str(
			self.path_key)
		return path_key_label

	def get_equation_label(self):
		equation_label = str(
			self.equation_as_string)
		return equation_label

	def get_arc_length_label(self):
		value_label = self.get_formatted_numerical_value(
			value=self.arc_length)
		arc_length_label = "arc-length: {} m".format(
			value_label)
		return arc_length_label

	def get_elapsed_duration_label(self):
		value_label = self.get_formatted_numerical_value(
			value=self.elapsed_duration)
		elapsed_duration_label = "elapsed duration: {} s".format(
			value_label)
		return elapsed_duration_label

	@staticmethod
	def get_formatted_numerical_value(value):
		if not isinstance(value, (int, float, np.int64)):
			raise ValueError("invalid type(value): {}".format(type(value)))
		if int(value) == value:
			value_label = r"{:,}".format(
				int(
					value))
		else:
			value_label = r"{:,.4}".format(
				value)
		return value_label

	@staticmethod
	def get_autocorrected_string_delimiter(label_delim):
		if label_delim is None:
			modified_label_delim = ""
		elif isinstance(label_delim, str):
			modified_label_delim = label_delim[:]
		else:	
			raise ValueError("invalid type(label_delim): {}".format(type(label_delim)))
		return modified_label_delim

	@staticmethod
	def get_autocorrected_label_methods(label_methods):
		if label_methods is None:
			modified_label_methods = list()
		elif isinstance(label_methods, str):
			modified_label_methods = [label_methods]
		elif isinstance(label_methods, (tuple, list, set)):
			modified_label_methods = list(
				label_methods)
		else:
			raise ValueError("invalid type(label_methods): {}".format(type(label_methods)))
		return modified_label_methods

class BasePathConfiguration(BasePathLabelConfiguration):

	def __init__(self):
		super().__init__()

	def __repr__(self):
		return "BasePathConfiguration()"

	def __str__(self):
		label_methods = (
			"name",
			"path key",
			"equation",
			"arc-length",
			"elapsed duration")
		s = self.get_path_label(
			label_methods=label_methods,
			is_include_boundary_labels=True,
			label_delim="\n")
		return s

	def initialize(self, xi, yi, xf, yf, g_acceleration=None):
		# self.initialize_visual_settings()
		self.initialize_name()
		self.initialize_path_key()
		self.initialize_default_facecolor()
		self.initialize_gravitational_acceleration(
			g_acceleration=g_acceleration)
		self.initialize_boundary_coordinates(
			xi=xi,
			xf=xf,
			yi=yi,
			yf=yf)
		self.initialize_analytic_status()
		self.initialize_parametric_status()
		self.initialize_function_mapping()
		self.initialize_equation_as_string()

	def evaluate(self):
		self.initialize_arc_length()
		self.initialize_elapsed_duration()

class BaseAnalyticPathConfiguration(BasePathConfiguration):

	def __init__(self):
		super().__init__()

	def __repr__(self):
		return "BaseAnalyticPathConfiguration()"

	def initialize_analytic_status(self):
		self._is_analytic = True

	def initialize_parametric_status(self):
		self._is_parametric = False

	def get_arc_length(self):

		def integrand(x):
			y_prime = self.get_derivative_of_y_wrt_x(
				x=x)
			ds_dx = np.sqrt(
				1 + np.square(y_prime))
			return ds_dx

		arc_length, _ = quad(
			integrand,
			self.xi,
			self.xf,
			# limit=100,
			)
		return arc_length

	def get_elapsed_duration(self):

		def integrand(x):
			y = self.get_y_of_x(
				x=x)
			h = self.yi - y
			if h <= 0:
				t = 0
			else:
				v = np.sqrt(
					2 * self.g_acceleration * h)
				y_prime = self.get_derivative_of_y_wrt_x(
					x=x)
				ds_dx = np.sqrt(
					1 + np.square(y_prime))
				t = ds_dx / v
			return t

		elapsed_duration, _ = quad(
			integrand,
			self.xi,
			self.xf,
			# limit=100,
			)
		return elapsed_duration

	def get_x_of_tau(self, number_sample_positions=1000):
		x = np.linspace(
			self.xi,
			self.xf,
			number_sample_positions)
		return x

class BaseStochasticPathConfiguration(BasePathConfiguration):

	def __init__(self):
		super().__init__()

	def __repr__(self):
		return "BaseStochasticPathConfiguration()"

	def initialize_analytic_status(self):
		self._is_analytic = False

	def initialize_parametric_status(self):
		self._is_parametric = False

##