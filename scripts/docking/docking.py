import os
import shutil
import subprocess

# Paths
ligand_folder = "ligands"  # Folder containing all your ligand .pdbqt files
template_dpf = "template.dpf"  # Your prepared template DPF
output_folder = "batch_docking_results"

# AutoDock executable
autodock_exe = "autodock4.exe"  # Adjust if necessary (e.g., full path)

# Make sure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Read the template DPF once
with open(template_dpf, 'r') as file:
    template_dpf_content = file.read()

# Loop over all ligands
for ligand_file in os.listdir(ligand_folder):
    if ligand_file.endswith(".pdbqt"):
        ligand_name = os.path.splitext(ligand_file)[0]
        
        # Create a custom .dpf for each ligand
        dpf_content = template_dpf_content.replace("{ligand_name}", ligand_name)
        dpf_filename = os.path.join(output_folder, f"{ligand_name}.dpf")
        
        with open(dpf_filename, 'w') as dpf_file:
            dpf_file.write(dpf_content)
        
        # Copy ligand into output folder
        shutil.copy(os.path.join(ligand_folder, ligand_file), output_folder)

        # Run AutoDock
        print(f"Docking {ligand_name}...")
        subprocess.run([autodock_exe, "-p", dpf_filename, "-l", os.path.join(output_folder, f"{ligand_name}.dlg")])

print("Batch docking complete!")