from pathlib import Path
import json
root=Path(__file__).resolve().parent
content={p.relative_to(root).as_posix():p.read_text(encoding="utf-8") for p in sorted((root/"manuais").glob("**/*.md"))}
(root/"manual_content.js").write_text("window.MANUAL_CONTENT = "+json.dumps(content,ensure_ascii=False,indent=2)+";\n",encoding="utf-8")
print("manual_content.js atualizado com",len(content),"arquivos Markdown.")
