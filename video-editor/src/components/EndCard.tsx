import {
  AbsoluteFill,
  useCurrentFrame,
  useVideoConfig,
  interpolate,
  spring,
} from "remotion";

export const EndCard: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const appear = spring({
    frame,
    fps,
    config: { damping: 16, stiffness: 100 },
  });

  const opacity = interpolate(frame, [0, fps * 0.5], [0, 1], {
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill style={{ opacity }}>
      <AbsoluteFill
        style={{
          background:
            "linear-gradient(0deg, rgba(0,0,0,0.92) 0%, rgba(13,94,175,0.85) 50%, transparent 100%)",
          justifyContent: "flex-end",
          alignItems: "center",
          paddingBottom: 120,
          paddingLeft: 40,
          paddingRight: 40,
          flexDirection: "column",
          gap: 24,
        }}
      >
        <div
          style={{
            transform: `scale(${appear}) translateY(${interpolate(appear, [0, 1], [40, 0])}px)`,
            textAlign: "center",
            direction: "rtl",
          }}
        >
          <div
            style={{
              fontSize: 56,
              fontWeight: 900,
              color: "#FFD700",
              fontFamily: "Heebo, sans-serif",
              textShadow: "0 4px 20px rgba(0,0,0,0.8)",
              lineHeight: 1.3,
              letterSpacing: -1,
            }}
          >
            רוצה לדעת עוד?
          </div>
          <div
            style={{
              fontSize: 44,
              fontWeight: 700,
              color: "white",
              fontFamily: "Heebo, sans-serif",
              textShadow: "0 3px 16px rgba(0,0,0,0.8)",
              marginTop: 12,
              lineHeight: 1.4,
            }}
          >
            עקוב לסרטונים נוספים{"\n"}על השקעות ביוון 🇬🇷
          </div>
        </div>

        {/* Follow button style */}
        <div
          style={{
            transform: `scale(${appear})`,
            background: "#0D5EAF",
            borderRadius: 50,
            paddingTop: 18,
            paddingBottom: 18,
            paddingLeft: 48,
            paddingRight: 48,
            border: "3px solid white",
            fontSize: 40,
            fontWeight: 800,
            color: "white",
            fontFamily: "Heebo, sans-serif",
            direction: "rtl",
            letterSpacing: -0.5,
          }}
        >
          👆 עקוב עכשיו
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
