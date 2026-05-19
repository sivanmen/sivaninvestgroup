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

const VIDEO_DURATION_FRAMES = 2460; // 82s × 30fps
const HOOK_DURATION_FRAMES = 150;   // 5 seconds
const END_CARD_START = VIDEO_DURATION_FRAMES - 120; // last 4 seconds

export const GreeceInvestmentVideo: React.FC = () => {
  const [handle] = useState(() => delayRender("Loading Heebo font"));

  useEffect(() => {
    loadHeebo()
      .then(() => continueRender(handle))
      .catch((e) => cancelRender(e));
  }, [handle]);

  return (
    <AbsoluteFill
      style={{ backgroundColor: "black", fontFamily: `'${HEEBO}', sans-serif` }}
    >
      {/* Background video - full screen */}
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

      {/* Hebrew subtitles - throughout entire video */}
      <Subtitles />

      {/* Opening hook - first 5 seconds */}
      <Sequence from={0} durationInFrames={HOOK_DURATION_FRAMES}>
        <Hook />
      </Sequence>

      {/* Title card - first 5 seconds */}
      <Sequence from={0} durationInFrames={HOOK_DURATION_FRAMES}>
        <TitleCard />
      </Sequence>

      {/* End card - last 4 seconds */}
      <Sequence from={END_CARD_START} durationInFrames={120}>
        <EndCard />
      </Sequence>
    </AbsoluteFill>
  );
};
