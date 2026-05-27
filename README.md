# German Text-to-Voice Generator

A command-line tool that generates German pronunciation audio files using OpenAI's Text-to-Speech API. The audio files are designed to be imported directly into my Anki card set for spaced repetition pronunciation practice.

---

## How to use it

1. Type a German sentence into the command line as an argument when you run `main.py`
2. The tool calls OpenAI's TTS API and generates a slow, clear `.mp3` file of the sentence
3. The sentence and audio file path are saved to a local SQLite database
4. When needed, you manually copy the `.mp3` file into Anki as a card audio attachment to supplement your written sentence

---

## Project structure

```
├── main.py          # Entry point — runs the full pipeline
├── tts.py           # Calls OpenAI TTS API and saves the .mp3
├── database.py      # SQLite helpers (stores sentences + audio paths)
├── input_args.py    # Parses the sentence from the command line
├── requirements.txt # Python dependencies
├── .env.example     # Template for your API key
├── audio/           # Generated .mp3 files (created automatically, folder not on GitHub)
├── db/              # SQLite database (created automatically, folder not on GitHub)
└── logfile.log      # Run log (created automatically, folder not on GitHub)
```

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/HeatherDriver/Text-To-Speech-German.git
cd Text-To-Speech-German
```

### 2. Create and activate a virtual environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your OpenAI API key

```bash
copy .env.example .env
notepad .env
```

Replace `sk-your-key-here` with your real OpenAI API key. 

---

## Usage

Run the tool with a German sentence in quotes, for example:

```bash
python main.py "Ich möchte Kaffee, bitte."
```

The `.mp3` file is saved in the `audio/` folder. Example output:

```
audio/3f2a1b4c9d01.mp3
```

### Re-running the same sentence

If you run the same sentence twice, the tool skips the API call and reuses the existing audio file automatically. This saves API costs.

---

## Importing audio into Anki

1. Run the tool to generate your `.mp3` file
2. In Anki, create or edit a card and just drag and drop to add the audio reference in a field:
   ```
   [sound:3f2a1b4c9d01.mp3]
   ```
3. Anki will play the audio automatically when the card is reviewed

---

## Configuration

| Setting | Location | Default | Options |
|---|---|---|---|
| Voice | `tts.py` → `DEFAULT_VOICE` | `nova` | alloy, echo, fable, onyx, nova, shimmer |
| Speed | `tts.py` → `generate_audio()` | `0.8` | 0.25 (slowest) → 4.0 (fastest). 1.0 is the default, this has been set lower for language learning |
| Audio quality | `tts.py` → `TTS_MODEL` | `tts-1` | `tts-1`, `tts-1-hd` (higher quality, slower) |

---

## Requirements

- Python 3.10+
- OpenAI API key
- Internet connection (for the TTS API call)
- Anki App