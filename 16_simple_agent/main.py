import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel

load_dotenv()


gemini_api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
)

model = OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=provider)

agent = Agent(
    name="Greeting Agent",
    instructions="You are greeting agent, when someone says hi you will say salam, from Abdul Ahad, if someone say bye you say Allah hafiz, if some talk other then greeting you will say i can't talk other then greeting",
    model=model,
)

user_question = input("Please enter your question: ")

result = Runner.run_sync(agent, user_question)

print(result.final_output)
