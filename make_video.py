import argparse
from pathlib import Path

import cv2


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_dir", type=str, default="out_reconstructed")
    parser.add_argument("--output", type=str, default="reconstructed.mp4")
    parser.add_argument("--fps", type=int, default=24)
    args = parser.parse_args()

    # Sort by filename so frames stay in order (frame_00001, frame_00002, ...)
    paths = sorted(Path(args.input_dir).glob("*.png"))
    if not paths:
        raise RuntimeError(f"No .png files found in {args.input_dir}")

    # Use the first frame to get the video size
    first = cv2.imread(str(paths[0]))
    height, width = first.shape[:2]

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    writer = cv2.VideoWriter(args.output, fourcc, args.fps, (width, height))

    for p in paths:
        frame = cv2.imread(str(p))
        if frame is None:
            print(f"Skipping unreadable file: {p}")
            continue
        if frame.shape[:2] != (height, width):
            frame = cv2.resize(frame, (width, height))
        writer.write(frame)

    writer.release()
    print(f"Wrote {len(paths)} frames to {args.output} at {args.fps} fps")


if __name__ == "__main__":
    main()
