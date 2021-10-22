# DeepGlobe

## Description

This repository contains the my own implementation of DeepGlobe Road Extraction Challenge. The model is trained based on Autoencoder. The original dataset is split into training, validation and testing dataset. 'meta_data.csv' contains image names of satellite and mask image pairs, which can be generate from 'split_dataset.py'.

## Autoencoder structure
![GitHub Logo](/nn.png)

The encoder has three convolutional layers with different sizes. The number of maps in each layer is 32, 64 and 128 respectively. Similar to decoder, the number of maps in each transpose convolutional layer is 64, 32 and 1 respectively. The output of the last layer has a shape of (128, 128, 1), which is the same as the shape of the resized mask image.

## How to run
- Unzip the dataset under the root folder
- Run through every cell in 'main.ipynb'
- No need to run 'split_dataset.py' if 'meta_data.csv' exists

## Issues
Based on the configuration of my device, it is really hard to train a large network in an effcient time. Going through all 3 epoches can take 45 minutes on my device. Also I tried running my code in Colab using GPU, but it took much longer time in reading satellite images using 'cv2.imread()'. 
