from ev_pddl.world_state import WorldState
import debugpy

class Encounter:

    def __init__(self, initialization_text, worldstate : WorldState):
        self.name = initialization_text['name']
        self.description = initialization_text['description']
        self.metadata = initialization_text['metadata']
        self.preconditions_text = initialization_text['preconditions']
        self.preconditions = worldstate.create_action_proposition_from_PDDL(self.preconditions_text)
        self.executed = False
        self.skipped = False

    def get_start_encouter_message(self) -> str:
        """
        This method is used to get the message to be sent to the environment when the encounter is started.

        Returns
        -------
        str
            The message to be sent to the environment when the encounter is started.
        """
        return "start_encounter({})".format(self.name)