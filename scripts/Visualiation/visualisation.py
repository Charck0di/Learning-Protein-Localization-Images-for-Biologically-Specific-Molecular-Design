import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define the docking results
data = {
    'Ligand': ['ligands23', 'ligands11', 'ligands19', 'ligands25', 'ligands6', 'ligands4', 'ligands14', 'ligands10', 
               'ligands20', 'ligands2', 'ligands7', 'ligands15', 'ligands12', 'ligands21', 'ligands5', 'ligands18', 
               'ligands1', 'ligands13', 'ligands24', 'ligands9', 'ligands8', 'ligands3', 'ligands17', 'ligands16'],
    'BindingEnergy (kcal/mol)': [-8.36, -7.87, -7.84, -7.56, -6.73, -6.13, -5.37, -5.28, -5.12, -4.43, -4.08, -3.98, 
                                 -3.38, -3.06, -2.29, -2.07, -1.69, -1.32, -0.88, 4.37, 6.34, 57.77, 78.85, 121.61]
}

# Create DataFrame
df = pd.DataFrame(data)

# Sort DataFrame by BindingEnergy (kcal/mol)
df = df.sort_values('BindingEnergy (kcal/mol)', ascending=True)

# Fancy style
sns.set_style('whitegrid')

# Plot
plt.figure(figsize=(12, 7))

# Use seaborn to create a bar plot
sns.barplot(x='Ligand', y='BindingEnergy (kcal/mol)', data=df, palette='viridis')

# Add title and labels
plt.title('Docking Results', fontsize=16)
plt.xlabel('Ligand', fontsize=14)
plt.ylabel('Binding Energy (kcal/mol)', fontsize=14)

# Rotate the x labels for better readability
plt.xticks(rotation=90)

# Display the plot
plt.tight_layout()
plt.show()