import dataclasses  # noqa

_input_sm = """
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
"""


_input_lg = """
#############################################################################################################################################
#.........................#...###...#...#...#.............#...#...#...#.......###...#...#...###...#.....###...#...........#...#.........#...#
#.#######################.#.#.###.#.#.#.#.#.#.###########.#.#.#.#.#.#.#.#####.###.#.#.#.#.#.###.#.#.###.###.#.#.#########.#.#.#.#######.#.#.#
#...#...#...............#.#.#.....#.#.#...#.#.....#.......#.#.#.#...#.#.....#.#...#.#.#...#...#.#.#...#.#...#...#.........#.#...#...#...#.#.#
###.#.#.#.#############.#.#.#######.#.#####.#####.#.#######.#.#.#####.#####.#.#.###.#.#######.#.#.###.#.#.#######.#########.#####.#.#.###.#.#
###...#.#.#.............#.#.......#.#.....#...#...#.....#...#...#.....#...#.#.#...#...#.......#.#...#.#.#.#.......#.........#...#.#...###.#.#
#######.#.#.#############.#######.#.#####.###.#.#######.#.#######.#####.#.#.#.###.#####.#######.###.#.#.#.#.#######.#########.#.#.#######.#.#
#...###...#...#...#.....#.#.......#.#...#.#...#.#.....#.#...#...#.....#.#...#...#.#...#...#...#.#...#.#.#.#.#.......#...#.....#...###...#.#.#
#.#.#########.#.#.#.###.#.#.#######.#.#.#.#.###.#.###.#.###.#.#.#####.#.#######.#.#.#.###.#.#.#.#.###.#.#.#.#.#######.#.#.###########.#.#.#.#
#.#.#...#.....#.#.#.#...#.#.......#.#.#.#.#.#...#...#...###...#...#...#.....#...#...#.#...#.#.#.#...#.#.#.#.#.#.......#.#.....#...#...#.#.#.#
#.#.#.#.#.#####.#.#.#.###.#######.#.#.#.#.#.#.#####.#############.#.#######.#.#######.#.###.#.#.###.#.#.#.#.#.#.#######.#####.#.#.#.###.#.#.#
#.#.#.#.#.......#...#...#...#.....#...#.#.#.#...#...#...#...#.....#...#.....#.#...#...#.#...#.#.#...#.#.#.#...#.......#...#...#.#.#...#...#.#
#.#.#.#.###############.###.#.#########.#.#.###.#.###.#.#.#.#.#######.#.#####.#.#.#.###.#.###.#.#.###.#.#.###########.###.#.###.#.###.#####.#
#.#.#.#.###...#...#.....#...#.........#.#.#.###.#.###.#.#.#.#.....#...#.....#.#.#.#...#.#...#...#...#.#.#.#...........###...###.#...#.#.....#
#.#.#.#.###.#.#.#.#.#####.###########.#.#.#.###.#.###.#.#.#.#####.#.#######.#.#.#.###.#.###.#######.#.#.#.#.###################.###.#.#.#####
#.#...#.#...#.#.#.#.....#.......#...#.#.#.#.#...#.#...#...#...###.#...###...#...#...#.#.#...#.......#.#...#...........#...###...#...#.#.#...#
#.#####.#.###.#.#.#####.#######.#.#.#.#.#.#.#.###.#.#########.###.###.###.#########.#.#.#.###.#######.###############.#.#.###.###.###.#.#.#.#
#.....#...#...#.#.....#.......#.#.#...#...#...#...#...#.....#...#...#...#.......#...#.#.#...#.....#...#...............#.#...#...#.#...#.#.#.#
#####.#####.###.#####.#######.#.#.#############.#####.#.###.###.###.###.#######.#.###.#.###.#####.#.###.###############.###.###.#.#.###.#.#.#
#...#.#...#...#.....#.........#.#.........#.....#.....#...#...#.###...#.#...#...#...#.#.###.#.....#...#.#.........#...#.#...#...#.#.#...#.#.#
#.#.#.#.#.###.#####.###########.#########.#.#####.#######.###.#.#####.#.#.#.#.#####.#.#.###.#.#######.#.#.#######.#.#.#.#.###.###.#.#.###.#.#
#.#.#...#...#.......#.........#.###...###.#.....#.....#...###...#...#.#.#.#.#.....#.#.#...#.#.#...#...#...#.......#.#.#.#.###...#.#.#.....#.#
#.#.#######.#########.#######.#.###.#.###.#####.#####.#.#########.#.#.#.#.#.#####.#.#.###.#.#.#.#.#.#######.#######.#.#.#.#####.#.#.#######.#
#.#...#...#...#...#...###.....#.....#.....#.....#...#.#.......###.#.#.#.#.#...###.#...#...#.#.#.#.#.#.......###...#.#.#.#.#...#.#...#...#...#
#.###.#.#.###.#.#.#.#####.#################.#####.#.#.#######.###.#.#.#.#.###.###.#####.###.#.#.#.#.#.#########.#.#.#.#.#.#.#.#.#####.#.#.###
#...#.#.#...#...#...###...#.........#.....#.#...#.#.#.#.......#...#.#.#.#...#...#.#.....###.#...#...#.....#...#.#.#.#.#.#.#.#.#...#...#...###
###.#.#.###.###########.###.#######.#.###.#.#.#.#.#.#.#.#######.###.#.#.###.###.#.#.#######.#############.#.#.#.#.#.#.#.#.#.#.###.#.#########
#...#.#.#...###.......#.....#...###...#...#...#.#.#.#.#...#...#...#.#.#.#...#...#.#...#...#.#...#...#.....#.#...#.#.#.#.#.#.#...#.#.#...#...#
#.###.#.#.#####.#####.#######.#.#######.#######.#.#.#.###.#.#.###.#.#.#.#.###.###.###.#.#.#.#.#.#.#.#.#####.#####.#.#.#.#.#.###.#.#.#.#.#.#.#
#...#.#.#.#...#.....#.#.......#.......#.#.......#.#...#...#.#...#.#.#.#.#...#.#...#...#.#.#...#...#.#.#...#.#.....#.#...#...#...#.#...#...#.#
###.#.#.#.#.#.#####.#.#.#############.#.#.#######.#####.###.###.#.#.#.#.###.#.#.###.###.#.#########.#.#.#.#.#.#####.#########.###.#########.#
#...#...#.#.#...#...#.#...........#...#.#.#...#...#.....###...#.#.#.#.#...#.#.#...#.#...#...#...#...#...#...#...#...#...#.....#...#.........#
#.#######.#.###.#.###.###########.#.###.#.#.#.#.###.#########.#.#.#.#.###.#.#.###.#.#.#####.#.#.#.#############.#.###.#.#.#####.###.#########
#...#...#...#...#...#.#.......#...#...#.#.#.#.#.#...#...#...#.#.#.#.#...#.#.#.###.#.#...#...#.#.#.....#.........#.#...#...#...#...#.#.......#
###.#.#.#####.#####.#.#.#####.#.#####.#.#.#.#.#.#.###.#.#.#.#.#.#.#.###.#.#.#.###.#.###.#.###.#.#####.#.#########.#.#######.#.###.#.#.#####.#
###...#.....#.#...#.#.#.....#.#.....#.#.#.#.#...#...#.#.#.#.#.#.#.#...#.#.#.#...#.#...#.#...#.#.#...#.#...........#...###...#.###.#.#.#.....#
###########.#.#.#.#.#.#####.#.#####.#.#.#.#.#######.#.#.#.#.#.#.#.###.#.#.#.###.#.###.#.###.#.#.#.#.#.###############.###.###.###.#.#.#.#####
#...........#...#...#.......#.....#.#.#.#.#...#.....#.#.#.#.#.#...#...#.#.#.#...#.###.#...#.#.#...#.#.#.............#...#...#.....#...#...###
#.###############################.#.#.#.#.###.#.#####.#.#.#.#.#####.###.#.#.#.###.###.###.#.#.#####.#.#.###########.###.###.#############.###
#.......#.....#...#.......#.....#.#.#...#...#.#.#...#.#.#.#.#...###...#.#.#.#...#...#.#...#.#.#.....#.#...#...#...#.....###.#...........#...#
#######.#.###.#.#.#.#####.#.###.#.#.#######.#.#.#.#.#.#.#.#.###.#####.#.#.#.###.###.#.#.###.#.#.#####.###.#.#.#.#.#########.#.#########.###.#
#.......#.###...#...###...#.#...#...###...#...#.#.#.#.#.#.#.#...#.....#.#.#...#...#.#.#...#...#...#...###...#...#...###...#.#.........#...#.#
#.#######.#############.###.#.#########.#.#####.#.#.#.#.#.#.#.###.#####.#.###.###.#.#.###.#######.#.###############.###.#.#.#########.###.#.#
#.........#...#...#...#.....#...........#.....#.#.#.#.#.#.#.#.###...#...#...#.###.#.#.#...#.......#.#...............#...#...#.......#...#.#.#
###########.#.#.#.#.#.#######################.#.#.#.#.#.#.#.#.#####.#.#####.#.###.#.#.#.###.#######.#.###############.#######.#####.###.#.#.#
###...#.....#...#...#.....#...................#.#.#.#.#.#.#...#.....#.....#.#.#...#.#...###...#.....#...............#.#.......#.....#...#.#.#
###.#.#.#################.#.###################.#.#.#.#.#.#####.#########.#.#.#.###.#########.#.###################.#.#.#######.#####.###.#.#
#...#.#.#...#...#.......#...#.......#.......#...#.#.#.#.#.....#...#...#...#.#.#...#.........#.#.#...........#.....#...#.......#.....#.###...#
#.###.#.#.#.#.#.#.#####.#####.#####.#.#####.#.###.#.#.#.#####.###.#.#.#.###.#.###.#########.#.#.#.#########.#.###.###########.#####.#.#######
#.#...#...#...#...#...#.......#...#...#.....#.....#.#.#.#...#.#...#.#.#...#...###...#.....#.#.#.#...#.....#.#.###.....#.....#...###.#...#...#
#.#.###############.#.#########.#.#####.###########.#.#.#.#.#.#.###.#.###.#########.#.###.#.#.#.###.#.###.#.#.#######.#.###.###.###.###.#.#.#
#.#...###...###...#.#.#.........#.......###...#...#...#...#...#.#...#...#.....#.....#.###...#...###...#...#...#...###...###...#...#...#...#.#
#.###.###.#.###.#.#.#.#.###################.#.#.#.#############.#.#####.#####.#.#####.#################.#######.#.###########.###.###.#####.#
#...#.....#.....#...#.#.............###...#.#...#...#...#.......#.....#...#...#.....#...#...###.......#.........#...........#...#...#.......#
###.#################.#############.###.#.#.#######.#.#.#.###########.###.#.#######.###.#.#.###.#####.#####################.###.###.#########
###.................#.............#...#.#...#...#...#.#.#...#...#...#.###.#.###...#...#...#...#.....#.#.................#...###...#...#.....#
###################.#############.###.#.#####.#.#.###.#.###.#.#.#.#.#.###.#.###.#.###.#######.#####.#.#.###############.#.#######.###.#.###.#
#...#...............#...........#.#...#.#.....#.#.....#...#...#...#...#...#.#...#.#...#.....#.#.....#.#...#...........#...###...#.....#.#...#
#.#.#.###############.#########.#.#.###.#.#####.#########.#############.###.#.###.#.###.###.#.#.#####.###.#.#########.#######.#.#######.#.###
#.#.#...#...#.......#.###.......#.#.....#.....#.....#...#.....###.......#...#...#.#...#...#...#.....#...#...#.....#...#.......#.........#...#
#.#.###.#.#.#.#####.#.###.#######.###########.#####.#.#.#####.###.#######.#####.#.###.###.#########.###.#####.###.#.###.###################.#
#.#.....#.#.#.#...#...#...#.....#.#.....#...#.#...#...#.......#...#.....#...###.#.###.....###...###...#.....#...#...###.#...............#...#
#.#######.#.#.#.#.#####.###.###.#.#.###.#.#.#.#.#.#############.###.###.###.###.#.###########.#.#####.#####.###.#######.#.#############.#.###
#.....#...#...#.#.#...#...#.#...#...###...#.#...#...#...#...###.....###.....#...#.....#...#...#.#...#.....#...#...#...#.#.............#...###
#####.#.#######.#.#.#.###.#.#.#############.#######.#.#.#.#.#################.#######.#.#.#.###.#.#.#####.###.###.#.#.#.#############.#######
#...#.#.#.......#...#.#...#.#.............#.........#.#.#.#.....#...#####...#.......#.#.#.#...#...#.......###.#...#.#...#.............#.....#
#.#.#.#.#.###########.#.###.#############.###########.#.#.#####.#.#.#####.#.#######.#.#.#.###.###############.#.###.#####.#############.###.#
#.#.#...#...........#.#.....###...........#.........#.#.#.#.....#.#...#...#.#.......#...#.....#...#.........#.#.....#...#.........###...#...#
#.#.###############.#.#########.###########.#######.#.#.#.#.#####.###.#.###.#.#################.#.#.#######.#.#######.#.#########.###.###.###
#.#.#.............#.#.#.......#...........#.#######...#...#.....#.#...#...#...#...#.....#.....#.#.#.#...#...#.....#...#.....#...#...#.#...###
#.#.#.###########.#.#.#.#####.###########.#.###################.#.#.#####.#####.#.#.###.#.###.#.#.#.#.#.#.#######.#.#######.#.#.###.#.#.#####
#.#.#...........#.#.#.#.....#.#...#######...#################E#...#.#...#.....#.#.#.#...#.#...#.#...#.#.#.......#.#.......#...#...#...#.....#
#.#.###########.#.#.#.#####.#.#.#.###########################.#####.#.#.#####.#.#.#.#.###.#.###.#####.#.#######.#.#######.#######.#########.#
#.#.........#...#...#.......#...#..S###############.....#####.#...#...#.#.....#.#...#.#...#.....###...#.....#...#.#...#...#.....#.........#.#
#.#########.#.#####################################.###.#####.#.#.#####.#.#####.#####.#.###########.#######.#.###.#.#.#.###.###.#########.#.#
#.........#...#.......#.....#...#...#...#####.......#...#####.#.#.....#.#.......#...#...#.....#...#.......#...###.#.#.#.....#...###...###...#
#########.#####.#####.#.###.#.#.#.#.#.#.#####.#######.#######.#.#####.#.#########.#.#####.###.#.#.#######.#######.#.#.#######.#####.#.#######
###...#...#...#.#.....#.#...#.#...#...#.....#.....#...###...#.#.#...#...#.....#...#...###...#...#...#...#...#...#...#.........#.....#.......#
###.#.#.###.#.#.#.#####.#.###.#############.#####.#.#####.#.#.#.#.#.#####.###.#.#####.#####.#######.#.#.###.#.#.###############.###########.#
#...#...#...#.#.#...#...#.#...#...........#...#...#.......#.#...#.#.#...#...#.#...#...#...#.......#.#.#.....#.#.#...###.......#.....#.......#
#.#######.###.#.###.#.###.#.###.#########.###.#.###########.#####.#.#.#.###.#.###.#.###.#.#######.#.#.#######.#.#.#.###.#####.#####.#.#######
#.........###...###...###...###.........#.....#.#...........#...#.#.#.#.....#.....#...#.#.......#.#.#.........#...#.....#.....#.....#...#...#
#######################################.#######.#.###########.#.#.#.#.###############.#.#######.#.#.#####################.#####.#######.#.#.#
#.............###...........###.........###...#.#.......###...#.#.#.#.............#...#.......#...#.#...................#.......#.....#...#.#
#.###########.###.#########.###.###########.#.#.#######.###.###.#.#.#############.#.#########.#####.#.#################.#########.###.#####.#
#.......#...#...#.#...#...#.....#...###.....#...#.....#...#.#...#.#.#.....###...#.#.....#...#.....#.#.................#.....#...#...#.......#
#######.#.#.###.#.#.#.#.#.#######.#.###.#########.###.###.#.#.###.#.#.###.###.#.#.#####.#.#.#####.#.#################.#####.#.#.###.#########
###...#...#.#...#...#...#.........#.....#.........###...#.#.#.....#.#...#.....#.#.#...#...#.......#.....#...........#...#...#.#...#.........#
###.#.#####.#.###########################.#############.#.#.#######.###.#######.#.#.#.#################.#.#########.###.#.###.###.#########.#
#...#.....#.#.#...#.....#...............#.........#...#...#...#.....###.#.....#.#.#.#.........#.......#...#...#...#.....#.....###...........#
#.#######.#.#.#.#.#.###.#.#############.#########.#.#.#######.#.#######.#.###.#.#.#.#########.#.#####.#####.#.#.#.###########################
#.#.....#.#.#.#.#.#...#.#.............#.#.........#.#...###...#.......#...###.#.#...#...#.....#.###...#.....#...#.......###.................#
#.#.###.#.#.#.#.#.###.#.#############.#.#.#########.###.###.#########.#######.#.#####.#.#.#####.###.###.###############.###.###############.#
#...#...#...#...#.....#.###...#...#...#.#.#.......#...#...#.....#.....###...#.#.#...#.#.#...#...#...#...#...............#...#...#...#...#...#
#####.#################.###.#.#.#.#.###.#.#.#####.###.###.#####.#.#######.#.#.#.#.#.#.#.###.#.###.###.###.###############.###.#.#.#.#.#.#.###
#.....#.....#...#.....#.....#...#...###...#.#.....###...#.###...#...#...#.#.#.#.#.#.#.#.###...###...#.###.........#...###.#...#...#.#.#.#...#
#.#####.###.#.#.#.###.#####################.#.#########.#.###.#####.#.#.#.#.#.#.#.#.#.#.###########.#.###########.#.#.###.#.#######.#.#.###.#
#...#...###.#.#.#.#...#...................#.#.....#.....#.....#.....#.#...#.#.#.#.#.#.#.....#.....#.#.#.........#.#.#.....#.......#...#...#.#
###.#.#####.#.#.#.#.###.#################.#.#####.#.###########.#####.#####.#.#.#.#.#.#####.#.###.#.#.#.#######.#.#.#############.#######.#.#
###...#.....#.#.#.#...#.#.................#.....#.#...........#.#...#...#...#.#.#.#...#.....#...#.#...#.......#...#.#.............#...###.#.#
#######.#####.#.#.###.#.#.#####################.#.###########.#.#.#.###.#.###.#.#.#####.#######.#.###########.#####.#.#############.#.###.#.#
#.......#...#.#...#...#.#.#.....#.......#...#...#...#...#.....#.#.#...#.#...#.#.#.....#...#...#.#.#...........#...#.#.........#.....#...#.#.#
#.#######.#.#.#####.###.#.#.###.#.#####.#.#.#.#####.#.#.#.#####.#.###.#.###.#.#.#####.###.#.#.#.#.#.###########.#.#.#########.#.#######.#.#.#
#...#...#.#...#.....#...#.#...#.#.#.....#.#.#.....#.#.#.#...#...#.#...#...#.#.#.#...#.#...#.#.#.#.#.............#...#.......#...#...#...#.#.#
###.#.#.#.#####.#####.###.###.#.#.#.#####.#.#####.#.#.#.###.#.###.#.#####.#.#.#.#.#.#.#.###.#.#.#.###################.#####.#####.#.#.###.#.#
###...#.#.....#.....#...#...#.#...#.#...#.#...#...#.#.#...#.#.#...#.....#.#...#.#.#...#...#.#.#.#.#...#.....#.......#.....#.#.....#.#.#...#.#
#######.#####.#####.###.###.#.#####.#.#.#.###.#.###.#.###.#.#.#.#######.#.#####.#.#######.#.#.#.#.#.#.#.###.#.#####.#####.#.#.#####.#.#.###.#
#.....#.......###...#...#...#.#.....#.#...#...#...#.#.#...#.#.#.....#...#...###.#.....#...#.#.#.#.#.#.#...#.#.....#...#...#.#.#...#...#.#...#
#.###.###########.###.###.###.#.#####.#####.#####.#.#.#.###.#.#####.#.#####.###.#####.#.###.#.#.#.#.#.###.#.#####.###.#.###.#.#.#.#####.#.###
#...#.###...#...#.#...###.....#.....#...###.....#.#...#...#.#.#...#.#...#...#...#.....#...#.#...#...#.#...#.#...#.#...#...#.#...#...#...#...#
###.#.###.#.#.#.#.#.###############.###.#######.#.#######.#.#.#.#.#.###.#.###.###.#######.#.#########.#.###.#.#.#.#.#####.#.#######.#.#####.#
#...#.....#...#...#...#.........###.#...#.......#...#.....#.#.#.#...#...#...#...#.#...#...#.......###...###.#.#...#.#.....#.....#...#...#...#
#.###################.#.#######.###.#.###.#########.#.#####.#.#.#####.#####.###.#.#.#.#.#########.#########.#.#####.#.#########.#.#####.#.###
#...#.....#.......#...#...#...#.....#.#...#...#.....#.#.....#.#...#...#.....#...#.#.#...#...#...#.......#...#.....#.#.#...#...#...#.....#...#
###.#.###.#.#####.#.#####.#.#.#######.#.###.#.#.#####.#.#####.###.#.###.#####.###.#.#####.#.#.#.#######.#.#######.#.#.#.#.#.#.#####.#######.#
#...#...#.#.#.....#...###...#.......#.#...#.#.#.....#...#.....#...#...#.....#...#.#.#...#.#.#.#...#...#.#.....#...#.#...#...#.....#.#.......#
#.#####.#.#.#.#######.#############.#.###.#.#.#####.#####.#####.#####.#####.###.#.#.#.#.#.#.#.###.#.#.#.#####.#.###.#############.#.#.#######
#...#...#...#...#.....#.......#...#.#.###.#.#.#...#.....#.#...#.#.....#...#.#...#.#.#.#...#.#...#.#.#.#...#...#...#...#.....#.....#...#...###
###.#.#########.#.#####.#####.#.#.#.#.###.#.#.#.#.#####.#.#.#.#.#.#####.#.#.#.###.#.#.#####.###.#.#.#.###.#.#####.###.#.###.#.#########.#.###
#...#...#.......#.....#.#...#...#.#.#.#...#.#.#.#.#.....#...#.#.#...#...#.#.#.#...#.#.....#.#...#...#.#...#.#.....#...#...#.#...#...#...#...#
#.#####.#.###########.#.#.#.#####.#.#.#.###.#.#.#.#.#########.#.###.#.###.#.#.#.###.#####.#.#.#######.#.###.#.#####.#####.#.###.#.#.#.#####.#
#...#...#.......#.....#...#.....#...#.#...#.#.#.#.#.......#...#...#...###...#.#...#.#.....#.#.......#.#.#...#.....#.....#.#...#...#...#...#.#
###.#.#########.#.#############.#####.###.#.#.#.#.#######.#.#####.###########.###.#.#.#####.#######.#.#.#.#######.#####.#.###.#########.#.#.#
#...#.#.........#...#...#.......#...#...#.#.#.#.#.#...#...#...#...#...........#...#.#.#...#.........#...#...#.....#.....#...#.#.......#.#.#.#
#.###.#.###########.#.#.#.#######.#.###.#.#.#.#.#.#.#.#.#####.#.###.###########.###.#.#.#.#################.#.#####.#######.#.#.#####.#.#.#.#
#.#...#.......#...#.#.#...#.......#.#...#.#.#.#.#...#.#...#...#...#.....#.....#.###.#...#.................#.#.....#.#...#...#.#.....#...#.#.#
#.#.#########.#.#.#.#.#####.#######.#.###.#.#.#.#####.###.#.#####.#####.#.###.#.###.#####################.#.#####.#.#.#.#.###.#####.#####.#.#
#.#.#...###...#.#.#.#...#...#.......#.###.#.#.#.#.....#...#.#...#.#.....#.#...#...#.....#.....#...#.....#.#.#.....#...#...#...#.....#...#.#.#
#.#.#.#.###.###.#.#.###.#.###.#######.###.#.#.#.#.#####.###.#.#.#.#.#####.#.#####.#####.#.###.#.#.#.###.#.#.#.#############.###.#####.#.#.#.#
#.#.#.#.....#...#...###...###.....#...#...#.#...#...#...###...#...#.#.....#.#.....#.....#...#.#.#.#.###...#.#.............#...#.......#.#...#
#.#.#.#######.###################.#.###.###.#######.#.#############.#.#####.#.#####.#######.#.#.#.#.#######.#############.###.#########.#####
#...#.....#...#...#...#...#.......#...#...#...#.....#...........#...#.#.....#.....#...#...#.#...#.#.....###.#...#...#.....###...........#...#
#########.#.###.#.#.#.#.#.#.#########.###.###.#.###############.#.###.#.#########.###.#.#.#.#####.#####.###.#.#.#.#.#.###################.#.#
#...#.....#.###.#...#...#...#...#...#.###.....#...#...#.....#...#.....#...#.......#...#.#.#...###.....#...#...#...#.#.....................#.#
#.#.#.#####.###.#############.#.#.#.#.###########.#.#.#.###.#.###########.#.#######.###.#.###.#######.###.#########.#######################.#
#.#.#.....#...#.#...#...#...#.#.#.#.#.........#...#.#.#...#.#.#...#...#...#.......#...#.#...#.......#...#.........#.#.......#...#.....#...#.#
#.#.#####.###.#.#.#.#.#.#.#.#.#.#.#.#########.#.###.#.###.#.#.#.#.#.#.#.#########.###.#.###.#######.###.#########.#.#.#####.#.#.#.###.#.#.#.#
#.#.......#...#.#.#.#.#.#.#.#.#.#.#...#...#...#...#.#.#...#.#.#.#...#...#...#...#.#...#...#...#...#...#.#.....#...#.#...#...#.#.#...#.#.#.#.#
#.#########.###.#.#.#.#.#.#.#.#.#.###.#.#.#.#####.#.#.#.###.#.#.#########.#.#.#.#.#.#####.###.#.#.###.#.#.###.#.###.###.#.###.#.###.#.#.#.#.#
#...........###...#...#...#...#...###...#...#####...#...###...#...........#...#...#.......###...#.....#...###...###.....#.....#.....#...#...#
#############################################################################################################################################
"""

