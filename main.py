from generator import generate_component
from self_corrector import generate_with_self_correction
from exporter import export_component
from validator import load_design_system
from editor import edit_component


def main():


    design_system = load_design_system()
    current_component = None
    while True :
        if not current_component :
            user_prompt = input("Enter component description: ")
            
            current_component = generate_with_self_correction(
                user_prompt=user_prompt,
                generator_function=generate_component
            )
        else :
            user_prompt = input("\nEnter edit instruction (or type 'exit'): ")

            if user_prompt.lower() == "exit":
                break

            edited = edit_component(
                previous_code=current_component,
                user_instruction=user_prompt,
                design_system=design_system
            )

            current_component = generate_with_self_correction(
                user_prompt=edited,
                generator_function=lambda x: x
            )

        print("\n===== CURRENT COMPONENT =====\n")
        print(current_component)

 

    save = input("\nSave component to file? (y/n): ")
    if save.lower() == "y":
        path = export_component(current_component)
        print(f"Saved to: {path}")



if __name__ == "__main__":
    main()
