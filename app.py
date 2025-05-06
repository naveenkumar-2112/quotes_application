from flask import Flask, render_template
import datetime
import hashlib

app = Flask(__name__)

def load_quotes():
    with open('unique_quotes.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        quotes = []
        for line in lines:
            if '|' in line:
                text, author = line.strip().split('|', 1)
                quotes.append({'text': text, 'author': author})
        return quotes

@app.route('/')
def home():
    quotes = load_quotes()
    
    # Use a hash of the date to pick a deterministic quote of the day
    today_str = datetime.datetime.now().strftime('%Y-%m-%d')
    hash_value = int(hashlib.sha256(today_str.encode()).hexdigest(), 16)
    index = hash_value % len(quotes)
    
    quote = quotes[index]
    return render_template('index.html', quote=quote)

if __name__ == '__main__':
    app.run(debug=True)
