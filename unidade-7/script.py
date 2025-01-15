import pathlib
import whisper
from langchain_ollama.llms import OllamaLLM

file_path = pathlib.Path(__file__).parent.joinpath("Rick_Astley_-_Never_Gonna_Give_You_Up.mp3").as_posix()
whisper_model = whisper.load_model("base.en")
whisper_result = whisper_model.transcribe(file_path)
transcription = whisper_result["text"]

prompt = f"Destaque os pontos chaves do seguinte texto: {transcription}"
llm_model = OllamaLLM(model="llama3.2:3b")
response = llm_model.invoke(prompt)

print(response)
