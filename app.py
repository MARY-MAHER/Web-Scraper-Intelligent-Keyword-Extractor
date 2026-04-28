import re
from collections import Counter

def extract_real_keywords(input_path, output_path):
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            raw_content = f.read()
        text = raw_content.lower()
        text = re.sub(r'[أإآٱ]', 'ا', text)
        text = re.sub(r'ة', 'ه', text)
        text = re.sub(r'ى', 'ي', text)
        text = re.sub(r'[^a-z0-9ا-ي\s]', ' ', text)
        
        words = " ".join(text.split()).split()
        total_words = len(words)
        forbidden = {
            "في", "من", "على", "الى", "عن", "مع", "هذا", "هذه", "كان", "يكون", "و", "او", "ثم", 
            "000", "اضغط", "هنا", "تصل", "تبدا", "سنة", "سنوات", "جنيه", "مصري", "الشيخ", "زايد"
        }
        potential_keywords = Counter()
        for n in range(2, 5):
            for i in range(len(words) - n + 1):
                phrase = " ".join(words[i:i+n])
                p_words = phrase.split()
                
                if p_words[0] in forbidden or p_words[-1] in forbidden:
                    continue
                
                if all(w.isdigit() for w in p_words):
                    continue
                    
                potential_keywords[phrase] += 1

        sorted_keys = sorted(potential_keywords.keys(), key=lambda x: len(x.split()), reverse=True)
        final_counts = dict(potential_keywords)

        for i, long_p in enumerate(sorted_keys):
            count_long = final_counts.get(long_p, 0)
            if count_long <= 0: continue
            
            for j in range(i + 1, len(sorted_keys)):
                short_p = sorted_keys[j]
                if f" {short_p} " in f" {long_p} " or long_p.startswith(short_p) or long_p.endswith(short_p):
                    final_counts[short_p] -= count_long

        keywords_list = []
        for phrase, count in final_counts.items():
            if count >= 2:
                percentage = round((count / total_words) * 100, 1)
                keywords_list.append((phrase, count, percentage))

        keywords_list.sort(key=lambda x: x[1], reverse=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("[\n")
            for item in keywords_list[:40]: 
                f.write(f"  ('{item[0]}', {item[1]}, {item[2]}),\n")
            f.write("]")
        
        print(f"done {output_path}")

    except Exception as e:
        print(f" error: {e}")

in_file = r"C:\Users\HomePC\Desktop\New Text Document.txt"
out_file = r"C:\Users\HomePC\Desktop\Keywords.txt"

extract_real_keywords(in_file, out_file)
