import fs from "fs"

const db = JSON.parse(
  fs.readFileSync("database/payloads.json","utf8")
)

const index = []

for (const [group,payloads] of Object.entries(db.data)) {

  if (!Array.isArray(payloads)) continue

  for (const p of payloads) {

    index.push({
      name: p.name || p.title || "",
      category: p.category || "",
      tags: p.tags || [],
      group
    })
  }
}

fs.writeFileSync(
  "database/payload_index.json",
  JSON.stringify(index,null,2)
)

console.log("index generated", index.length)
