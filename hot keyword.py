import re
from collections import Counter

def final_residual_cleaner(input_path, output_path):
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            text = f.read()

        text = text.lower()
        text = re.sub(r"[أإآ]", "ا", text)
        text = re.sub(r"ة", "ه", text)
        text = re.sub(r"ى", "ي", text)
        text = re.sub(r"[^\w\s]", " ", text)
        words = text.split()
        
        all_counts = Counter()
        for n in range(2, 7):
            phrases = [" ".join(words[i:i+n]) for i in range(len(words)-n+1)]
            all_counts.update(phrases)
        final_counts = dict(all_counts)
        sorted_phrases = sorted(final_counts.keys(), key=lambda x: len(x.split()), reverse=True)
        for i, long_phrase in enumerate(sorted_phrases):
            long_val = final_counts[long_phrase]
            if long_val <= 0: continue
            
            for j in range(i + 1, len(sorted_phrases)):
                short_phrase = sorted_phrases[j]
                if short_phrase in long_phrase:
                    final_counts[short_phrase] -= long_val

        with open(output_path, 'w', encoding='utf-8') as f_out:            
            sorted_final = sorted(final_counts.items(), key=lambda x: x[1], reverse=True)
            
            for phrase, count in sorted_final:
                if count > 1:
                    f_out.write(f"[{count}]: {phrase}\n")

        return f"{output_path}"

    except Exception as e:
        return f" error: {e}"

in_p = r"C:\Users\HomePC\Desktop\New Text Document.txt"
out_p = r"C:\Users\HomePC\Desktop\Final_Clean_Report.txt"
print(final_residual_cleaner(in_p, out_p))
