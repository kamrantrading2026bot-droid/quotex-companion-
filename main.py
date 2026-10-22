
from flask import Flask, jsonify
import os

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, initial-scale=1">
    <title>VIP AI SIGNAL BOARD</title>
    <style>
        body {
            background: #101722;
            color: white;
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 20px;
        }
        .panel {
            background: #1d2938;
            padding: 24px;
            border-radius: 15px;
            max-width: 450px;
            margin: 30px auto;
        }
        .signal {
            font-size: 24px;
            font-weight: bold;
            margin: 25px 0;
        }
        .status {
            color: #f0c75e;
            line-height: 1.6;
        }
    </style>
</head>
<body>
    <div class="panel">
        <h2>VIP AI SIGNAL BOARD</h2>
        <p>QUOTEX OTC | 1-MINUTE CHART</p>
        <div class="signal">WAIT</div>
        <p class="status">
            Market data is not connected.<br>
            No verified trading signal is available.
        </p>
        <p>Signal Status: NOT ANALYZED</p>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return HTML

@app.route("/health")
def health():
    return jsonify({
        "status": "online",
        "signal": "WAIT",
        "market_data_connected": False,
        "analysis_complete": False
    })

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8080))
    )
