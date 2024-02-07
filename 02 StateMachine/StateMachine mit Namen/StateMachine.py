class StateMachine:
    def __init__(self, states):
        self.states = {state: i for i, state in enumerate(states)}
        self.current_state = states[0] if states else None
        self.previous_state = None
        self.entry_triggered = False
        self.debug = False

    def change_to(self, state):
        if state in self.states:
            self.previous_state = self.current_state
            self.current_state = state
            if self.debug:
                print("Change to:", self.current_state, "[" + str(self.states[self.current_state]) +"]" )
            if self.previous_state != self.current_state:
                return True
        else:
            if self.debug:
                print("State", state, "does not exist.")

    def exit_state(self):
        if self.previous_state != self.current_state:
            if self.debug:
                print("Exiting state:", self.previous_state)
            return True
        return False

    def state(self):
        return self.current_state

    def state_number(self):
        return self.states[self.current_state]

    def entry_state(self):
        if self.previous_state != self.current_state:
            self.entry_triggered = True
            self.previous_state = self.current_state
            if self.debug:
                print("Entering state:", self.current_state)
            return True
        return False

    def force_to(self, state):
        if state in self.states:
            self.previous_state = self.current_state
            self.current_state = state
            if self.debug:
                print("Force to:", self.current_state, "[" + str(self.states[self.current_state]) +"]" )
        else:
            if self.debug:
                print("State", state, "does not exist.")

    def print_debug(self, debug):
        self.debug = debug

    def is_state(self, statename):
        return statename == self.current_state
