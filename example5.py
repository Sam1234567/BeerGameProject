#set parameters:
params = Params(Params(alpha = 1.0,
				beta = 0.551,
				theta = 0.5,
				Q = 0.6,
				RIO = 5 #for now, demand is constant
			)


#iterate the map to 1000 steps
iterate(5000, params)

#plot parameters
plot_begin = 0
plot_end = 2000

#plot the trajectory of each variable 
plotTrajectories(plot_begin, plot_end)

#plot the factory's inventory against the factory's incoming orders
plotTwoComponents("FI", "RI", plot_begin, plot_end)

