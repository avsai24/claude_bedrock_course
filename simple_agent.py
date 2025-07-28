from strands import Agent
from strands.models.bedrock import BedrockModel

model = BedrockModel(model_id="amazon.nova-lite-v1:0", region="us-east-1")
agent = Agent(model=model)
response = agent("what is todays date?")
print(response)