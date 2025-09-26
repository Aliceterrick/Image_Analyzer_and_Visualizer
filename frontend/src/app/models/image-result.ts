import { Detection } from "./detection";

export interface CloudResult {
  instances: Detection[];
  concepts: Detection[];
}

export interface ImageResult {
  image: string;
  local: Detection[];
  cloud: CloudResult;
}