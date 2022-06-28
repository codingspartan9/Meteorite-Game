from copy import deepcopy

from base.velocity_calculator import VelocityCalculator


class HistoryKeeper:
    last_objects = {}
    times = []
    last_time = 0

    @staticmethod
    def add(history_keeper_object, name, needs_deepcopy):
        if needs_deepcopy:
            history_keeper_object = deepcopy(history_keeper_object)

        HistoryKeeper.last_objects[f"{name}{VelocityCalculator.time}"] = history_keeper_object

    @staticmethod
    def get_last(name):
        return HistoryKeeper.get_last_using_time(name, HistoryKeeper.last_time)

    @staticmethod
    def get_last_using_time(name, time):
        return HistoryKeeper.last_objects.get(f"{name}{time}")





