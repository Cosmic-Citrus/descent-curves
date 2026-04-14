import numpy as np
from plotter_paths_configuration import DescentCurvesViewer
from paths_base_configuration import BasePathConfiguration
from paths_linear_configuration import AnalyticLinearPathConfiguration
from paths_parabolic_configuration import AnalyticParabolicPathConfiguration
from paths_elliptical_configuration import AnalyticEllipticalPathConfiguration
from paths_cosine_configuration import AnalyticCosinePathConfiguration
from paths_exponential_configuration import AnalyticExponentialPathConfiguration
from paths_brachistochrone_configuration import AnalyticBrachistochronePathConfiguration



class BaseDescentCurvesConfiguration(BasePathConfiguration):

	def __init__(self):
		super().__init__()
		self._path_configurations_mapping = None
		self._number_path_configurations = None

	@property
	def path_configurations_mapping(self):
		return self._path_configurations_mapping
	
	@property
	def number_path_configurations(self):
		return self._number_path_configurations

	def initialize_name(self):
		self._name = "Descent Curves"

	def pre_initialize_path_configurations_mapping(self):
		self._path_configurations_mapping = dict()
		self._number_path_configurations = 0

	def add_path_configuration(self, cls):
		path_configuration = cls()
		path_configuration.initialize(
			xi=self.xi,
			yi=self.yi,
			xf=self.xf,
			yf=self.yf,
			g_acceleration=self.g_acceleration)
		path_configuration.evaluate()
		if path_configuration.name not in self.path_configurations_mapping.keys():
			self._number_path_configurations += 1
		# self._path_configurations_mapping[path_configuration.name] = path_configuration
		self._path_configurations_mapping[path_configuration.path_key] = path_configuration			

	def get_path_configurations(self, path_keys=None):
		if path_keys is None:
			selected_path_configurations = tuple(
				list(
					self.path_configurations_mapping.values()))
		elif isinstance(path_keys, str):
			if path_keys not in self.path_configurations_mapping.keys():
				raise ValueError("invalid path_keys: {}".format(path_keys))
			selected_path_configurations = tuple([
				self.path_configurations_mapping[path_keys],
				])
		elif isinstance(path_keys, (tuple, list, set)):
			for path_key in path_keys:
				if path_key not in self.path_configurations_mapping.keys():
					raise ValueError("invalid path_key in path_keys; path_key={}".format(path_key))
			selected_path_configurations = tuple([
				self.path_configurations_mapping[path_key]
					for path_key in path_keys])
		else:
			raise ValueError("invalid type(path_keys): {}".format(type(path_keys)))
		number_selected_path_configurations = len(
			selected_path_configurations)
		if number_selected_path_configurations < 1:
			raise ValueError("invalid len(selected_paths_configurations): {}".format(number_selected_path_configurations))
		return selected_path_configurations, number_selected_path_configurations

class DescentCurvesConfiguration(BaseDescentCurvesConfiguration):

	def __init__(self):
		super().__init__()

	def __repr__(self):
		return "DescentCurvesConfiguration()"

	def __str__(self):
		if self.path_configurations_mapping is None:
			s = ""
		else:
			s = "\n".join([
				str(path_configuration)
					for path_configuration in self.path_configurations_mapping.values()])
		return s

	def initialize(self, xi, yi, xf, yf, g_acceleration=1):
		self.initialize_name()
		self.pre_initialize_path_configurations_mapping()
		self.initialize_boundary_coordinates(
			xi=xi,
			xf=xf,
			yi=yi,
			yf=yf)
		self.initialize_gravitational_acceleration(
			g_acceleration=g_acceleration)

	def add_linear_path(self):
		self.add_path_configuration(
			AnalyticLinearPathConfiguration)

	def add_parabolic_path(self):
		self.add_path_configuration(
			AnalyticParabolicPathConfiguration)

	def add_elliptical_path(self):
		self.add_path_configuration(
			AnalyticEllipticalPathConfiguration)

	def add_cosine_path(self):
		self.add_path_configuration(
			AnalyticCosinePathConfiguration)

	def add_exponential_decay_path(self):
		self.add_path_configuration(
			AnalyticExponentialPathConfiguration)

	def add_brachistochrone_path(self):
		self.add_path_configuration(
			AnalyticBrachistochronePathConfiguration)

	def view_path_trajectories(self, *args, **kwargs):
		viewer = DescentCurvesViewer()
		viewer.initialize_visual_settings(
			tick_size=self.visual_settings.tick_size,
			label_size=self.visual_settings.label_size,
			text_size=self.visual_settings.text_size,
			cell_size=self.visual_settings.cell_size,
			title_size=self.visual_settings.title_size)
		viewer.update_save_directory(
			path_to_save_directory=self.visual_settings.path_to_save_directory)
		viewer.view_path_trajectories(
			self, # descent_curves,
			*args,
			**kwargs)







##