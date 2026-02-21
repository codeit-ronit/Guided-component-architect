from validator import validate_component

test_code = """
<div style="color: #ff0000;">
  <h1>Hello</h1>
"""


result = validate_component(test_code)

print("Valid:", result.is_valid)
print("Errors:", result.errors)
