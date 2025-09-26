import os
import subprocess

# Change this to your actual path
base_folder = r"C:\Akash_OneDrive\OneDrive\Desktop\CodeReviewBot"

sample_folder = os.path.join(base_folder, "sample_code")
output_folder = os.path.join(base_folder, "outputs")

# Create outputs folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Get all .py files in sample_code folder
try:
    py_files = [f for f in os.listdir(sample_folder) if f.endswith(".py")]
except FileNotFoundError:
    print(f"❌ ERROR: sample_code folder not found at {sample_folder}")
    exit(1)

# Run analysis tools on each file
for file in py_files:
    file_path = os.path.join(sample_folder, file)
    
    print(f"\n🔍 Analyzing {file}...\n")

    # -----------------------
    # Pylint
    pylint_output = os.path.join(output_folder, f"{file}_pylint.txt")
    print("Pylint results:")
    subprocess.run(f"pylint {file_path}", shell=True)
    subprocess.run(f"pylint {file_path} > \"{pylint_output}\"", shell=True)

    # -----------------------
    # Flake8
    flake8_output = os.path.join(output_folder, f"{file}_flake8.txt")
    print("\nFlake8 results:")
    subprocess.run(f"flake8 {file_path}", shell=True)
    subprocess.run(f"flake8 {file_path} > \"{flake8_output}\"", shell=True)

    # -----------------------
    # Radon - Cyclomatic Complexity
    radon_cc_output = os.path.join(output_folder, f"{file}_radon_cc.txt")
    print("\nRadon Cyclomatic Complexity:")
    subprocess.run(f"radon cc {file_path} -s", shell=True)
    subprocess.run(f"radon cc {file_path} -s > \"{radon_cc_output}\"", shell=True)

    # -----------------------
    # Radon - Maintainability Index
    radon_mi_output = os.path.join(output_folder, f"{file}_radon_mi.txt")
    print("\nRadon Maintainability Index:")
    subprocess.run(f"radon mi {file_path}", shell=True)
    subprocess.run(f"radon mi {file_path} > \"{radon_mi_output}\"", shell=True)

print("\n✅ Code analysis completed. Check the outputs folder for detailed files.")
