import nbformat
from pathlib import Path

def clear_notebook_outputs(notebook_path):
    with open(notebook_path) as f:
        nb = nbformat.read(f, as_version=4)
    
    for cell in nb.cells:
        if cell.cell_type == 'code':
            cell.outputs = []
            cell.execution_count = None
    
    with open(notebook_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)

# Clear all notebooks in current directory
notebooks = Path('.').glob('*.ipynb')
for notebook in notebooks:
    clear_notebook_outputs(str(notebook))
