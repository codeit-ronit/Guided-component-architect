import json
import logging
from utils import call_llm
from validator import validate_component

logging.basicConfig(level=logging.INFO)

MAX_RETRIES = 3


def build_fix_prompt(original_code, errors, design_system):
    return f"""
You are an Angular code repair agent.

The following component has errors:

ERRORS:
{errors}

ORIGINAL CODE:
{original_code}

DESIGN SYSTEM:
{json.dumps(design_system, indent=2)}

Fix the component so that:
- Do NOT reference designSystem as a variable.
- Do NOT use {{ }} interpolation.
- Replace tokens with actual HEX values.
- All colors must be raw HEX values.
- All brackets are balanced
- Only allowed design tokens are used
- No unauthorized colors
- Output raw Angular component code only
- No explanations
- No markdown.

Return corrected code only.
"""


def generate_with_self_correction(user_prompt, generator_function):
    from generator import generate_component
    from validator import load_design_system

    design_system = load_design_system()

    code = generator_function(user_prompt)

    for attempt in range(MAX_RETRIES):
        validation_result = validate_component(code)

        if validation_result.is_valid:
            return code

        logging.info(f"Attempt {attempt + 1} failed: {validation_result.errors}")

        fix_prompt = build_fix_prompt(
            original_code=code,
            errors=validation_result.errors,
            design_system=design_system
        )

        code = call_llm(
            system_prompt="You strictly repair Angular code.",
            user_prompt=fix_prompt
        )

    return code  # return last attempt even if invalid
