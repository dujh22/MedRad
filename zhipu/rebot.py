import zhipuai

zhipuai.api_key = "具体你的api_key"

messages = []

def robot():
    response = zhipuai.model_api.sse_invoke(
        model="chatglm_turbo",
        prompt=messages,
        temperature=0.95,
        top_p=0.7,
        incremental=True
    )

    robot_answer = ""
    print("Robot: ", end = "", flush = True)
    for event in response.events():
      if event.event == "add":
          print(event.data, end = "", flush = True)
          robot_answer = robot_answer + event.data
      elif event.event == "error" or event.event == "interrupted":
          print(event.data, end = "", flush = True)
      elif event.event == "finish":
          print(event.data, end = "\n", flush = True)
          robot_answer = robot_answer + event.data
          messages.append({"role":"user", "content": robot_answer})

          print(event.meta)
      else:
          print(event.data, end = "", flush = True)

if __name__ == '__main__':
    while True:
        user_question = input("User: ")
        messages.append({"role":"user", "content": user_question})
        robot()
