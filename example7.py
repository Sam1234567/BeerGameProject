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
plotThreeComponents("FI", "FIO","RI", plot_begin, plot_end)

plot2DGrayscale(Params(alpha = 1.0,
				beta = 0.5,
				theta = 0.5,
				Q = 0.5,
				RIO = 5 #for now, demand is constant
			),'alpha', 'theta', 0.5, 0.5, "FI", 100, 50)
			
#  plot2DGrayscale(Params(alpha = 0.40,
#    ...: ^I^I^I^Ibeta = 0,
#    ...: ^I^I^I^Itheta = 0.51,
#    ...: ^I^I^I^IQ = 0.5,
#    ...: ^I^I^I^IRIO = 5 #for now, demand is constant
#    ...: ^I^I^I),'alpha', 'beta', 1.1,0.6, "FI", 100, 200)
