import cv2
import os

def extract_frames(video_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(video_path)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    frame_number = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imwrite(f"{output_folder}/frame_{frame_number:05d}.png", frame)
        frame_number += 1

    cap.release()
    return fps, frame_count

if __name__ == "__main__":
    input_video = "input_sd_video.mp4"
    output_folder = "extracted_frames"
    fps, frame_count = extract_frames(input_video, output_folder)
    print(f"Extracted {frame_count} frames at {fps} FPS")
