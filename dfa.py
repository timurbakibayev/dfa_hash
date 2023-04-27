import logging
from dataclasses import dataclass, field
from typing import Tuple, Dict, Optional, List
from logging import getLogger

logger = getLogger("dfa")
logger.setLevel(logging.DEBUG)


@dataclass(frozen=True)
class State:
    hash: str
    accepting: bool = False


@dataclass
class DFA:
    initial_state: State
    current_state: Optional[State] = None
    states: List[State] = field(default_factory=list)
    rules: Dict[Tuple[State, str], State] = field(default_factory=dict)
    total_hash: str = None
    hash_length = 5

    def add_rule(self, from_state: State, letter: str, to_state: State):
        self.rules[(from_state, letter)] = to_state
        if from_state not in self.states:
            self.states.append(from_state)
        if to_state not in self.states:
            self.states.append(to_state)

    def step(self, letter):
        state_letter = (self.current_state, letter)
        if state_letter in self.rules:
            self.current_state = self.rules[state_letter]
            logger.info(f"Switched to state {self.current_state}")

    def simulate(self, word: str):
        self.current_state = self.initial_state
        self.total_hash = ""
        i = 0
        while len(self.total_hash) < self.hash_length:
            i = (i+1) % len(self.states)
            self.total_hash += self.states[i].hash
        for letter in word:
            self.step(letter)
            self.total_hash = self.total_hash + self.current_state.hash
            if len(self.total_hash) > self.hash_length:
                self.total_hash = self.total_hash[-self.hash_length:]
