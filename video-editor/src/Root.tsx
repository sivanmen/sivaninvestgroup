import "./index.css";
import { Composition } from "remotion";
import { GreeceInvestmentVideo, type VideoProps } from "./Composition";

export const RemotionRoot: React.FC = () => {
  return (
    <Composition
      id="SivanInvestVideo"
      component={GreeceInvestmentVideo}
      fps={30}
      width={1080}
      height={1920}
      defaultProps={{
        hookLine1: "לפני שאתה משקיע ביוון",
        hookLine2: "5 הטעויות שחייבים לדעת",
        showEndCard: false,
        durationInFrames: 2460,
      } satisfies VideoProps}
      calculateMetadata={async ({ props }) => ({
        durationInFrames: props.durationInFrames,
      })}
    />
  );
};
