import subprocess

scripts = ["extract.py", "transform.py", "load.py", "upload_to_s3.py"]

for script in scripts:
    print(f"Running {script}...")
    subprocess.run(["python", script], check=True)

print("Pipeline complete.")