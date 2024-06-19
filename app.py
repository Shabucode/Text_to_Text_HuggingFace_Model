from fastapi import FastAPI
from transformers import pipeline

##create a new FASTAPI app instance
app=FastAPI()

# Use a pipeline as a high-level helper
#from transformers import pipeline
#or # Load model directly
#from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

#tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
#model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")

#Initialize the text generation pipeline
pipe = pipeline("text2text-generation", model="google/flan-t5-small")

@app.get("/")
def home():
    return {"message":"Hello World"}

@app.get("/generate")
def generate(text:str):
    #use the pipeline to generate text from input text
    output=pipe(text)

    #return the output in json format response
    return {"output":output[0]['generated_text']}