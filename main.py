import random

from dfa import State, DFA

odd = State("A")
even = State("B")

dfa = DFA(even)
dfa.add_rule(odd, "1", even)
dfa.add_rule(even, "1", odd)

dfa.simulate("011101101011010100111000")
print(dfa.current_state)
print(dfa.total_hash)

num_states: int = 10
alphabet = "abcdef"
states = [State(alphabet[i % len(alphabet)]) for i in range(num_states)]
dfa = DFA(states[0])
dfa.states = states

for state in states:
    for letter in alphabet:
        dfa.add_rule(state, letter, random.choice(states))

dfa.simulate("a")
print(dfa.total_hash)
