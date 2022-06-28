from base.history_keeper import HistoryKeeper
from base.velocity_calculator import VelocityCalculator


class Event:
    happened_this_cycle = False
    name = ""

    def __init__(self):
        self.name = id(self)

    def run(self, happened_this_cycle):
        self.happened_this_cycle = happened_this_cycle

        HistoryKeeper.add(happened_this_cycle, self.name, False)

    def happened_last_cycle(self):
        return HistoryKeeper.get_last(self.name)

    def is_click(self):
        return not self.happened_last_cycle() and self.happened_this_cycle

    def has_stopped(self):
        return self.happened_last_cycle() and not self.happened_this_cycle


class TimedEvent:
    current_time = 0
    is_started = False
    time_needed = 0

    def __init__(self, time_needed):
        self.time_needed = time_needed

    def run(self, should_reset, should_start):
        if should_reset:
            self.reset()

        if should_start and not self.is_started:
            self.start()

        if self.is_started:
            self.current_time += VelocityCalculator.time

    def start(self):
        self.current_time = 0
        self.is_started = True

    def reset(self):
        self.current_time = 0
        self.is_started = False

    def is_done(self):
        return self.is_started and self.current_time >= self.time_needed

    def has_finished(self):
        return not self.is_started or self.is_done()