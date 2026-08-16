from pathlib import Path
root=Path(__file__).resolve().parents[1]
print("SAMSLT repository:",root)
print("Top-level folders:",[p.name for p in root.iterdir() if p.is_dir()])
