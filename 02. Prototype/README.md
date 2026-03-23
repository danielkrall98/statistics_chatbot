# Prototype

## Description
This is a small CLI-Tool for queries regarding statistical data in natural language.

## Architecture
- User Questions
- LLM generates pandas-queries
- Python executes the queries and gets a result
- LLM explains the result

## Used Data
- `wien_bevoelkerung.csv`
- Data is cleaned using `clean_data.py`
- Written into `cleaned_data.csv`

## Example Query
`Frage: Welcher Bezirk hat die meisten Einwohner?`

## Classes
- `prompts.py` includes the query and answer prompt
- `llm.py` includes LLM-Model etc.
- `query_engine.py` 
- `main.py` 

## Setup
1. Rename `.examplenv` to `.env` and add your OpenAI API-Key
2. In `/02. Prototype`
- `python3 -m venv environment-name`
- `source environment-name/bin/activate`
- `pip install -r requirements.txt`

## Running the Tool
1. In `02. Prototype/src/` run
   - `python main.py`
2. Ask your Question
3. Receive an answer
   - `Generated Query` shows the generated pandas Query
   - `Raw Result` shows the Result of the Query (number)
   - `Antwort` is the natural language answer from the LLM.

## Examples
- Bild 1
- Bild 2
- Bild 3
- Bild 4