import { useCurrentFrame, useVideoConfig } from "remotion";
import type { TikTokPage } from "@remotion/captions";

const HIGHLIGHT_COLOR = "#FFD700";
const TEXT_COLOR = "white";

export const CaptionPage: React.FC<{ page: TikTokPage }> = ({ page }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const currentTimeMs = (frame / fps) * 1000;
  const absoluteTimeMs = page.startMs + currentTimeMs;

  return (
    <div
      style={{
        position: "absolute",
        bottom: 320,
        left: 24,
        right: 24,
        direction: "rtl",
        textAlign: "right",
        padding: "18px 24px",
        background: "rgba(0,0,0,0.55)",
        borderRadius: 18,
        borderRight: "5px solid #0D5EAF",
      }}
    >
      <div
        style={{
          fontSize: 58,
          fontWeight: 800,
          fontFamily: "Heebo, sans-serif",
          whiteSpace: "pre-wrap",
          lineHeight: 1.35,
          letterSpacing: -0.5,
        }}
      >
        {page.tokens.map((token) => {
          const isActive =
            token.fromMs <= absoluteTimeMs && token.toMs > absoluteTimeMs;
          return (
            <span
              key={token.fromMs}
              style={{
                color: isActive ? HIGHLIGHT_COLOR : TEXT_COLOR,
                textShadow: isActive
                  ? "0 0 20px rgba(255,215,0,0.6)"
                  : "2px 2px 8px rgba(0,0,0,0.9)",
                transition: "none",
              }}
            >
              {token.text}
            </span>
          );
        })}
      </div>
    </div>
  );
};
