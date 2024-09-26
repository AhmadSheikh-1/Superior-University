class MultiReflexAgent:
    def __init__(self, desired_temps):
        self.desired_temps = desired_temps
    
    def perceive(self, current_temps):
        self.current_temps = current_temps
    
    def act(self):
        actions = {}
        for room, current_temp in self.current_temps.items():
            desired_temp = self.desired_temps.get(room, None)
            if desired_temp is not None:
                if current_temp < desired_temp:
                    actions[room] = "turn on the heater"
                else:
                    actions[room] = "turn off the heater"
        return actions

room_temps = {
    "Living room": 27,
    "Kitchen": 34,
    "Bedroom": 20
}

desired_temps = {
    "Living room": 22,
    "Kitchen": 25,
    "Bedroom": 21
}

agent = MultiReflexAgent(desired_temps)
agent.perceive(room_temps)
actions = agent.act()

for room, action in actions.items():
    print(f"{room}: {room_temps[room]} ==> {action}")
