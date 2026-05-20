import { useState, useEffect } from "react";
import {
  AbsoluteFill,
  Video,
  staticFile,
  Sequence,
  continueRender,
  delayRender,
  cancelRender,
} from "remotion";
import { Hook } from "./components/Hook";
import { TitleCard } from "./components/TitleCard";
import { Subtitles } from "./components/Subtitles";
import { EndCard } from "./components/EndCard";
import { loadHeebo, HEEBO } from "./fonts";

export interface VideoProps {
  hookLine1: string;
  hookLine2: string;
  showEndCard: boolean;
  durationInFrames: number;
}

const HOOK_DURATION_FRAMES = 150; // 5 seconds

export const GreeceInvestmentVideo: React.FC<VideoProps> = ({
  hookLine1,
  hookLine2,
  showEndCard,
  durationInFrames,
}) => {
  const [handle] = useState(() => delayRender("Loading Heebo font"));

  useEffect(() => {
    loadHeebo()
      .then(() => continueRender(handle))
      .catch((e) => cancelRender(e));
  }, [handle]);

  const endCardStart = durationInFrames - 120; // last 4 seconds

  return (
    <AbsoluteFill
      style={{ backgroundColor: "black", fontFamily: `'${HEEBO}', sans-serif` }}
    >
      {/* Background video */}
      <Video
        src={staticFile("video.mp4")}
        style={{ width: "100%", height: "100%", objectFit: "cover" }}
      />

      {/* Bottom gradient for subtitle readability */}
      <AbsoluteFill
        style={{
          background:
            "linear-gradient(0deg, rgba(0,0,0,0.65) 0%, rgba(0,0,0,0.3) 25%, transparent 50%)",
          pointerEvents: "none",
        }}
      />

      {/* Subtitles — full video */}
      <Subtitles />

      {/* Hook — first 5 seconds, always shown */}
      <Sequence from={0} durationInFrames={HOOK_DURATION_FRAMES}>
        <Hook line1={hookLine1} line2={hookLine2} />
      </Sequence>

      {/* Title card — first 5 seconds */}
      <Sequence from={0} durationInFrames={HOOK_DURATION_FRAMES}>
        <TitleCard />
      </Sequence>

      {/* End card — last 4 seconds, only when requested */}
      {showEndCard && (
        <Sequence from={endCardStart} durationInFrames={120}>
          <EndCard />
        </Sequence>
      )}
    </AbsoluteFill>
  );
};
