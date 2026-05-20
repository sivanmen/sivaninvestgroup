import {
  AbsoluteFill,
  useCurrentFrame,
  useVideoConfig,
  interpolate,
  spring,
} from "remotion";

interface HookProps {
  line1: string;
  line2: string;
}

export const Hook: React.FC<HookProps> = ({ line1, line2 }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const overlayOpacity = interpolate(frame, [0, fps * 0.6], [0, 1], {
    extrapolateRight: "clamp",
  });

  const hookSpring = spring({
    frame,
    fps,
    config: { damping: 14, stiffness: 120, mass: 0.8 },
  });

  const hookTranslateY = interpolate(hookSpring, [0, 1], [60, 0]);

  const line2Delay = spring({
    frame: Math.max(0, frame - fps * 0.4),
    fps,
    config: { damping: 14, stiffness: 120, mass: 0.8 },
  });

  const ctaOpacity = interpolate(frame, [fps * 1.8, fps * 2.5], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const fadeOut = interpolate(frame, [fps * 4.2, fps * 5], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill style={{ opacity: fadeOut }}>
      {/* Greek-blue gradient overlay */}
      <AbsoluteFill
        style={{
          background:
            "linear-gradient(160deg, rgba(13,94,175,0.82) 0%, rgba(0,0,0,0.88) 60%, rgba(13,94,175,0.6) 100%)",
          opacity: overlayOpacity,
        }}
      />

      {/* Decorative Greek pattern lines */}
      <AbsoluteFill style={{ opacity: overlayOpacity * 0.25 }}>
        {[...Array(8)].map((_, i) => (
          <div
            key={i}
            style={{
              position: "absolute",
              top: 0,
              bottom: 0,
              left: `${i * 14}%`,
              width: 2,
              background:
                "linear-gradient(180deg, transparent, rgba(255,255,255,0.4), transparent)",
            }}
          />
        ))}
      </AbsoluteFill>

      {/* Main hook content */}
      <AbsoluteFill
        style={{
          justifyContent: "center",
          alignItems: "center",
          flexDirection: "column",
          gap: 28,
          paddingTop: 80,
        }}
      >
        {/* Warning + Flag */}
        <div
          style={{
            fontSize: 90,
            transform: `scale(${hookSpring}) translateY(${hookTranslateY}px)`,
            opacity: hookSpring,
            filter: "drop-shadow(0 6px 24px rgba(0,0,0,0.6))",
            lineHeight: 1,
          }}
        >
          ⚠️🇬🇷
        </div>

        {/* Line 1 */}
        <div
          style={{
            direction: "rtl",
            textAlign: "center",
            opacity: hookSpring,
            transform: `translateY(${hookTranslateY}px)`,
            paddingLeft: 48,
            paddingRight: 48,
          }}
        >
          <div
            style={{
              fontSize: 76,
              fontWeight: 900,
              color: "white",
              fontFamily: "Heebo, sans-serif",
              lineHeight: 1.25,
              textShadow: "0 4px 24px rgba(0,0,0,0.85)",
              letterSpacing: -1,
            }}
          >
            {line1}
          </div>
        </div>

        {/* Line 2 - gold accent */}
        <div
          style={{
            direction: "rtl",
            textAlign: "center",
            opacity: line2Delay,
            transform: `translateY(${interpolate(line2Delay, [0, 1], [50, 0])}px)`,
            paddingLeft: 40,
            paddingRight: 40,
          }}
        >
          <div
            style={{
              fontSize: 68,
              fontWeight: 800,
              color: "#FFD700",
              fontFamily: "Heebo, sans-serif",
              lineHeight: 1.3,
              textShadow:
                "0 0 40px rgba(255,215,0,0.4), 0 4px 20px rgba(0,0,0,0.8)",
              letterSpacing: -0.5,
            }}
          >
            {line2}
          </div>
        </div>

        {/* CTA */}
        <div
          style={{
            color: "rgba(255,255,255,0.9)",
            fontSize: 40,
            fontFamily: "Heebo, sans-serif",
            fontWeight: 600,
            opacity: ctaOpacity,
            direction: "rtl",
            letterSpacing: 0,
            textShadow: "0 2px 12px rgba(0,0,0,0.8)",
          }}
        >
          👇 המשך לצפייה
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
