import gradio as gr
import chat

# Initial prompt for the chatbot
chat.gemi("consider yourself a mental health chatbot. Your response should be one or four lines only. Don't answer unnecessary questions, only health-related and mental illness therapy questions.")

def bot(user_input):
    return chat.gemi(user_input)

with gr.Blocks(css="""
    body {
  
    .loading {
        display: none !important; /* Hide loading animation */
    }
""") as demo:
    gr.Markdown("## ☮️ MindMate - Mental Health Chatbot")
    
    chatbot_input = gr.Textbox(label="Your Input", placeholder="Enter your message here...")
    chatbot_output = gr.Textbox(label="MindMate Response")
    chatbot_button = gr.Button("Send")

    chatbot_button.click(fn=bot, inputs=chatbot_input, outputs=chatbot_output)

demo.launch(server_name="0.0.0.0", server_port=7860, share=True)
