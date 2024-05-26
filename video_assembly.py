import cv2
import os

def assemble_video(frames_folder, output_path, fps):
    frame_files = sorted([os.path.join(frames_folder, f) for f in os.listdir(frames_folder) if f.endswith('.png')])
    
    frame_example = cv2.imread(frame_files[0])
    height, width, layers = frame_example.shape
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    for frame_file in frame_files:
        frame = cv2.imread(frame_file)
        video.write(frame)

    video.release()

if __name__ == "__main__":
    frames_folder = "processed_frames"
    output_video = "output_hd_video.mp4"
    fps = 30
    assemble_video(frames_folder, output_video, fps)
    print("Video assembly completed successfully!")
