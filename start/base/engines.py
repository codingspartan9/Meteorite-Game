class CollisionsEngine:

    @staticmethod
    def is_horizontal_collision(object1, object2):
        return object1.left_edge <= object2.right_edge and object1.right_edge >= object2.left_edge

    @staticmethod
    def is_vertical_collision(object1, object2):
        return object1.top_edge <= object2.bottom_edge and object1.bottom_edge >= object2.top_edge

    @staticmethod
    def is_collision(object1, object2):
        return CollisionsEngine.is_horizontal_collision(object1, object2) and CollisionsEngine.is_vertical_collision(object1, object2)


