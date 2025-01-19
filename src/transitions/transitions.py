import agents.agents as agents

# =============== SYNTHESIS ===================

def research_state_transition(last_speaker, groupchat):
    messages = groupchat.messages

    if last_speaker is agents.initializer:
        # init -> retrieve
        return agents.coder
    elif last_speaker is agents.coder:
        # retrieve: action 1 -> action 2
        return agents.executor
    elif last_speaker is agents.executor:
        if messages[-1]["content"] == "exitcode: 1":
            # retrieve --(execution failed)--> retrieve
            return agents.coder
        else:
            # retrieve --(execution success)--> research
            return agents.scientist
    elif last_speaker == "Scientist":
      
        # research -> end
        return None