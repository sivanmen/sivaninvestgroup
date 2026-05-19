import path from "path";
import { fileURLToPath } from "url";
import {
  downloadWhisperModel,
  installWhisperCpp,
  transcribe,
  toCaptions,
} from "@remotion/install-whisper-cpp";
import fs from "fs";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const cwd = path.join(__dirname, "..");

const to = path.join(cwd, "whisper.cpp");
const inputPath = path.join(cwd, "audio.wav");
const outputPath = path.join(cwd, "public", "captions.json");

console.log("Installing Whisper.cpp...");
await installWhisperCpp({ to, version: "1.5.5" });

console.log("Downloading multilingual medium model (supports Hebrew)...");
await downloadWhisperModel({ model: "medium", folder: to });

console.log("Transcribing audio...");
const whisperCppOutput = await transcribe({
  model: "medium",
  whisperPath: to,
  whisperCppVersion: "1.5.5",
  inputPath,
  tokenLevelTimestamps: true,
  language: "he",
});

const { captions } = toCaptions({ whisperCppOutput });
fs.writeFileSync(outputPath, JSON.stringify(captions, null, 2));
console.log(`Captions saved to ${outputPath} (${captions.length} entries)`);
