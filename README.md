#  Automated Web Scraper & Intelligent Keyword Extractor

A Python-based tool designed to extract clean content from web pages and perform advanced **NLP-based frequency analysis**. The project features a custom "Residual Cleaning" algorithm to ensure accurate keyword extraction by preventing redundant frequency counts within nested n-grams.

##  Features

* **Robust Web Scraping:** Uses `BeautifulSoup` to extract the core body text while intelligently filtering out noise (scripts, styles, headers, footers, and navbars).
* **Arabic Text Normalization:** Comprehensive cleaning of Arabic characters (Normalization of Hamzas, Ta-Marbuta, and Alif-Maqsura) to ensure data consistency.
* **Multi-Range N-gram Analysis:** Generates and counts phrases ranging from 2-grams up to 6-grams.
* **Smart Residual Logic:** A custom algorithm that prevents "double counting." If a short phrase is part of a longer frequent phrase, its count is adjusted to reflect its true independent frequency.
* **Automated Reporting:** Generates a sorted frequency report of the most relevant "Hot Keywords."

##  Tech Stack

* **Python 3.x**
* **Libraries:** * `Requests`: For handling HTTP requests.
    * `BeautifulSoup4`: For parsing and cleaning HTML.
    * `Re`: For Regex-based text normalization.
    * `Collections (Counter)`: For efficient frequency mapping.

## 📖 How It Works

1.  **Extraction:** The `get_full_body_text` function fetches the URL and strips away non-content HTML elements.
2.  **Preprocessing:** Text is converted to lowercase, special characters are removed, and Arabic letters are normalized.
3.  **Tokenization:** The text is split into tokens to generate sequences (N-grams).
4.  **Residual Cleaning:** * The system sorts phrases from longest (6-grams) to shortest (2-grams).
    * It subtracts the occurrence of longer phrases from the counts of their constituent shorter phrases.
    * *Example:* If "Artificial Intelligence" appears 10 times, it won't inflate the count of the word "Intelligence" unnecessarily.

## 💻 Usage

```python
# 1. Scrape data
text = get_full_body_text('your_target_url')

# 2. Process and extract hot keywords
final_residual_cleaner('input_text.txt', 'final_report.txt')
```

## 📊 Sample Output
The output report follows this format:
```text
[15]: الشيخ زايد
[12]: مول ذا كور
[8]: وحدات اداريه’’
