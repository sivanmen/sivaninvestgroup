#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────
# Sivan Invest — Video Render Pipeline
# ─────────────────────────────────────────────────────────────
# Usage:
#   ./scripts/render.sh --input <video.mp4> [options]
#
# Options:
#   --input       <path>   Source video file (required)
#   --hook-line1  "text"   First hook line  (default: "")
#   --hook-line2  "text"   Second hook line (default: "")
#   --end-card             Add end card at the last 4 seconds
#   --output      <path>   Output file      (default: output_final.mp4)
#
# Examples:
#   # Basic — hook only, no end card
#   ./scripts/render.sh --input raw.mp4 \
#     --hook-line1 "לפני שאתה משקיע ביוון" \
#     --hook-line2 "5 הטעויות שחייבים לדעת"
#
#   # With end card
#   ./scripts/render.sh --input raw.mp4 \
#     --hook-line1 "3 סיבות להשקיע בסלוניקי" \
#     --hook-line2 "שכולם מפספסים" \
#     --end-card \
#     --output saloniki_final.mp4
# ─────────────────────────────────────────────────────────────
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
RNNOISE_MODEL="$PROJECT_DIR/scripts/bd.rnnn"
RNNOISE_URL="https://github.com/GregorR/rnnoise-models/raw/master/beguiling-drafter-2018-08-30/bd.rnnn"

# ── defaults ──────────────────────────────────────────────────
INPUT=""
HOOK_LINE1=""
HOOK_LINE2=""
SHOW_END_CARD="false"
OUTPUT="output_final.mp4"

# ── parse args ────────────────────────────────────────────────
while [[ $# -gt 0 ]]; do
  case "$1" in
    --input)       INPUT="$2";       shift 2 ;;
    --hook-line1)  HOOK_LINE1="$2";  shift 2 ;;
    --hook-line2)  HOOK_LINE2="$2";  shift 2 ;;
    --end-card)    SHOW_END_CARD="true"; shift ;;
    --output)      OUTPUT="$2";      shift 2 ;;
    *) echo "Unknown option: $1"; exit 1 ;;
  esac
done

if [[ -z "$INPUT" ]]; then
  echo "Error: --input is required"
  exit 1
fi

if [[ ! -f "$INPUT" ]]; then
  echo "Error: file not found: $INPUT"
  exit 1
fi

echo "═══════════════════════════════════════════════"
echo "  Sivan Invest Video Pipeline"
echo "  Input:    $INPUT"
echo "  Hook 1:   $HOOK_LINE1"
echo "  Hook 2:   $HOOK_LINE2"
echo "  End card: $SHOW_END_CARD"
echo "  Output:   $OUTPUT"
echo "═══════════════════════════════════════════════"

# ── step 1: copy source video ─────────────────────────────────
echo "[1/4] Preparing source video..."
cp "$INPUT" "$PROJECT_DIR/public/video.mp4"

# ── step 2: detect video duration in frames ───────────────────
echo "[2/4] Detecting video duration..."
DURATION_SEC=$(ffprobe -v error -show_entries format=duration \
  -of default=noprint_wrappers=1:nokey=1 "$INPUT")
FPS=30
DURATION_FRAMES=$(python3 -c "import math; print(math.ceil(float('$DURATION_SEC') * $FPS))")
echo "      Duration: ${DURATION_SEC}s → ${DURATION_FRAMES} frames"

# ── step 3: render with Remotion ──────────────────────────────
echo "[3/4] Rendering with Remotion (hook + visual overlays)..."
RAW_OUTPUT="$PROJECT_DIR/output_raw.mp4"

PROPS=$(python3 -c "
import json
print(json.dumps({
  'hookLine1': '$HOOK_LINE1',
  'hookLine2': '$HOOK_LINE2',
  'showEndCard': $SHOW_END_CARD,
  'durationInFrames': $DURATION_FRAMES,
}))
")

cd "$PROJECT_DIR"
npx remotion render SivanInvestVideo "$RAW_OUTPUT" \
  --props="$PROPS" \
  --log=warn

# ── step 4: noise reduction with ffmpeg ───────────────────────
echo "[4/4] Applying noise reduction (arnndn mix=0.5 + highpass 80Hz)..."

# download RNNoise model if missing
if [[ ! -f "$RNNOISE_MODEL" ]]; then
  echo "      Downloading RNNoise model..."
  curl -fsSL "$RNNOISE_URL" -o "$RNNOISE_MODEL"
fi

ffmpeg -y -i "$RAW_OUTPUT" \
  -af "highpass=f=80,arnndn=m=${RNNOISE_MODEL}:mix=0.5" \
  -c:v copy \
  -c:a aac -b:a 192k \
  "$OUTPUT" 2>/dev/null

rm -f "$RAW_OUTPUT"

echo "═══════════════════════════════════════════════"
echo "  Done! → $OUTPUT"
echo "═══════════════════════════════════════════════"
