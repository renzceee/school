class FSM:
    def __init__(self, states, alphabet, start_state, accepting_states, transitions):
        self.states = states
        self.alphabet = alphabet
        self.start_state = start_state
        self.accepting_states = accepting_states
        self.transitions = transitions

    def process_input(self, input_string):
        current_state = self.start_state

        for symbol in input_string:
            if symbol not in self.alphabet:
                raise ValueError(f"Input symbol {symbol} is not in the alphabet.")

            current_state = self.transitions.get((current_state, symbol), None)
            if current_state is None:
                return "Rejected"

        if current_state in self.accepting_states:
            return "Accepted"
        else:
            return "Rejected"



states = {'q0', 'q1'}
alphabet = {'0', '1'}
start_state = 'q0'
accepting_states = {'q1'}
transitions = {
    ('q0', '0'): 'q0',
    ('q0', '1'): 'q1',
    ('q1', '0'): 'q1',
    ('q1', '1'): 'q1'
}


fsm = FSM(states, alphabet, start_state, accepting_states, transitions)


input_string = '010'
result = fsm.process_input(input_string)


if result == "Accepted":
    print(f"The FSM ACCEPTED the string '{input_string}'")
else:
    print(f"The FSM REJECTED the string '{input_string}'")