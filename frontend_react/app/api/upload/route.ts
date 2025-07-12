import { NextRequest, NextResponse } from "next/server";
import { v4 as uuidv4 } from "uuid";
import { storage } from "@/lib/gcs";

export async function POST(req: NextRequest) {
  try {
    const formData = await req.formData();
    const file = formData.get("file") as File;

    if (!file) {
      return NextResponse.json({ error: "No file provided" }, { status: 400 });
    }

    const arrayBuffer = await file.arrayBuffer();
    const buffer = Buffer.from(arrayBuffer);
    const fileName = `${uuidv4()}_${file.name}`;

    const bucket = storage.bucket("hitalyzer-audio-files");
    const blob = bucket.file(fileName);

    await blob.save(buffer, {
      contentType: file.type || "audio/wav",
      // ❌ No se puede usar `public: true` si tienes uniform bucket-level access
    });

    const publicUrl = `https://storage.googleapis.com/hitalyzer-audio-files/${fileName}`;

    return NextResponse.json({ fileName, publicUrl });
  } catch (err) {
    console.error("❌ Upload error:", err);
    return NextResponse.json({ error: "Upload failed" }, { status: 500 });
  }
}
