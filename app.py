from flask import Flask, render_template

app = Flask(__name__)

house_pts = {"artemis": 3,
          "helios": 60,
          "athena": 34,
          "poseidon": 1
          }

house_colours = {"artemis": "green",
                 "helios": "red",
                 "athena": "purple",
                 "poseidon": "blue"
                 }

past_words = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<text>")
def info(text):
    if text in house_pts.keys():
        house_colour = house_colours[text]
        house_pt = house_pts[text]
        return render_template("house.html", house=text, house_colour=house_colour, house_pt=house_pt)
    else:
        len_text = len(text)
        cons_count = 0
        vow_count = 0
        letter_freq = {}
        for char in text:
            if char.isalpha():
                if char in "AEIOUaeiou":
                    vow_count += 1
                else:
                    cons_count += 1
            char = char.lower()
            if char not in letter_freq.keys():
                letter_freq[char] = 1
            else:
                letter_freq[char] += 1

        past_words.append(text)
        return render_template("analysis.html", text=text, len_text=len_text, vow_count=vow_count, cons_count=cons_count, letter_freq=letter_freq, past_words=past_words)

if __name__ == "__main__":
    app.run(port=5555)

