import os

files = [
    "1-0.persona-spectrum.md",
    "1.persona-spectrum.md",
    "2.persona-spectrum-final.md",
    "3.persona-cards.md",
    "4.persona-validation-report.md",
    "5.persona-spectrum-map.md",
    "6.customer-journey-map.md"
]

replacements = {
    "?듭떖1": "핵심1",
    "?듭떖2": "핵심2",
    "?뺤옣1": "확장1",
    "洹밸떒1": "극단1",
    "洹밸떒2": "극단2",
    "鍮꾪솢??": "비활성1"
}

dir_path = r"c:\Users\a\modu2026\w2-2Persona-CJM"

for file_name in files:
    file_path = os.path.join(dir_path, file_name)
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        modified = False
        for k, v in replacements.items():
            if k in content:
                content = content.replace(k, v)
                modified = True
                
        if modified:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Fixed {file_name}")
