import os  
import requests  
  
class Agent:  
    def __init__(self, name, instructions, model):  
        self.name = name  
        self.instructions = instructions  
        self.model = model  
  
class Runner:  
    @staticmethod  
    def run_sync(starting_agent, input):  
        return AsyncOpenAI().chat(starting_agent.model, starting_agent.instructions, input)  
  
class AsyncOpenAI:  
    def __init__(self):  
        self.api_key = os.getenv("OPENROUTER_API_KEY")  
        self.api_url = "https://openrouter.ai/api/v1/chat/completions"  
        self.headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}  
  
    def chat(self, model, instructions, user_input):  
        data = {"model": model, "messages": [  
            {"role": "system", "content": instructions},  
            {"role": "user", "content": user_input}]  
        }  
        response = requests.post(self.api_url, headers=self.headers, json=data)  
        if response.status_code == 200:  
            return response.json()["choices"][0]["message"]["content"]  
        else:  
            return f"Error: {response.status_code} - {response.text}"  
  
openAIChatCompletionsModel = None 
