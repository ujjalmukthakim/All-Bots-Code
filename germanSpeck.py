import subprocess
from deep_translator import GoogleTranslator
import time

def start_listening_practice():
    translator = GoogleTranslator(source='en', target='de')
    english_text = 'hello, good morning. how are you doing? i am fine. do you want to spend time with us?\n yes, why not!'
    
    print("\nTranslating...")
    german_text = translator.translate(english_text)
    print(f"German Translation: {german_text}")
    
    # Using a very slow rate for clarity
    slow_rate = 60 
    speed_command = f"[[rate {slow_rate}]]"
    
    # Split by sentences
    sentences = [s.strip() for s in german_text.replace('!', '.').replace('?', '.').split('.') if s.strip()]
    
    print(f"\n--- Starting Practice ---")
    
    # We will do a few full cycles of the whole text
    for cycle in range(10):
        print(f"\nCycle {cycle+1}/10:")
        
        for sentence in sentences:
            # 1. Word-by-Word Pass
            words = sentence.split()
            print(f"  Focusing on: '{sentence}'")
            print("  - Word by word:")
            for word in words:
                subprocess.run(['say', '-v', 'Anna', f"{speed_command} {word}"])
                time.sleep(0.3) # Short pause between words
            
            # 2. Full-Sentence Pass
            print("  - Full sentence:")
            subprocess.run(['say', '-v', 'Anna', f"{speed_command} {sentence}"])
            
            # Pause between sentences
            time.sleep(1.0) 

    print("\nPractice session completed!")

if __name__ == "__main__":
    start_listening_practice()