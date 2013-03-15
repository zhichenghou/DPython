from builder import *


class Director(object):
    def construct(self, builder):
        builder.build_part_a()
        builder.build_part_b()
