from flask import Flask, request, render_template_string

app = Flask(__name__)

# A slightly more advanced HTML/CSS template
html_template = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { font-family: sans-serif; text-align: center; padding: 50px; background-color: #f4f7f6; }
        .card { background: white; padding: 20px; border-radius: 10px; display: inline-block; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }
        h1 { color: #2c3e50; }
        .rank { font-weight: bold; color: #e67e22; font-size: 1.5em; }
    </style>
</head>
<body>
    <div class="card">
        <h1>EcoTrack</h1>
        <form method="POST">
            Daily Commute (km): <input type="number" name="commute" required><br><br>
            Meat meals per week: <input type="number" name="meat" required><br><br>
            <input type="submit" value="Calculate Rank">
        </form>
        {% if footprint %}
            <h2>Weekly CO2: {{ footprint }} kg</h2>
            <p>Your Rank: <span class="rank">{{ rank }}</span></p>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
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
