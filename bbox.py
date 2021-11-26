class BBoxCoordinate():
    
    def __init__(self):
        self.corner_list = [
            [], # [bottom_left_x,   bottom_left_y   ]
            [], # [top_left_x,      top_left_y      ]
            [], # [top_right_x,     top_right_y     ]
            []  # [bottom_right_x,  bottom_right_y  ]
        ]

    def set_bottom_left(self, coord):
        self.corner_list[0] = coord
        self.corner_list[1][0] = coord[0]
        self.corner_list[3][1] = coord[1]
    
    def set_top_left(self, coord):
        self.corner_list[1] = coord
        self.corner_list[0][0] = coord[0]
        self.corner_list[2][1] = coord[1]

    def set_bottom_right(self, coord):
        self.corner_list[3] = coord
        self.corner_list[2][0] = coord[0]
        self.corner_list[0][1] = coord[1]
    
    def set_top_right(self, coord):
        self.corner_list[2] = coord
        self.corner_list[3][0] = coord[0]
        self.corner_list[1][1] = coord[1]

    def _entered_check(_list):
        if not _list:
            raise Exception('Not entered index exist.')

    def get_corner_list(self):
        for _list in self.corner_list:
            self._entered_check(_list)
        return self.corner_list

    def get_bottom_left(self):
        self._entered_check(self.corner_list[0])
        return self.corner_list[0]
    
    def get_bottom_left(self):
        self._entered_check(self.corner_list[1])
        return self.corner_list[1]

    def get_bottom_left(self):
        self._entered_check(self.corner_list[2])
        return self.corner_list[2]

    def get_bottom_left(self):
        self._entered_check(self.corner_list[3])
        return self.corner_list[3]