from pprint import pp  # noqa


@dataclasses.dataclass(frozen=True)
class Position:
    x: int
    y: int

    def __str__(self):
        return f"({self.x},{self.y})"

    def __repr__(self):
        return str(self)

    def add(self, other: "Position") -> "Position":
        return Position(self.x + other.x, self.y + other.y)


Path = list[Position]


class Dirs:
    NORTH = Position(0, -1)
    EAST = Position(1, 0)
    SOUTH = Position(0, 1)
    WEST = Position(-1, 0)

    ALL = [NORTH, EAST, SOUTH, WEST]


class StringGrid:
    def __init__(self, grid_str: str):
        self._data_raw = grid_str.strip()
        self._data = self._data_raw
        self.width = self._data_raw.index("\n")
        self.height = self._data_raw.count("\n") + 1

    def __str__(self):
        return self._data_raw

    def index_to_pos(self, index: int) -> Position:
        return Position(index % (self.width + 1), index // (self.width + 1))

    def pos_to_index(self, pos: Position) -> int:
        return pos.y * (self.width + 1) + pos.x

    def find(self, symbol: str) -> Position:
        return self.index_to_pos(self._data.index(symbol))

    def is_in_bounds(self, pos: Position):
        return 0 <= pos.x < self.width and 0 <= pos.y < self.height

    def get(self, pos: Position) -> str:
        return self._data[self.pos_to_index(pos)]

    def set(self, pos: Position, symbol: str) -> None:
        idx = self.pos_to_index(pos)
        self._data = self._data[:idx] + symbol + self._data[idx + 1 :]
        self._data_raw = self._data

    def copy(self) -> "StringGrid":
        return StringGrid(self._data)


class Maze:
    class NoSolution(Exception):
        pass

    WALL = "#"
    START = "S"
    END = "E"
    SPACE = "."

    def __init__(self, floor_str: str):
        self._grid = StringGrid(floor_str)
        self.start = self._grid.find(Maze.START)
        self.end = self._grid.find(Maze.END)
        self.dir = Dirs.EAST

    @property
    def grid(self):
        return self._grid

    def __str__(self):
        return str(self._grid)

    def path_string(self, path: Path) -> str:
        grid = self._grid.copy()
        for pos in path:
            grid.set(pos, "*")
        return str(grid)

    def solve(self) -> tuple[Path, dict[Position, int]]:
        pos = self.start
        path = [pos]
        steps = {pos: 0}

        while pos != self.end:
            next_pos = None
            for direction in Dirs.ALL:
                other_pos = pos.add(direction)
                if (
                    self._grid.is_in_bounds(other_pos)
                    and self._grid.get(other_pos) != Maze.WALL
                    and (len(path) == 1 or other_pos != path[-2])
                ):
                    next_pos = other_pos
                    break

            path.append(next_pos)
            steps[next_pos] = steps[pos] + 1
            pos = next_pos
        return path, steps


@dataclasses.dataclass(frozen=True)
class Cheat:
    start: Position
    end: Position
    steps_saved: int

    def __str__(self):
        return f"Cheat({self.start}, {self.end}, {self.steps_saved})"

    def __repr__(self):
        return str(self)



def get_all_cheats(
    grid: StringGrid, path: Path, steps: dict[Position, int]
) -> list[Cheat]:
    all_cheats = []

    steps_remaining = {}
    for k,v in steps.items():
        steps_remaining[k] = len(path) - v

    for pos in path:
        for direction in Dirs.ALL:
            pos1 = pos.add(direction)
            if grid.get(pos1) != Maze.WALL:
                continue

            end_pos = pos1.add(direction)
            if end_pos not in steps_remaining:
                continue

            steps_from_end_pos = steps_remaining[end_pos]
            if steps_from_end_pos < steps_remaining[pos]:
                all_cheats.append(Cheat(
                    start=pos,
                    end=end_pos,
                    steps_saved=steps_remaining[pos] - steps_from_end_pos - 2,
                ))

    return all_cheats


def main(puzzle_input):
    maze = Maze(puzzle_input)
    path, steps = maze.solve()
    cheats = get_all_cheats(maze.grid, path, steps)
    #print(maze.path_string(path))
    #pp(steps)
    pp(sorted(cheats, key=lambda x: x.steps_saved))
    cheats_summary = {}
    over_100 = 0
    for c in cheats:
        cheats_summary.setdefault(c.steps_saved, 0)
        cheats_summary[c.steps_saved] += 1
        if c.steps_saved >= 100:
            over_100 += 1
    pp(cheats_summary)
    print("Over 100:", over_100)


_input_xs = """
#####
#E.##
##S##
#####
"""


if __name__ == "__main__":
    # main(_input_xs)
    # main(_input_sm)
    main(_input_lg)
