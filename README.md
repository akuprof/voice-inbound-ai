Here’s your complete README.md content to include in the root of your olge-website GitHub repo:

⸻


# 🇮🇳 OLGE Website — Online Crime Investigation & Legal Grievance Enforcement

> Presented by **Akbar Ali.S, B.Voc(IT)**  
> Certified Cyber Forensic Associate  
> _"Justice. Vigilance. Action." – நீதியும், விழிப்புணர்வும், நடவடிக்கையும்._

---

## 🔧 Project Overview

This is a mobile-first public interface to help Indian citizens:
- File online cybercrime complaints
- Talk to an AI Legal Assistant (Tamil + English)
- Learn rights & protections under law
- Volunteer to support OLGE awareness campaigns

---

## 🖥️ Tech Stack

- **HTML + Tailwind CSS** (no frameworks required)
- **jsPDF** (client-side PDF generation)
- **ElevenLabs Voice Assistant** (API embed)
- **No backend/server required** (for MVP)

---

## 📂 Folder Structure

olge-website/
├── index.html               # Homepage with hero banner, CTA, ElevenLabs AI
├── complaint.html           # Complaint form with jsPDF export
├── assets/
│   └── images/
│       └── logo.png         # OLGE Logo
└── README.md                # This guide

---

## 🚀 Quick Start

### 1. Clone the Repo
```bash
git clone https://github.com/<your-username>/olge-website.git
cd olge-website

2. Run Locally

Just open index.html or complaint.html in your browser.

No server setup needed.

⸻

📦 CDN Resources

Tailwind CSS

<link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">

jsPDF

<script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>


⸻

🔐 ElevenLabs Integration

To embed the Tamil-English voice assistant, you’ll need your own ElevenLabs API Key.

const response = await fetch("https://api.elevenlabs.io/v1/convai/settings/dashboard", {
  method: "GET",
  headers: {
    "Xi-Api-Key": "<your-api-key>"
  },
});


⸻

📲 Deployment

Option 1: Netlify
	•	Drag olge-website/ folder into Netlify
	•	Site is live instantly

Option 2: Vercel
	•	Install Vercel CLI
	•	vercel deploy

⸻

✅ Features
	•	🇮🇳 Tamil-English content and UI
	•	🔰 FIR Auto Generator (PDF)
	•	🎙️ AI Police Assistant
	•	📄 Legal Rights FAQ
	•	🧑‍💼 Volunteer Signup + Badge

⸻

📫 Contact & Community
	•	WhatsApp: 9600210429
	•	Telegram: @the_ai_professor
	•	Email: politicai123@gmail.com

⸻

Built with ❤️ for a safer digital India
பாதுகாப்பான இணைய இந்தியாவுக்காக உருவாக்கப்பட்டது

---

✅ You can now copy this into your repo’s `README.md` file.

Let me know if you'd like a GitHub Actions CI/CD config, privacy policy template, or bot webhook setup next.
