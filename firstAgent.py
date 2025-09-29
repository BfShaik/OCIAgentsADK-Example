from oci.addons.adk import Agent, AgentClient
from oci.addons.adk.tool.prebuilt import AgenticRagTool

def main():
    
    client = AgentClient(
        auth_type="api_key",
        profile="DEFAULT",
        region="us-ashburn-1"
    )

    # Assuming the knowledge base is already provisioned
    knowledge_base_id = "ocid1.genaiagentknowledgebase.oc1.iad.amaaaaaa2j5jslyayo44m5o2i2ofxf3h3v6kldg7gfjj5l26qfntw36u5liq"

    # Create a RAG tool that uses the knowledge base
    # The tool name and description are optional, but strongly recommended for LLM to understand the tool.
    rag_tool = AgenticRagTool(
        name="OCI RAG tool",
        description="Use this tool to answer questions about products of  Oracle Cloud Infrastructure (OCI).",
        knowledge_base_ids=[knowledge_base_id],
    )

    # Create the agent with the RAG tool
    agent = Agent(
        client=client,
        agent_endpoint_id="ocid1.genaiagentendpoint.oc1.iad.amaaaaaa2j5jslyamhyjqz2gxnpt34w2ww7sfjfehsuwajxt32n7kxx6amzq",
        instructions="Answer question using the OCI RAG tool.",
        tools=[rag_tool]
    )

    # Set up the agent once
    agent.setup()

    # Run the agent with a user query
    input = "Give me the list of products whose price more than 1000"
    response = agent.run(input)
    response.pretty_print()

if __name__ == "__main__":
    main()