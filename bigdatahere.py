from flask import Flask, request, render_template_string

app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { 
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; 
            background: url('https://images.unsplash.com/photo-1506744038136-46273834b3fb?q=80&w=2670&auto=format&fit=crop') no-repeat center center fixed; 
            background-size: cover;
            display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; 
        }
        .card { 
            /* Refined Liquid Glass Effect */
            background: rgba(255, 255, 255, 0.7); 
            backdrop-filter: blur(20px); 
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.3);
            padding: 50px; 
            border-radius: 35px; 
            box-shadow: 0 30px 60px rgba(0,0,0,0.15); 
            width: 100%; 
            max-width: 450px; 
            text-align: center; 
        }
        
        h2 { color: #1d1d1f; font-weight: 700; font-size: 2.2rem; margin-bottom: 30px; letter-spacing: -0.5px; }
        
        input { width: 100%; padding: 15px; margin: 10px 0; background: rgba(255,255,255,0.6);
                border: 1px solid rgba(255,255,255,0.5); border-radius: 14px; 
                box-sizing: border-box; font-size: 16px; outline: none; transition: 0.3s; }
        input:focus { background: rgba(255,255,255,0.9); }
        
        button { width: auto; padding: 12px 25px; background-color: #0071e3; color: white; border: none; 
                 border-radius: 20px; font-size: 14px; font-weight: 600; cursor: pointer; 
                 transition: all 0.3s ease; margin-top: 25px; box-shadow: 0 4px 15px rgba(0,113,227,0.3); }
        button:hover { background-color: #0077ed; transform: translateY(-2px); }
        
        .result { margin-top: 30px; padding: 20px; background: rgba(255, 255, 255, 0.4); border-radius: 20px; }
    </style>
</head>
<body>
    <div class="card">
        <h2>EcoTrack</h2>
        <form method="POST">
            <input type="number" name="commute" placeholder="Daily Commute (km)" required>
            <input type="number" name="meat" placeholder="Meat meals per week" required>
            <button type="submit">GET MY SCORE</button>
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
