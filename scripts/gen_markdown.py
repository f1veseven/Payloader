import json
from pathlib import Path

data=json.loads(Path("database/payloads.json").read_text())

db=data["data"]

out=["# Payloader Payload 手册\n"]

for group,payloads in db.items():

    if not isinstance(payloads,list):
        continue

    out.append(f"\n## {group}\n")

    for p in payloads:

        name=p.get("name") or p.get("title") or "unknown"

        out.append(f"\n### {name}\n")

        if p.get("category"):
            out.append(f"分类: `{p['category']}`\n")

        if p.get("description"):
            out.append(p["description"]+"\n")

        steps=p.get("steps") or []

        for s in steps:

            cmds=s.get("commands") or []

            for c in cmds:
                out.append("```bash\n"+c+"\n```\n")

Path("docs/payloads.md").write_text("".join(out))
