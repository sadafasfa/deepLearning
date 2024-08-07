def run_combination_therapy():
    """Function for combination therapy analysis."""
    if not best_combinations:
        result_text_combination.delete('1.0', tk.END)
        result_text_combination.insert(tk.END, "No combination therapy results. Run the genetic algorithm first.", "bold")
        return
    

    combination_results = []
    
    for i in range(len(best_combinations) - 1):
        drug1, targets1 = best_combinations[i]
        for j in range(i + 1, len(best_combinations)):
            drug2, targets2 = best_combinations[j]
            shared_targets = set(targets1) & set(targets2)
            if shared_targets:
                combination_results.append((drug1, drug2, len(shared_targets), shared_targets))
    

    combination_results.sort(key=lambda x: x[2], reverse=True)
    
    result_text_combination.delete('1.0', tk.END)
    if combination_results:
        for drug1, drug2, shared_count, shared_targets in combination_results:
            result_text_combination.insert(tk.END, f"{drug1} and {drug2} collectively target: {', '.join(shared_targets)}\n\n", "bold")
    else:
        result_text_combination.insert(tk.END, "No significant combination found.", "bold")

app = tk.Tk()
app.title("DrugTargetTool 1.0.0")
app.geometry("800x600")
app.config(bg="lightblue")


header_frame = tk.Frame(app, bg="lightblue")
header_frame.pack(fill=tk.X)

title_label = tk.Label(header_frame, text="Drug Combination  By Genetic Algorithm", bg="lightblue", font=("Helvetica", 12))
title_label.pack(side=tk.LEFT, padx=10)

developer_label = tk.Label(header_frame, text="Sadaf&Reza, Aug 2024", bg="lightblue", font=("Helvetica", 8))
developer_label.pack(side=tk.RIGHT, padx=10)

notebook = ttk.Notebook(app)
notebook.pack(pady=10, expand=True)

tab_drugcomga = ttk.Frame(notebook)
tab_combination = ttk.Frame(notebook)

notebook.add(tab_drugcomga, text='Top Drugs')
notebook.add(tab_combination, text='Combination Therapy')

selected_file_path = ""


instructions = """
Instructions:
1. Click 'Choose File' to select a CSV or Excel file containing 'Drug' and 'Target' columns.
2. Enter the number of top drugs to display.
3. Click 'Run' to start the genetic algorithm.
4. Results will be displayed and saved to your desktop as 'result.xlsx'.
"""
tk.Label(tab_drugcomga, text=instructions, bg="lightblue", justify=tk.LEFT).pack(pady=10)

file_label = tk.Label(tab_drugcomga, text="No file selected")
file_label.pack(pady=10)

choose_file_button = tk.Button(tab_drugcomga, text="Choose File", command=choose_file, bg="lightblue")
choose_file_button.pack(pady=5)

tk.Label(tab_drugcomga, text="Number of Top Drugs:").pack(pady=5)
num_top_drugs_entry = tk.Entry(tab_drugcomga)
num_top_drugs_entry.pack(pady=5)

progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(tab_drugcomga, orient="horizontal", length=400, mode="determinate", variable=progress_var, maximum=100)
progress_bar.pack(pady=10)

run_button = tk.Button(tab_drugcomga, text="Run", command=on_run, bg="lightblue")
run_button.pack(pady=10)

result_text = ScrolledText(tab_drugcomga, width=80, height=20)
result_text.pack(pady=10)
result_text.tag_configure("bold", font=("Helvetica", 10, "bold"))

tk.Label(tab_combination, text="Combination Therapy Analysis").pack(pady=10)
run_combination_button = tk.Button(tab_combination, text="Run Combination Therapy", command=run_combination_therapy, bg="lightblue")
run_combination_button.pack(pady=10)

result_text_combination = ScrolledText(tab_combination, width=80, height=20)
result_text_combination.pack(pady=10)
result_text_combination.tag_configure("bold", font=("Helvetica", 10, "bold"))


app.mainloop()