# Tennis-Machine-Project
### Introduction
This project analyzes Tennis players in a video to measure their speed, ball shot speed and number of shots. This project will detect players and the tennis ball using YOLO and also utilizes CNNs to extract court keypoints. This hands on project is perfect for polishing your machine learning, and computer vision skills.
Big thanks to (https://github.com/abdullahtarek/tennis_analysis) who was the original tutorial creator

###Output Videos:

![output_video(2)](https://github.com/user-attachments/assets/e60422f8-e8bc-4721-afb1-24e60c8d5ea6)

### Models Used

I've removed most of the models due GitHub space limits, you will need to go through and get the data sources and train these models yourself, I recommend using google collab if you do not have access to a gpu

    YOLO v8 for player detection

    Fine Tuned YOLO for tennis ball detection

    Court Key point extraction

    Trained YOLOV5 model: https://drive.google.com/file/d/1UZwiG1jkWgce9lNhxJ2L0NVjX1vGM05U/view?usp=sharing

    Trained tennis court key point model: https://drive.google.com/file/d/1QrTOF1ToQ4plsSZbkBs3zOLkVt3MBlta/view?usp=sharing

### Training

    Tennis ball detetcor with YOLO: training/tennis_ball_detector_training.ipynb
    Tennis court keypoint with Pytorch: training/tennis_court_keypoints_training.ipynb

### Requirements

    python3.8
    ultralytics
    pytroch
    pandas
    numpy
    opencv

