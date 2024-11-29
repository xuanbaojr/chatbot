import requests

def hello_world():
    res = requests.get("http://localhost:8001")
    if res.status_code == 200:
        print("res.json", (res.json()))
        return res.json()['text']

    else:
        print(f"Error: {res.status_code}")
        return None

class DefaultLLM():
    def __init__(self) -> None:
        self.url = "http://localhost:8001"

    def single_forward(self, question):
        res = requests.post(url=f"{self.url}/default_llm/single_forward/{1}",
                            json={
                                "system": "you are an excellent assistant !",
                                "human": question
                            })
        if res.status_code == 200:
            return res.json()['answer']
        else:
            print(f"Error: {res.status_code}")
            return None
        
if __name__ == "__main__":
    # res = hello_world()
    default_llm = DefaultLLM()
    res_single_forward = default_llm.single_forward(question="What was Ho Chi Minh born ?")
    print("res_single_forward", res_single_forward)
    