import os
from dotenv import load_dotenv
from agents import Agent, Runner, openAIChatCompletionsModel, AsyncOpenAI

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_K")
#.....................

client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

agent = Agent (
    name="my agent",
    instructions="you are a helpfull assistance",
    model=openAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client),
)
#.....................
result = Runner.run_sync(starting_agent=agent, input="hi, how are you?")
print(result.final_output)