from tts import generate_audio
from dotenv import load_dotenv
import database as db
import input_args
import logging
import time

load_dotenv()   # reads OPENAI_API_KEY from .env


if __name__ == "__main__":
    # Initiate logfile
    logging.basicConfig(filename="logfile.log", level=logging.INFO)
    start = time.time()
    logging.info('---Started---')

    db.init_db()

    # Parse out text to translate
    german_text = input_args.get_input_text()
    logging.info(("Text:", german_text))
    # Input this to translator
    audio_path = generate_audio(german_text)
    
    # Translation CRUD
    translation_id = db.insert_translation(german_text, audio_path)
    logging.info(("Audio_path:", audio_path))

    # Concludes writing to logfile
    time_to_run = time.time() - start
    logging.info(("Time to run:", time_to_run))
    logging.info('---Finished---')