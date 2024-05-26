import os
from frame_extraction import extract_frames
from frame_processing import process_frames
from video_assembly import assemble_video

input_video = "input_sd_video.mp4"
extracted_frames_folder = "extracted_frames"
processed_frames_folder = "processed_frames"
output_video = "output_hd_video.mp4"

# Step 1: Extract frames
fps, frame_count = extract_frames(input_video, extracted_frames_folder)
print(f"Step 1 completed: Extracted {frame_count} frames at {fps} FPS")

# Step 2: Process frames
process_frames(extracted_frames_folder, processed_frames_folder)
print("Step 2 completed: Frame processing completed successfully!")

# Step 3: Assemble video
assemble_video(processed_frames_folder, output_video, fps)
print("Step 3 completed: Video assembly completed successfully!")

print("Video conversion process completed successfully!")
