from g4f.client import Client
import gradio as gr

client = Client()
def chatbot_response(user_input):
        response = client.chat.completions.create(
        model="gpt-3.5-turbo",
          messages=[{"role": "user", "content": user_input}],
        )
        return(response.choices[0].message.content)
interface=gr.Interface(
        fn=chatbot_response,
        inputs=gr.Textbox(lines=2,placeholder='Please provide your input here'),
        outputs='text',
        title='Ai Assistant chabot',
        description='Ask any question'
)

if __name__=="__main__":
        interface.launch(share=True)
