from utils import call_llm
import json


def edit_component(previous_code, user_instruction, design_system):
    system_prompt = f"""
You are an Angular component editor.

STRICT RULES:
- Modify the existing component based on instruction.
- Do NOT remove existing functionality.
- Maintain design token compliance.
- Use HEX colors only.
- Border radius must be {design_system["borderRadius"]}.
- Output raw Angular component code only.
- No markdown.
- No explanations.
"""

    user_prompt = f"""
EXISTING COMPONENT:
{previous_code}

EDIT INSTRUCTION:
{user_instruction}

Apply changes and return full updated component.
"""

    return call_llm(system_prompt, user_prompt)
