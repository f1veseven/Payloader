import json
from pathlib import Path

data=json.loads(Path("database/payloads.json").read_text())

db=data["data"]

def to_str(v):
    if v is None:
        return ""
    if isinstance(v,str):
        return v
    if isinstance(v,dict):
        return v.get("zh") or v.get("en") or ""
    return str(v)

out=["# Payloader Payload 手册\n"]

for group,payloads in db.items():

    if not isinstance(payloads,list):
        continue

    out.append(f"\n## {group}\n")

    for p in payloads:

        name=to_str(p.get("name") or p.get("title") or "unknown")

        out.append(f"\n### {name}\n")

        category=to_str(p.get("category"))
        if category:
            out.append(f"分类: `{category}`\n")

        desc=to_str(p.get("description"))
        if desc:
            out.append(desc+"\n")

        steps=p.get("steps") or []

        for s in steps:

            cmds=s.get("commands") or []

            for c in cmds:
                out.append("```bash\n"+c+"\n```\n")

Path("docs/payloads.md").write_text("".join(out))
