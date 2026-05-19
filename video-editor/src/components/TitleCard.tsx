import { useCurrentFrame, useVideoConfig, interpolate } from "remotion";

export const TitleCard: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const slideIn = interpolate(frame, [0, fps * 0.6], [-140, 0], {
    extrapolateRight: "clamp",
    easing: (t: number) => 1 - Math.pow(1 - t, 3),
  });

  const opacity = interpolate(frame, [0, fps * 0.4], [0, 1], {
    extrapolateRight: "clamp",
  });

  const fadeOut = interpolate(frame, [fps * 4.2, fps * 5], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <div
      style={{
        position: "absolute",
        top: 0,
        left: 0,
        right: 0,
        transform: `translateY(${slideIn}px)`,
        opacity: opacity * fadeOut,
        background:
          "linear-gradient(180deg, rgba(0,0,0,0.85) 0%, rgba(13,94,175,0.7) 60%, transparent 100%)",
        paddingTop: 60,
        paddingBottom: 100,
        paddingLeft: 36,
        paddingRight: 36,
        direction: "rtl",
      }}
    >
      {/* Channel badge */}
      <div
        style={{
          display: "inline-flex",
          alignItems: "center",
          gap: 12,
          background: "rgba(13,94,175,0.9)",
          borderRadius: 40,
          paddingTop: 10,
          paddingBottom: 10,
          paddingLeft: 24,
          paddingRight: 24,
          border: "2px solid rgba(255,255,255,0.4)",
          marginBottom: 16,
        }}
      >
        <span style={{ fontSize: 36 }}>🇬🇷</span>
        <span
          style={{
            fontSize: 32,
            fontWeight: 700,
            color: "white",
            fontFamily: "Heebo, sans-serif",
            letterSpacing: -0.3,
          }}
        >
          Sivan Invest
        </span>
      </div>

      {/* Main title */}
      <div
        style={{
          fontSize: 52,
          fontWeight: 900,
          color: "white",
          fontFamily: "Heebo, sans-serif",
          lineHeight: 1.2,
          textShadow: "0 3px 16px rgba(0,0,0,0.8)",
          letterSpacing: -1,
        }}
      >
        5 טעויות של משקיע ראשון ביוון
      </div>
    </div>
  );
};
