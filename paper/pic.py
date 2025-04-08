import matplotlib.pyplot as plt
import numpy as np

# Define data
models = ["Baichuan", "AiMed", "GPT4-Turbo", "MedRad-Baichuan", "MedRad-AiMed", "MedRad-GPT4-Turbo"]
qualitative_scores = [2, 3, 4, 3, 4, 5] 
clinical_scores = [3, 3, 4, 4, 5, 5] 

# Sort data in ascending order
qualitative_data = sorted(zip(models, qualitative_scores), key=lambda x: x[1])
clinical_data = sorted(zip(models, clinical_scores), key=lambda x: x[1])

# Extract sorted models and scores
models_qualitative, sorted_qualitative_scores = zip(*qualitative_data)
models_clinical, sorted_clinical_scores = zip(*clinical_data)

# Function to draw bar chart
def draw_bar_chart(models, scores, title, ax, colors):
    x = np.arange(len(models))
    ax.bar(x, scores, color=colors, edgecolor='black', linewidth=1)
    ax.set_xticks(x)
    ax.set_xticklabels(models, rotation=30, ha="right", fontsize=10)
    ax.set_yticks(np.arange(0, 6, 1))  # Ensure y-ticks are regularly spaced
    ax.set_ylim(0, 5.5)  # Set limit slightly above the max (5)
    ax.set_xlabel("Models", fontsize=11, labelpad=10)
    ax.set_ylabel("Score (Stars)", fontsize=11, labelpad=10)
    ax.set_title(title, fontsize=13, pad=15)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_linewidth(0.8)
    ax.spines["bottom"].set_linewidth(0.8)
    ax.grid(axis="y", linestyle="--", linewidth=0.6, alpha=0.5)

# Define consistent colors for each model
color_map = {
    "Baichuan": "#4E79A7",
    "AiMed": "#F28E2C",
    "GPT4-Turbo": "#76B7B2",
    "MedRad-Baichuan": "#E15759",
    "MedRad-AiMed": "#59A14F",
    "MedRad-GPT4-Turbo": "#EDC948"
}

colors_qualitative = [color_map[model] for model in models_qualitative]
colors_clinical = [color_map[model] for model in models_clinical]

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5), dpi=300)

draw_bar_chart(models_qualitative, sorted_qualitative_scores, "Qualitative QA", ax1, colors_qualitative)
draw_bar_chart(models_clinical, sorted_clinical_scores, "Clinical Diagnosis", ax2, colors_clinical)

# Save image with tight layout
fig.tight_layout(pad=2)
plt.savefig("acl_style_bar_charts.png", dpi=300)
plt.show()