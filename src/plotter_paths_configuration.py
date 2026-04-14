import numpy as np
import matplotlib.pyplot as plt
from plotter_base_configuration import BasePlotterConfiguration


class BaseDescentCurvesViewer(BasePlotterConfiguration):

	def __init__(self):
		super().__init__()

	@staticmethod
	def get_path_alpha(number_paths):
		if not isinstance(number_paths, int):
			raise ValueError("invalid type(number_paths): {}".format(type(number_paths)))
		if number_paths < 1:
			raise ValueError("invalid number_paths: {}".format(number_paths))
		if number_paths == 1:
			alpha = 1
		else:
			alpha = 2 / (number_paths + 1)
		return alpha

	@staticmethod
	def get_save_name(path_keys, is_animated=False, is_save=False):
		if is_save:
			if not isinstance(is_animated, bool):
				raise ValueError("invalid type(is_animated): {}".format(type(is_animated)))
			save_name = "-".join([
				path_key
					for path_key in path_keys])
			if is_animated:
				suffix = "-trajectory"
			else:
				suffix = "-path"
			save_name += suffix
		else:
			save_name = None
		return save_name

	def get_path_facecolors(self, path_configurations, cmap=None, facecolors=None):
		if (cmap is None) and (facecolors is None):
			facecolors = [
				path_configuration.default_facecolor
					for path_configuration in path_configurations]
		else:
			raise ValueError("not yet implemented")
		return facecolors

class DescentCurvesPlotFormatConfiguration(BaseDescentCurvesViewer):

	def __init__(self):
		super().__init__()

	def autoformat_plot(self, ax, descent_curves):
		ax = self.visual_settings.autoformat_axis_ticks_and_ticklabels(
			ax=ax,
			x_major_ticks=True,
			x_minor_ticks=True,
			y_major_ticks=True,
			y_minor_ticks=True,
			x_major_ticklabels=True,
			x_minor_ticklabels=False,
			y_major_ticklabels=True,
			y_minor_ticklabels=False)
		ax = self.visual_settings.autoformat_grid(
			ax=ax,
			grid_color="gray")
		xlabel = r"X-axis [$m$]"
		ylabel = r"Y-axis [$m$]"
		title = "Paths from ({}, {}) to ({}, {})".format(
			descent_curves.get_formatted_numerical_value(
				descent_curves.xi),
			descent_curves.get_formatted_numerical_value(
				descent_curves.yi),
			descent_curves.get_formatted_numerical_value(
				descent_curves.xf),
			descent_curves.get_formatted_numerical_value(
				descent_curves.yf),
			)
		# title = "Paths from A to B"
		ax = self.visual_settings.autoformat_axis_labels(
			ax=ax,
			xlabel=xlabel,
			ylabel=ylabel,
			title=title)
		return ax

	def autoformat_legend(self, fig, ax):
		handles, labels = ax.get_legend_handles_labels()
		number_columns = len(
			labels)
		if number_columns > 5:
			if number_columns % 2 == 0:
				number_columns = number_columns // 2
			else:
				number_columns = 4
		leg_title = "Paths"
		leg_kwargs = dict()
		bbox_to_anchor = [
			0,
			-0.1375,
			1,
			1]
		leg_kwargs["bbox_to_anchor"] = bbox_to_anchor
		leg_kwargs["bbox_transform"] = fig.transFigure
		leg = self.visual_settings.get_legend(
			fig=fig,
			ax=ax,
			handles=handles,
			labels=labels,
			number_columns=number_columns,
			title=leg_title,
			**leg_kwargs)
		return fig, ax, leg

