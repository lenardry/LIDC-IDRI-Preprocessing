from configparser import ConfigParser

if __name__ == "__main__":
    # This python file creates a configuartion file. Change the below directories for your application

    config = ConfigParser()

    # prepare_dataset.py configuration
    config['prepare_dataset'] = {
        #Path To LIDC Dataset
        'LIDC_DICOM_PATH': '../LIDC-IDRI/manifest-1600709154662/LIDC-IDRI',
        # Directory to save the output files
        # Directory for masks
        'MASK_PATH':'../LIDC-IDRI Preprocessed Exp 3/Mask',
        # Directory for images
        'IMAGE_PATH':'../LIDC-IDRI Preprocessed Exp 3/Image',
        # To save images and mask that doesn't contain any nodule or cancer
        # These images will be used later to evaluate our model
        'CLEAN_PATH_IMAGE':'../LIDC-IDRI Preprocessed Exp 3/Clean/Image',
        'CLEAN_PATH_MASK':'../LIDC-IDRI Preprocessed Exp 3/Clean/Mask',
        # CSV file containing nodule information, malignancy, train test split
        'META_PATH': '../LIDC-IDRI Preprocessed Exp 3/Meta/',
        # Mask Threshold is the np.sum(MASK) threshold. Some Masks are too small. We remove these small images,masks as they might act as outliers
        # The threshold 8 was decided by empirical evaluation.
        'Mask_Threshold':8
    }


    # This is the configuration file for pylidc library
    config['pylidc'] = {
        # Confidence level determines the overlap between the 4 doctors who have made annotation
        'confidence_level': 0.5,
        # 512 determines the size of the image
        'padding_size': 512
    }

    # Create the configuration file in lung.conf
    with open('./lung.conf', 'w') as f:
          config.write(f)
