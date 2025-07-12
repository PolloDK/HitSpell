import { Storage } from "@google-cloud/storage";
import path from "path";

const credentialsPath = process.env.GOOGLE_APPLICATION_CREDENTIALS
  ? path.resolve(process.cwd(), process.env.GOOGLE_APPLICATION_CREDENTIALS)
  : "";

export const storage = new Storage({
  projectId: "hitalyzer-feature-extraction",
  keyFilename: credentialsPath,
});
