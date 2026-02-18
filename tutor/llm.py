from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline

## Generate answers using retrieved context.

   ## model="mistralai/Mistral-7B-Instruct-v0.2",
pipe = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    max_new_tokens=128,
    temperature=0.3
)

llm = HuggingFacePipeline(pipeline=pipe)