import json
from utils import call_llm


def generate_component(user_prompt):
    with open("design-system.json", "r") as f:
        design_system = json.load(f)

    system_prompt = f"""
You are a strict Angular component generator.
You MUST generate a COMPLETE Angular standalone component including:

1. import {{ Component }} from '@angular/core';
2. @Component decorator
3. selector property
4. template property using backticks (` `)
5. styles array
6. export class ComponentName

STRICT RULES:
- Output full Angular TypeScript file.
- No explanations.
- Use inline HEX colors only.
- Do NOT use markdown.
- Do NOT use Tailwind named colors like bg-white, text-gray-500.
- Do NOT use rounded-xl or similar.
- Use ONLY these design tokens:

{json.dumps(design_system, indent=2)}

Use exact HEX codes from design system.
If a color is needed, use style="color: #xxxxxx"
Do not invent new tokens.
No markdown.
Only raw code.
"""


    return call_llm(system_prompt, user_prompt)
