# stage_01.py

STAGE = "one"

try:
    with open("output_stage_one.txt", "w") as f:
        f.write(f"Stage {STAGE} started successfully...")
    print("Message written to output_stage_one.txt successfully.")
except Exception as e:
    print(f"Error: {e}")