class DescentCurvesPlotConfiguration(DescentCurvesPlotFormatConfiguration):

	def __init__(self):
		super().__init__()

	def plot_boundary_coordinates(self, descent_curves, ax, initial_facecolor="black", final_facecolor="black", initial_marker="x", final_marker="x"):
		if (initial_facecolor == final_facecolor) and (initial_marker == final_marker):
			label = "Initial (A)\nand Final (B)\nPositions"
			ax.scatter(
				[descent_curves.xi, descent_curves.xf],
				[descent_curves.yi, descent_curves.yf],
				color=initial_facecolor,
				# label=label,
				marker=initial_marker)
		else:
			initial_label = "Initial Position\nA"
			final_label = "Final Position\nB"
			for x, y, facecolor, marker, label in zip((descent_curves.xi, descent_curves.xf), (descent_curves.yi, descent_curves.yf), (initial_facecolor, final_facecolor), (initial_marker, final_marker), (initial_label, final_label)):
				ax.scatter(
					[x],
					[y],
					color=facecolor,
					# label=label,
					marker=marker)
		# xi_label = descent_curves.get_formatted_numerical_value(
		# 	value=descent_curves.xi)
		# yi_label = descent_curves.get_formatted_numerical_value(
		# 	value=descent_curves.yi)
		# xf_label = descent_curves.get_formatted_numerical_value(
		# 	value=descent_curves.xf)
		# yf_label = descent_curves.get_formatted_numerical_value(
		# 	value=descent_curves.yf)
		# ax.text(
		# 	descent_curves.xi,
		# 	descent_curves.yi,
		# 	"({}, {}) ".format( # A
		# 		xi_label,
		# 		yi_label),
		# 	fontsize=self.visual_settings.text_size,
		# 	horizontalalignment="right",
		# 	verticalalignment="bottom")
		# ax.text(
		# 	descent_curves.xf,
		# 	descent_curves.yf,
		# 	" ({}, {})".format( # B
		# 		xf_label,
		# 		yf_label),
		# 	fontsize=self.visual_settings.text_size,
		# 	horizontalalignment="left",
		# 	verticalalignment="top")
		return ax

	def plot_analytic_path(self, path_configuration, ax, label_methods, facecolor, alpha=1, label_delim=None, number_sample_positions=None):
		if not path_configuration.is_analytic:
			raise ValueError("path_configuration (path_key={}) is not analytic".format(path_configuration.path_key))
		if number_sample_positions is None:
			number_sample_positions = 100
		elif isinstance(number_sample_positions, int):
			if number_sample_positions <= 1:
				raise ValueError("invalid number_sample_positions: {}".format(number_sample_positions))
		else:
			raise ValueError("invalid type(number_sample_positions): {}".format(type(number_sample_positions)))
		label = path_configuration.get_path_label(
			label_methods=label_methods,
			label_delim=label_delim)
		x = path_configuration.get_x_of_tau(
			number_sample_positions=number_sample_positions)
		y = path_configuration.get_y_of_x(
			x=x)
		ax.plot(
			x,
			y,
			color=facecolor,
			label=label,
			alpha=alpha)
		return ax

class DescentCurvesViewer(DescentCurvesPlotConfiguration):

	def __init__(self):
		super().__init__()

	def view_path_trajectories(self, descent_curves, path_keys=None, number_sample_positions=100, label_methods=None, label_delim=None, cmap=None, facecolors=None, figsize=None, is_save=False):
		selected_path_configurations, number_selected_path_configurations = descent_curves.get_path_configurations(
			path_keys=path_keys)
		selected_path_keys = [
			path_configuration.path_key
				for path_configuration in selected_path_configurations]
		number_paths = len(
			selected_path_configurations)
		alpha = self.get_path_alpha(
			number_paths=number_paths)
		selected_facecolors = self.get_path_facecolors(
			path_configurations=selected_path_configurations,
			cmap=cmap,
			facecolors=facecolors)
		fig, ax = plt.subplots(
			figsize=figsize)
		ax.set_aspect(
			"equal")
		self.plot_boundary_coordinates(
			descent_curves=descent_curves,
			ax=ax)
		for path_configuration, facecolor in zip(selected_path_configurations, selected_facecolors):
			ax = self.plot_analytic_path(
				path_configuration=path_configuration,
				ax=ax,
				label_methods=label_methods,
				facecolor=facecolor,
				alpha=alpha,
				label_delim=label_delim)
		self.autoformat_plot(
			ax=ax,
			descent_curves=descent_curves)
		self.autoformat_legend(
			fig=fig,
			ax=ax)
		save_name = self.get_save_name(
			path_keys=selected_path_keys,
			is_animated=False,
			is_save=is_save)
		self.visual_settings.display_image(
			fig=fig,
			save_name=save_name)

	def view_phase_portraits(self, descent_curves, path_keys=None, number_sample_positions=100, facecolors=None, cmap=None, fps=12, figsize=None, is_save=False):
		raise ValueError("not yet implemented")

	def view_frequency_spectrum(self, descent_curves, path_keys=None, number_sample_positions=100, facecolors=None, cmap=None, figsize=None, is_save=False):
		raise ValueError("not yet implemented")

##