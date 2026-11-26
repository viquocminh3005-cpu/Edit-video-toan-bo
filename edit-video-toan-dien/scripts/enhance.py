#!/usr/bin/env python3
"""enhance — đưa âm lượng giọng nói về chuẩn cho video ĐÃ CẮT (chạy trước bước phủ chữ).
Hình giữ nguyên (copy, không encode lại). KHÔNG khử ồn, KHÔNG làm đẹp hình (chủ kênh chốt).

  python enhance.py <cut.mp4> -o <cut_enh.mp4> [--lufs -14]

• loudnorm về --lufs (mặc định -14 LUFS: chuẩn TikTok / YouTube / Facebook), LRA 7 (đoạn nhỏ nâng lên,
  đoạn to hạ xuống → không quá to, không quá nhỏ), đỉnh tối đa -1.5 dBTP (không rè).
"""
import argparse
import subprocess
import sys


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video"); ap.add_argument("-o", "--out", required=True)
    ap.add_argument("--lufs", type=float, default=-14, help="độ lớn chuẩn (LUFS)")
    a = ap.parse_args()
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", a.video, "-map", "0:v", "-map", "0:a", "-c:v", "copy",
                    "-af", f"loudnorm=I={a.lufs}:LRA=7:TP=-1.5,aresample=48000",
                    "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", a.out], check=True)
    print(f"Xong → {a.out}  (âm lượng chuẩn {a.lufs} LUFS)")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
