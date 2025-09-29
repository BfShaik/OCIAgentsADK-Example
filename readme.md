# OCI Generative AI Agent with RAG Example

This repository contains a simple Python example demonstrating how to set up and run a **Generative AI Agent** on Oracle Cloud Infrastructure (OCI) using the Agent Development Kit (**ADK**).

The agent is configured with an **Agentic RAG Tool** to query a specified OCI Knowledge Base, enabling it to answer questions based on your custom data.

## Prerequisites

Before running this script, ensure you have the following:

1.  **OCI Account and Permissions:** You must have an active OCI account with the necessary permissions to create and manage Generative AI Agent Endpoints and Knowledge Bases.
2.  **Generative AI Agent Endpoint:** An existing Agent Endpoint OCID is required.
3.  **Knowledge Base:** An existing Generative AI Agent Knowledge Base OCID is required.
4.  **OCI Configuration:** The script uses `auth_type="api_key"` and expects your OCI API key and configuration to be set up in your `~/.oci/config` file under the specified `profile` (default is `DEFAULT`).
5.  **Python Environment:** Python 3.x installed.

## Setup

Python
Create a project with a virtual environment:

# Create a project folder with name of your choice

mkdir <your-project-name>
cd <your-project-name>

# Create and activate a virtual environment under `<myenv>` subfolder

python -m venv <myenv>
source <myenv>/bin/activate

Python ADK requires Python 3.10 or later. Ensure you have the correct version of Python installed in your environment.

Installing the ADK
After you create a project and a virtual environment, install the latest version of ADK:

pip install "oci[adk]"
