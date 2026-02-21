import os
from datetime import datetime


def export_component(code, filename_prefix="generated_component"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{filename_prefix}_{timestamp}.ts"

    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)

    file_path = os.path.join(output_dir, filename)

    with open(file_path, "w") as f:
        f.write(code)

    return file_path
