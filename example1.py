#set parameters:
params = Params(alpha = 1.0,
				beta = 0.5,
				theta = 0.5,
				Q = 0.5,
				RIO = 5 #for now, demand is constant
			)


#iterate the map to 1000 steps
iterate(1000, params)

#plot parameters
plot_begin = 0
plot_end = 100

#plot the trajectory of each variable 
plotTrajectories(plot_begin, plot_end)

#plot the factory's inventory against the factory's incoming orders
plotTwoComponents("FI", "FIO", plot_begin, plot_end)