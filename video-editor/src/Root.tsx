import "./index.css";
import { Composition } from "remotion";
import { GreeceInvestmentVideo } from "./Composition";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="GreeceInvestment"
        component={GreeceInvestmentVideo}
        durationInFrames={2460}
        fps={30}
        width={1080}
        height={1920}
      />
    </>
  );
};
