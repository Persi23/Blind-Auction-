from flask import Flask, render_template, request

app = Flask(__name__)


def select_the_winner(data):
    highest_bid = 0
    winner_name = ""
    for name, bid in data.items():
        if bid > highest_bid:
            highest_bid = bid
            winner_name = name
    return winner_name, highest_bid

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        bid_str = request.form.get("bid")

        if bid_str and bid_str.isdigit():
            bid = int(bid_str)
        else:
            return render_template("index.html", message="Please enter a valid bid amount.")

        more_bidders = request.form.get("more_bidders")


        if 'bids' not in app.config:
            app.config['bids'] = {}
        app.config['bids'][name] = bid

        if more_bidders == "no":
            winner_name, highest_bid = select_the_winner(app.config['bids'])
            return render_template("winner.html", winner_name=winner_name, highest_bid=highest_bid)
        else:
            return render_template("index.html", message="Bid placed successfully! Waiting for other bidders...")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=False, host='127.0.0.1')
