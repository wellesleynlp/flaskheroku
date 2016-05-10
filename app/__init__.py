from flask import Flask, render_template, request

app = Flask(__name__)

# global dictionary of anagrams
analists = [line.split() for line in open('data/anagrams.txt').readlines()]
analists = dict([(line[0], line[1:]) for line in analists])

def find_anagrams(word):
    anagrams = analists.get(''.join(sorted(word.lower())), [])
    if anagrams == [] or anagrams == [word]:  # no anagrams besides word
        return 'None found'
    else:
        return ', '.join([w for w in anagrams if w!=word])

@app.route('/', methods=['GET', 'POST'])
def intro():
    if request.method == 'GET':
        return render_template('frontpage.html')
    elif request.method == 'POST':
        return render_template('frontpage.html', word = request.form["word"], results = find_anagrams(request.form["word"]))
