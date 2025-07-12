import { Storage } from "@google-cloud/storage";

let storage: Storage;

if (process.env.GCP_KEY_JSON) {
  // ✅ Repara saltos de línea mal codificados en la clave privada
  const raw = JSON.parse(process.env.GCP_KEY_JSON);
  if (raw.private_key && typeof raw.private_key === "string") {
    raw.private_key = raw.private_key.replace(/\\n/g, "\n");
  }

  storage = new Storage({
    credentials: raw,
    projectId: raw.project_id,
  });
} else {
  storage = new Storage({
    keyFilename: process.env.GOOGLE_APPLICATION_CREDENTIALS || "",
  });
}

export { storage };
