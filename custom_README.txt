1. gt lines all: each row describes x1, x2, y1, y2, image width, image height
2. gt_pri_lines_for_test: priary gt lines are denoted as 1, otherwise 0.


Inference on pre-trained model
1. Inference images have to be in .jpg (Change to .jpg from .png from data/image_ops/changeFileExtension.py)
2. Put images in data/agriNav_data
3. Run saveFilenameList.py from data/image_ops to obtain txt file with all filenames
4. Move agriNav_test_idx.txt to data/
5. In config.yml, verify that TEST_DIR and TEST_LABEL_FILE are correct
6. Change utils.py line 86 specify image directory for inference
7. Run python forward.py --model ./result/reproduce/dht_r50_nkl_d97b97138.pth --tmp ./result/segmentationMask_inference/


Generate training data
1. 
