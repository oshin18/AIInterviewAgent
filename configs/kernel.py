# Import necessary modules from Semantic Kernel and OpenAI/Azure connector
from semantic_kernel import Kernel
from semantic_kernel.agents import ChatCompletionAgent  # Agent that uses chat-based completion
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion  # Connector for Azure OpenAI services
from semantic_kernel.prompt_template import PromptTemplateConfig  # Configuration for defining prompt templates

# Initialize a Semantic Kernel instance which manages services and agents
kernel = Kernel()

# Define the Azure OpenAI service ID, which matches a config in your .env or Azure environment
service_id = "interview-service"

# Add the Azure OpenAI chat completion service to the kernel using the specified service ID
kernel.add_service(
    AzureChatCompletion(service_id=service_id),
)

# Retrieve and customize the execution settings (e.g., max tokens, temperature) for the OpenAI service
req_settings = kernel.get_prompt_execution_settings_from_service_id(service_id)
req_settings.max_tokens = 3000      # Limit the maximum number of tokens in the output
req_settings.temperature = 0.7      # Control creativity/randomness (higher = more creative)
req_settings.top_p = 0.8            # Use nucleus sampling (alternative to temperature)

# Function to create a ChatCompletionAgent from a prompt template file
def create_agent_from_template(template_path, agent_name):
    """
    Loads a prompt template from a file and creates a chat agent configured with that template.

    Args:
        template_path (str): Path to the .skprompt.txt file containing the prompt template.
        agent_name (str): Name used to register or identify the agent.

    Returns:
        ChatCompletionAgent: A ready-to-use chat agent with the configured prompt.
    """
    # Read the template file content
    with open(template_path, 'r') as file:
        template = file.read()

    # Create the prompt template configuration using handlebars format
    prompt_template = PromptTemplateConfig(
        name=agent_name,
        template=template,
        template_format="handlebars",  # Templating engine used (e.g., {{variable}})
        execution_settings=req_settings  # Execution settings defined above
    )

    # Instantiate and return the ChatCompletionAgent using the prompt template
    return ChatCompletionAgent(
        kernel=kernel,
        name=agent_name,
        prompt_template_config=prompt_template
    )
