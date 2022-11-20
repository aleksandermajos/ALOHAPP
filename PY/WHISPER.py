import os
import torch
import whisper
import re
from FILES import get_all_names

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
lang = 'German'
learning_path = '../DATA/PHRASES/LEARNING/'+lang

def transcribe_all_in_dir(path):
    model = whisper.load_model("medium")
    options = dict(language=lang, beam_size=5, best_of=5)
    transcribe_options = dict(task="transcribe", **options)
    translate_options = dict(task="translate", **options)
    list_of_files = get_all_names(path)
    for name in list_of_files:
        filename, file_extension = os.path.splitext(name)
        if file_extension == '.wav':
            full_input_path = path + '/' + name
            transcription = model.transcribe(full_input_path, **transcribe_options)["text"]
            translation = model.transcribe(full_input_path, **translate_options)["text"]
            print(transcription)
            print(translation)
            full_output_path = path + '/' + transcription + file_extension
            full_output_path = re.sub("[$@&!?]", "", full_output_path)
            os.rename(full_input_path, full_output_path)


transcribe_all_in_dir(learning_path)
oko=4

