import cv2
import numpy as np
import pandas as pd
from scipy.stats import kurtosis, skew

def extract_features(image_path):
    names = ['mean_r', 'mean_g', 'mean_b', 'stddev_r', 'stddev_g', 'stddev_b', 
             'variance', 'stddv_h', 'stddv_s', 'stddv_v', 'kurtosis', 'skewness']
    df = pd.DataFrame([], columns=names)
    
    main_img = cv2.imread(image_path)
    img = cv2.cvtColor(main_img, cv2.COLOR_BGR2RGB)
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    red_channel = img[:, :, 0]
    green_channel = img[:, :, 1]
    blue_channel = img[:, :, 2]
    
    h_channel = hsv_img[:, :, 0]
    s_channel = hsv_img[:, :, 1]
    v_channel = hsv_img[:, :, 2]
    
    red_mean = np.mean(red_channel)
    green_mean = np.mean(green_channel)
    blue_mean = np.mean(blue_channel)
    
    red_std = np.std(red_channel)
    green_std = np.std(green_channel)
    blue_std = np.std(blue_channel)
    
    h_std = np.std(h_channel)
    s_std = np.std(s_channel)
    v_std = np.std(v_channel)
    
    kur = kurtosis(img, axis=None)
    sk = skew(img, axis=None)
    var = np.var(img, axis=None)
    
    vector = [red_mean, green_mean, blue_mean, red_std, green_std, blue_std, var, 
              h_std, s_std, v_std, kur, sk]
    df_temp = pd.DataFrame([vector], columns=names)
    df = df.append(df_temp, ignore_index=True)
    
    return df

def normalize_features(df, train_stats):
    return (df - train_stats['mean']) / train_stats['std']

# Predict chlorophyll value from an image
def predict_chlorophyll(image_path, model, train_stats):
    features = extract_features(image_path)
    normed_features = normalize_features(features, train_stats)
    prediction = model.predict(normed_features).flatten()
    return prediction
