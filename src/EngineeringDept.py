print('\nBooting AIOS 2024...\n')
print('Importing dependencies...\n')
import loader
import prompts.prompts as prompts
import agents.agents as agents
import autogen
import transitions.transitions as transitions

print('Initiating OS...\n')

# loader.load_and_register_functions(agents.reviewer, agents.executor) 

print("\n===================================")
print("=                                 =")
print("  ---+=== Welcome to AIOS ===+---")
print("            Engineering           ")
print("=                                 =")
print("===================================\n")

groupchat = autogen.GroupChat(
  agents=[agents.agent_1, agents.user_proxy],
  messages=["Hello Agent"],
  max_round=10,
  speaker_selection_method=transitions.toolgen_state_transition,
  allow_repeat_speaker=False,
  send_introductions=True,
  enable_clear_history=True,
)

manager = autogen.GroupChatManager(
  groupchat=groupchat,
  system_message=prompts.group_chat_manager_prompt,
  human_input_mode="NEVER",
  description="A bot that manages conversations and replies in the group chat. ",
  
)

result = agents.initializer.initiate_chat(
    manager, message=f"""Topic: AI Blockchain Research. Requirement: a tool that pulls 5 research papers from arxiv api on a given topic."""
)

# '''print(result)'''

# pprint.pprint(result.chat_history)
# 
# pprint.pprint(result.summary)
# pprint.pprint(result.cost)

 