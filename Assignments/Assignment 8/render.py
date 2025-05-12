import subprocess

seasons = [
    "Season 1", "Season 2", "Season 3",
    "Season 4", "Season 5", "Season 6"
]

for season in seasons:
    output_name = f"sopranos_{season.replace(' ', '_')}.pdf"
    print(f"Rendering {output_name}...")

    subprocess.run([
        "quarto", "render", "Sopranos.qmd",
        "--to", "pdf",
        "--execute",
        "-P", f"season='{season}'",
        "--output", output_name
    ])
