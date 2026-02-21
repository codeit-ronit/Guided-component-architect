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

## 🛠 Running Locally

### Backend

cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py


### Frontend

cd frontend
npm install
npm run dev



---

## ⚠ Assumptions

- Tailwind CSS is pre-installed in frontend.
- Angular runtime is not required for preview (HTML extracted only).
- Groq API is used for LLM inference.
