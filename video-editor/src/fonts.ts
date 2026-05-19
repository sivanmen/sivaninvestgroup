import { loadFont } from "@remotion/fonts";
import { staticFile } from "remotion";

const family = "Heebo";

export const loadHeebo = () =>
  Promise.all([
    loadFont({ family, url: staticFile("fonts/Heebo-Regular.woff2"), weight: "400" }),
    loadFont({ family, url: staticFile("fonts/Heebo-Bold.woff2"), weight: "700" }),
    loadFont({ family, url: staticFile("fonts/Heebo-ExtraBold.woff2"), weight: "800" }),
    loadFont({ family, url: staticFile("fonts/Heebo-Black.woff2"), weight: "900" }),
  ]);

export const HEEBO = family;
