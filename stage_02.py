# stage_02.py

STAGE = "Two"

try:
    with open("output_stage_two.txt", "w") as f:
        f.write(f"Stage {STAGE} started successfully...")
    print("Message written to output_stage_two.txt successfully.")
except Exception as e:
    print(f"Error: {e}")
