class NFA:
    def __init__(self, states, alphabet, start_state, accepting_states, transitions):
        self.states = states
        self.alphabet = alphabet
        self.start_state = start_state
        self.accepting_states = accepting_states
        self.transitions = transitions

    def process_input(self, input_string):
        current_states = {self.start_state}

        for symbol in input_string:
            next_states = set()
            for state in current_states:
                next_states.update(self.transitions.get((state, symbol), set()))
            if not next_states:
                return False, current_states
            current_states = next_states

        if current_states & self.accepting_states:
            return True, current_states
        else:
            return False, current_states


states = {'q0', 'q1'}
alphabet = {'0', '1'}
start_state = 'q0'
accepting_states = {'q1'}
transitions = {
    ('q0', '0'): {'q0', 'q1'},
    ('q0', '1'): {'q0'},
    ('q1', '0'): {'q1'},
    ('q1', '1'): {'q1'}
}

nfa = NFA(states, alphabet, start_state, accepting_states, transitions)

input_string = '1'

accepted, final_states = nfa.process_input(input_string)

if accepted:
    print(f"The NFA accepts the string '{input_string}'")
else:
    print(f"Rejected. The NFA ends in the following states: {final_states}")
    print(f"Number of rejected states: {len(final_states)}")
