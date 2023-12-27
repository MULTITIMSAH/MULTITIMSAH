class BusSchedule:
    def __init__(self, route_name, stops, timings):
        self.route_name = route_name
        self.stops = stops
        self.timings = timings

    def display_schedule(self):
        print(f"Bus Schedule for Route: {self.route_name}")
        for stop, timing in zip(self.stops, self.timings):
            print(f"Stop: {stop} - Timing: {timing}")
        print()

def main():
    # Example Bus Schedule
    route_name = "Route 1"
    stops = ["Stop A", "Stop B", "Stop C", "Stop D"]
    timings = ["08:00 AM", "09:30 AM", "11:00 AM", "01:00 PM"]

    # Creating Bus Schedule Object
    bus_schedule = BusSchedule(route_name, stops, timings)

    # Displaying Bus Schedule
    bus_schedule.display_schedule()

if __name__ == "__main__":
    main()
