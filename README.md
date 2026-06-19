# EcoLife: Carbon Footprint Awareness Platform

EcoLife is an interactive, gamified web application designed to help individuals track and understand their environmental impact. By logging daily commute data and dietary habits, users receive a real-time carbon footprint score, personalized improvement tips, and a ranking to help gamify the journey toward a greener lifestyle.

## 🚀 The Inspiration
As a recent 12th-grade graduate, I wanted to build something that bridges the gap between complex climate data and daily personal habits. Most carbon calculators feel like boring forms; EcoLife turns sustainability into a retro-gaming experience, making it easier for users to engage with their environmental footprint.

## 🛠️ How I Built It
EcoLife was built with a focus on simplicity, speed, and user experience:
- **Backend:** Powered by **Flask (Python)** to handle request logic and dynamic template rendering.
- **Frontend:** Crafted with **HTML5, CSS3, and JavaScript**, utilizing a "Glassmorphism" design aesthetic.
- **Gamification:** Integrated **canvas-confetti** and custom CSS keyframe animations to provide immediate visual feedback based on user performance.
- **Persistence:** Utilized **Browser LocalStorage** to store user history and power a competitive, cross-session leaderboard without the need for a complex database backend.
- **Deployment:** Deployed on **Render** with automated CI/CD pipelines connected directly to this GitHub repository.

## 🎮 Features
- **Real-time Scoring:** Instant calculations for CO2 impact based on commute and diet.
- **Interactive UI:** Hover animations, progress bars, and a "retro" pixel-art aesthetic (Press Start 2P font).
- **Gamified Ranking:** Players are assigned ranks (Eco-Warrior, Intermediate, Needs Improvement) with unique visual cues like confetti for top performers.
- **Persistence:** Track your progress over time with a browser-based leaderboard.
- **Actionable Insights:** Every result includes a personalized tip to help users lower their footprint.

## 📈 Future Roadmap
While EcoLife is fully functional for this challenge, I have planned the following improvements for future iterations:
1. **Firebase Backend:** Moving from `localStorage` to a centralized Firebase database to enable global, cross-device leaderboards.
2. **Social Integration:** Adding a "Challenge a Friend" feature to share scores directly to social media.
3. **Advanced Analytics:** Detailed charts visualizing carbon reduction trends over months.

---
*Built with passion by Alrik for the PromptWars Virtual Challenge.*
