from oci.addons.adk import Agent, AgentClient
from oci.addons.adk.tool.prebuilt import AgenticRagTool

def main():
    
    client = AgentClient(
        auth_type="api_key",
        profile="DEFAULT",
        region="us-ashburn-1"
    )
 
 
    # Create the agent with the RAG tool
    agent = Agent(
        client=client,
        agent_endpoint_id="ocid1.genaiagentendpoint.oc1.iad.amaaaaaa2j5jslyamhyjqz2gxnpt34w2ww7sfjfehsuwajxt32n7kxx6amzq",
        instructions="Answer question using the OCI SQL tool."        
    )

    # Set up the agent once
    agent.setup()

    # Run the agent with a user query
    print("**************************Chat Result************************** Baba ********. baba *******")
    input = "Give me the list of employees and their names and deparments and a breif description of the departments"
    response = agent.run(input)
    response.pretty_print()

if __name__ == "__main__":
    main()