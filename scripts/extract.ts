import fs from "fs"
import path from "path"

const DATA_DIR = "./_src/src/data"

function collect(mod:any){
  if(Array.isArray(mod)) return mod

  const arr:any[]=[]

  for(const v of Object.values(mod)){
    if(Array.isArray(v)) arr.push(...v)
  }

  return arr
}

async function main(){

  const files=fs.readdirSync(DATA_DIR)

  const database:any={}

  for(const file of files){

    if(!file.endsWith(".ts")) continue

    const mod=await import(path.resolve(DATA_DIR,file))

    const name=file.replace(".ts","")

    database[name]=collect(mod)
  }

  const result={
    meta:{
      source:"3516634930/Payloader",
      generated:new Date().toISOString()
    },
    data:database
  }

  fs.mkdirSync("database",{recursive:true})

  fs.writeFileSync(
    "database/payloads.json",
    JSON.stringify(result,null,2)
  )

  console.log("payload database generated")
}

main()
