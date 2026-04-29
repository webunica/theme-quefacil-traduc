import json
import time
import sys
from deep_translator import GoogleTranslator

def eprint(*args, **kwargs):
    print(*args, flush=True, **kwargs)

def get_all_strings(data, strings_set):
    if isinstance(data, dict):
        for k, v in data.items():
            if isinstance(v, str):
                strings_set.add(v)
            else:
                get_all_strings(v, strings_set)
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, str):
                strings_set.add(item)
            else:
                get_all_strings(item, strings_set)

def replace_strings(data, translation_map):
    if isinstance(data, dict):
        return {k: replace_strings(v, translation_map) for k, v in data.items()}
    elif isinstance(data, list):
        return [replace_strings(item, translation_map) for item in data]
    elif isinstance(data, str):
        return translation_map.get(data, data)
    else:
        return data

def main():
    eprint("Loading en.default.schema.json...")
    with open("locales/en.default.schema.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    unique_strings = set()
    get_all_strings(data, unique_strings)
    strings_list = list(unique_strings)
    
    eprint(f"Found {len(strings_list)} unique strings to translate.")
    
    translator = GoogleTranslator(source='en', target='es')
    translation_map = {}
    
    batch_size = 50
    for i in range(0, len(strings_list), batch_size):
        batch = strings_list[i:i+batch_size]
        eprint(f"Translating batch {i//batch_size + 1}/{(len(strings_list) + batch_size - 1)//batch_size}...")
        try:
            # We can translate a batch list
            translated_batch = translator.translate_batch(batch)
            for orig, trans in zip(batch, translated_batch):
                translation_map[orig] = trans
        except Exception as e:
            eprint(f"Error on batch: {e}. Translating one by one...")
            for text in batch:
                try:
                    translation_map[text] = translator.translate(text)
                except Exception as ex:
                    eprint(f"Error translating '{text}': {ex}")
                    translation_map[text] = text
                time.sleep(0.5)
        time.sleep(1) # delay to avoid rate limit
        
    eprint("Replacing strings in JSON...")
    translated_data = replace_strings(data, translation_map)
    
    eprint("Saving es.schema.json...")
    with open("locales/es.schema.json", "w", encoding="utf-8") as f:
        json.dump(translated_data, f, ensure_ascii=False, indent=4)
        
    eprint("Done!")

if __name__ == "__main__":
    main()
