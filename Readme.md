# Guided Component Architect

A governed, agentic code-generation system that transforms natural language prompts into fully structured Angular components while enforcing strict design-system compliance.

## 🚀 Objective

This project demonstrates:

- Agentic LLM workflows
- Deterministic validation layers
- Self-correction loops
- Design-system governance enforcement
- Structured Angular component generation
- Live preview integration

---

## 🏗 Architecture

User Prompt  
↓  
Generator Agent (Angular component generation)  
↓  
Validator Agent (Design token + syntax enforcement)  
↓  
Self-Correction Loop (Automatic repair using error logs)  
↓  
Final Component Output  

---

## 🔁 Agentic Loop

1. The Generator produces a full Angular component.
2. The Validator checks:
   - Unauthorized colors
   - HEX-only enforcement
   - Tailwind misuse
   - RGBA restrictions
   - Bracket balance
3. If invalid:
   - Errors are fed back into a Repair Agent.
   - The model regenerates corrected code.
4. Loop runs up to 3 retries.

This ensures governed, production-safe output.

---

## 🎨 Design System

The system strictly enforces tokens defined in: 
design-system.json


This ensures:

- Consistent theming
- No arbitrary colors
- Border-radius governance
- Font consistency

---

## 🖥 Live Preview

The frontend allows:

- Pasting generated Angular components
- Viewing full TypeScript code
- Extracting and rendering the template section
- Switching between Code and Preview

---

## 🧠 Key Features

- Deterministic validation layer
- Self-healing retry mechanism
- Multi-turn editing support
- Export functionality
- Separation of generation and repair agents

---

# 🚀 Running the Project Locally

This project consists of two parts:

- 🧠 Backend (Agentic Angular Code Generator)
- 🖥 Frontend (Live Preview Studio)

Both must be run separately.

---

## 🔹 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/guided-component-architect.git
cd guided-component-architect
Step 1 — Create Virtual Environment
cd backend
python -m venv venv
source venv/bin/activate
Step 2 — Install Dependencies
pip install -r requirements.txt
Step 3 — Add Environment Variables

Create a .env file inside backend/:

GROQ_API_KEY=your_groq_api_key_here
Step 4 — Run Backend CLI
python main.py
Step 1 — Install Dependencies
cd ../frontend
npm install

🔹 Step 2 — Run Development Server
npm run dev


Open:

http://localhost:3000




---

## ⚠ Assumptions

- Tailwind CSS is pre-installed in frontend.
- Angular runtime is not required for preview (HTML extracted only).
- Groq API is used for LLM inference.
