# stage_03.py

STAGE = "Three"

try:
    with open("final_output.txt", "w") as f:
        f.write(f"Stage {STAGE} started successfully...")
    print("Message written to final_output.txt successfully.")
except Exception as e:
    print(f"Error: {e}")
