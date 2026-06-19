from flask import Flask, request, render_template_string

app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; 
               background-color: #f5f5f7; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .card { background: white; padding: 40px; border-radius: 25px; box-shadow: 0 20px 40px rgba(0,0,0,0.08); 
                width: 100%; max-width: 450px; text-align: center; }
        h2 { color: #1d1d1f; font-weight: 600; margin-bottom: 30px; }
        input { width: 100%; padding: 15px; margin: 10px 0; border: 1px solid #d2d2d7; border-radius: 12px; 
                box-sizing: border-box; font-size: 16px; }
        button { width: 100%; padding: 15px; background-color: #0071e3; color: white; border: none; 
                 border-radius: 12px; font-size: 16px; font-weight: 500; cursor: pointer; 
                 transition: background-color 0.3s ease; margin-top: 20px; }
        button:hover { background-color: #0077ed; }
        .result { margin-top: 30px; padding: 20px; background: #f5f5f7; border-radius: 20px; }
    </style>
</head>
<body>
    <div class="card">
        <h2>EcoTrack</h2>
        <form method="POST">
            <input type="number" name="commute" placeholder="Daily Commute (km)" required>
            <input type="number" name="meat" placeholder="Meat meals per week" required>
            <button type="submit">Calculate Impact</button>
        </form>
        {% if footprint %}
            <div class="result">
                <p>Weekly Emissions: <strong>{{ footprint }} kg</strong></p>
                <p>Rank: <strong>{{ rank }}</strong></p>
            </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    footprint, rank = None, None
    if request.method == 'POST':
        commute = float(request.form.get('commute', 0))
        meat = float(request.form.get('meat', 0))
        footprint = round((commute * 0.2) + (meat * 5), 2)
        if footprint < 50: rank = "Eco-Warrior 🏆"
        elif footprint < 150: rank = "Intermediate 🥈"
        else: rank = "Needs Improvement 🥉"
    return render_template_string(html_template, footprint=footprint, rank=rank)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
def index():
    footprint = None
    rank = None
    if request.method == 'POST':
        commute = float(request.form.get('commute', 0))
        meat = float(request.form.get('meat', 0))
        
        # Calculate score
        footprint = (commute * 0.2) + (meat * 5)
        
        # Determine Rank
        if footprint < 50:
            rank = "🌱 Eco-Warrior (Gold)"
        elif footprint < 150:
            rank = "🚶 Intermediate (Silver)"
        else:
            rank = "🌍 Needs Improvement (Bronze)"
            
    return render_template_string(html_template, footprint=footprint, rank=rank)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
