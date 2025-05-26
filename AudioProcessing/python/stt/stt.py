import whisper

# Carregar o modelo (use 'base', 'small', 'medium', 'large')
model = whisper.load_model("base")

# Transcrever o áudio
result = model.transcribe("output.wav", language="pt")

# Exibir o texto transcrito
print(result["text"])
