from descent_curves_configuration import DescentCurvesConfiguration


# is_save, path_to_save_directory = False, None
is_save, path_to_save_directory = True, "/Users/owner/Desktop/programming/curves_of_descent/output/"


if __name__ == "__main__":

	descent_curves = DescentCurvesConfiguration()
	descent_curves.initialize_visual_settings(
		text_size=8)
	descent_curves.update_save_directory(
		path_to_save_directory=path_to_save_directory)

	(xi, yi) = (1, 100)
	(xf, yf) = (100, 1)
	g_acceleration = 9.8

	descent_curves.initialize(
		xi=xi,
		xf=xf,
		yi=yi,
		yf=yf,
		g_acceleration=g_acceleration,
		)
	descent_curves.add_linear_path()
	descent_curves.add_parabolic_path()
	descent_curves.add_elliptical_path()
	descent_curves.add_exponential_decay_path()
	descent_curves.add_cosine_path()
	descent_curves.add_brachistochrone_path()
	path_configurations, number_selected_path_configurations = descent_curves.get_path_configurations(
		path_keys=None)

	print(descent_curves)

	descent_curves.view_path_trajectories(
		label_methods=("name", "equation", "arc-length", "elapsed duration"),
		label_delim="\n",
		figsize=(15, 9),
		is_save=is_save,
		)

##