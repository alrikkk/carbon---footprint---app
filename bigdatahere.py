from flask import Flask, request, render_template_string

app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html>
<head>
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">
    <style>
        body { 
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; 
            background: url('https://images.unsplash.com/photo-1506744038136-46273834b3fb?q=80&w=2670&auto=format&fit=crop') no-repeat center center fixed; 
            background-size: cover;
            display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; 
        }
        .card { 
            background: rgba(255, 255, 255, 0.4); 
            backdrop-filter: blur(25px) saturate(180%); 
            border: 1px solid rgba(255, 255, 255, 0.5);
            background-image: linear-gradient(135deg, rgba(255,255,255,0.4) 0%, rgba(255,255,255,0.1) 100%);
            padding: 50px; border-radius: 40px; 
            box-shadow: 0 40px 80px rgba(0,0,0,0.2); 
            width: 100%; max-width: 450px; text-align: center;
        }
        
        .header-container { display: flex; justify-content: center; align-items: center; gap: 15px; margin-bottom: 30px; }
        
        h2 { 
            font-family: 'Press Start 2P', cursive;
            color: #ffffff; font-size: 1.5rem; 
            text-shadow: 4px 4px 0px #000000; 
        }
        
        /* Updated to Headphones icon */
        .headphones { 
            width: 45px; height: auto; 
            animation: float 3s ease-in-out infinite;
            image-rendering: pixelated;
        }
        
        @keyframes float { 0% { transform: translateY(0px); } 50% { transform: translateY(-10px); } 100% { transform: translateY(0px); } }

        input { 
            width: 100%; padding: 15px; margin: 10px 0; 
            background: rgba(200, 200, 200, 0.5); 
            border: 1.5px solid rgba(255, 255, 255, 0.8); 
            border-radius: 15px; box-sizing: border-box; font-size: 16px; outline: none; color: white; 
        }
        input::placeholder { color: rgba(255, 255, 255, 0.9); }
        input:focus { background: rgba(200, 200, 200, 0.7); border-color: white; }
        
        button { 
            width: auto; padding: 12px 30px; background: rgba(0, 113, 227, 0.8); color: white; border: none; 
            border-radius: 20px; font-size: 14px; font-weight: 600; cursor: pointer; 
            transition: all 0.4s ease; margin-top: 25px; 
        }
        button:hover { background: rgba(255, 105, 180, 0.9); transform: translateY(-3px); }
        
        .result { margin-top: 30px; padding: 25px; background: rgba(255, 255, 255, 0.2); border-radius: 25px; color: white; }
        
        .shake { animation: shake 0.5s; }
        @keyframes shake { 0%, 100% {transform: translateX(0);} 25% {transform: translateX(-5px);} 75% {transform: translateX(5px);} }
    </style>
</head>
<body>
    <div class="card" id="card">
        <div class="header-container">
            <h2>ECOTRACK</h2>
            <img src="https://cdn-icons-png.flaticon.com/512/3067/3067425.png" class="headphones" alt="Headphones">
        </div>
        <form method="POST">
            <input type="number" name="commute" inputmode="numeric" placeholder="Daily Commute (km)" required>
            <input type="number" name="meat" inputmode="numeric" placeholder="Meat meals per week" required>
            <button type="submit">GET MY SCORE</button>
        </form>
        {% if footprint %}
            <div class="result" id="result-box">
                <p>Weekly Emissions: <strong>{{ footprint }} kg</strong></p>
                <p>Rank: <strong>{{ rank }}</strong></p>
            </div>
            <script>
                {% if rank == "Eco-Warrior 🏆" %}
                    confetti({ particleCount: 150, spread: 70, origin: { y: 0.6 } });
                {% elif rank == "Needs Improvement 🥉" %}
                    document.getElementById('card').classList.add('shake');
                {% endif %}
            </script>
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
