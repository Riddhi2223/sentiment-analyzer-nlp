import gradio as gr
from analyzer import analyze

def predict(text):
    r = analyze(text)
    return f"{r['sentiment']} - {r['confidence']:.0%} confidence"

interface = gr.Interface(
    fn=predict,
    inputs="text",
    outputs="text",
    title="Sentiment Analyzer"
)

interface.launch(share=True)
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)