import os
from semantic_kernel import Kernel
from semantic_kernel.agents import ChatCompletionAgent
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.prompt_template import PromptTemplateConfig

# Initialize the Kernel
kernel = Kernel()

# Prepare OpenAI service using credentials stored in the `.env` file
service_id = "interview-service"

kernel.add_service(
    AzureChatCompletion(service_id=service_id),
)

# Request settings
req_settings = kernel.get_prompt_execution_settings_from_service_id(service_id)
req_settings.max_tokens = 3000
req_settings.temperature = 0.7
req_settings.top_p = 0.8

# Function to create a PromptAgent from a template
def create_agent_from_template(template_path, agent_name):
    with open(template_path, 'r') as file:
        template = file.read()

    prompt_template = PromptTemplateConfig(
        name=agent_name,
        template=template,
        template_format="handlebars",
        execution_settings=req_settings,
    )

    return ChatCompletionAgent(
        kernel=kernel,
        name=agent_name,
        prompt_template_config=prompt_template
    )

