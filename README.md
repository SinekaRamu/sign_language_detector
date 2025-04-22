# sign-language-detector-python

Sign language detector with Python, OpenCV and Mediapipe !

1. `collect_imgs.py` used to collect the images from A to Z. For each alphabet 100 images have been taken. These images are stored in the data folder.
2. `create_dataset.py` creates the dataset form the collected images. This creates the file named `data.pickle`
3. `train_classifier.py` will train the model and creates the file `model.p`
4. `inference_classifier.py` interfaces with trained model, here camera window will opened to test the alphabets.

Testing to now how it works,
1. `my_camera.py` checks your system camera
2. `collect_single_image.py` will collect 100 images for single alphabet like A or L.
3. `my_dataset.py` sample for how the dataset are create with 3 figures.



