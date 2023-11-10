"""The River Simulation!"""

from exercises.ex08.river import River

# Creates the river!
my_river: River = River(15, 2)

# Calls river, so I can view it!
my_river.view_river()
my_river.one_river_week()
