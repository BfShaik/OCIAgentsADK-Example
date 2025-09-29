from typing import Dict
from oci.addons.adk import Agent, AgentClient, tool

@tool
def get_weather(location: str) -> Dict[str, str]:
    """Get the weather for a given location"""
    return {"location": location, "temperature": 72, "unit": "F"}


def main():
    # Create a client with your authentication details
    client = AgentClient(
        auth_type="api_key",
        profile="DEFAULT",
        region="us-ashburn-1"
    )

    # Instantiate the agent with your agent endpoint ID and the tool

    agent = Agent(
        client=client,
        agent_endpoint_id="ocid1.genaiagentendpoint.oc1.iad.amaaaaaa2j5jslyamhyjqz2gxnpt34w2ww7sfjfehsuwajxt32n7kxx6amzq",
        instructions="Perform weather queries using the given tools.",
        tools=[get_weather]
    )

    # Set up the agent (configures instructions and tools in the remote agent resource)
    agent.setup()

    # Run the agent with an input
    input = "Is it cold in Seattle?"
    response = agent.run(input)

    # Print the response
    response.pretty_print()

if __name__ == "__main__":
    main()