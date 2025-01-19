from autogen import AssistantAgent, UserProxyAgent, ConversableAgent, config_list_from_json
import prompts.prompts as prompts
from dotenv import load_dotenv

load_dotenv()

print('Configuring models...\n')

config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")

gpt35t = config_list["config_list"][0]
# gpt4 = config_list["config_list"][1]
# gpt4o = config_list["config_list"][2]

print('Creating agents...\n')

# ============= PROXIES ===============

user_proxy = UserProxyAgent(
    name="user_proxy",
    llm_config=False,
    human_input_mode='ALWAYS',
    code_execution_config={
        "use_docker": False,
        "work_dir": "sandbox"
    }
)

# ============== BRAINSTORMERS =================

agent_1 = ConversableAgent(
    name="agent_1",
    system_message=str(prompts.agent1_prompt),
    llm_config=gpt35t,
    code_execution_config=False,
    function_map=None,
    human_input_mode="NEVER",
)