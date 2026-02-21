import json
import re


class ValidationResult:
    def __init__(self, is_valid, errors):
        self.is_valid = is_valid
        self.errors = errors


def load_design_system():
    with open("design-system.json", "r") as f:
        return json.load(f)


def check_bracket_balance(code):
    stack = []
    brackets = {"{": "}", "(": ")", "[": "]"}

    for char in code:
        if char in brackets:
            stack.append(brackets[char])
        elif char in brackets.values():
            if not stack or stack.pop() != char:
                return False

    return len(stack) == 0


def check_design_token_compliance(code, design_system):
    errors = []

    allowed_colors = list(design_system["colors"].values())

    # Find all hex colors used in code
    hex_colors = re.findall(r"#[0-9a-fA-F]{6}", code)

    for color in hex_colors:
        if color not in allowed_colors:
            errors.append(f"Unauthorized color used: {color}")

    return errors


def validate_component(code):
    # Remove markdown fences if present
    code = re.sub(r"```.*?\n", "", code)
    code = re.sub(r"```", "", code)

 
    
    errors = []

    design_system = load_design_system()

    # 1️⃣ Check bracket balance
    if not check_bracket_balance(code):
        errors.append("Bracket mismatch detected.")

    # 2️⃣ Check design token compliance
    token_errors = check_design_token_compliance(code, design_system)
    errors.extend(token_errors)

    # 4️⃣ Check RGBA usage
    rgba_errors = check_rgba_usage(code, design_system)
    errors.extend(rgba_errors)

    return ValidationResult(len(errors) == 0, errors)



def check_tailwind_class_compliance(code, design_system):
    errors = []

    allowed_colors = list(design_system["colors"].values())
    allowed_radius = design_system["borderRadius"]

    # Extract class="...."
    class_blocks = re.findall(r'class="([^"]+)"', code)

    for block in class_blocks:
        classes = block.split()

        for cls in classes:
            # Check color utilities
            if cls.startswith(("bg-", "text-", "border-")):
                
                # Allow hex format like bg-[#6366f1]
                hex_match = re.search(r"#([0-9a-fA-F]{6})", cls)
                
                if hex_match:
                    color = f"#{hex_match.group(1)}"
                    if color not in allowed_colors:
                        errors.append(f"Unauthorized color used in class: {cls}")
                else:
                    errors.append(f"Non-HEX Tailwind color used: {cls}")

            # Check border radius
            if cls.startswith("rounded"):
                errors.append(
                    f"Unauthorized border radius class used: {cls}. "
                    f"Use inline style with border-radius: {allowed_radius}"
                )

    return errors

def check_rgba_usage(code, design_system):
    errors = []

    # detect rgba or rgb usage
    rgba_matches = re.findall(r"rgba?\([^)]+\)", code)

    if rgba_matches:
        errors.append(
            "RGBA/RGB colors are not allowed. Use HEX colors from design system only."
        )

    return errors

