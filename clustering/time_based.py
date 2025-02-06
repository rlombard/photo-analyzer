import numpy as np
from sklearn.cluster import DBSCAN
from config import TIME_CLUSTERING_EPS, TIME_CLUSTERING_MIN_SAMPLES
from utils.logger import logger

def cluster_images(images):
    """Cluster images based on time proximity."""
    try:
        timestamps = np.array([img['takenAtTimestamp'] for img in images]).reshape(-1, 1)
        dbscan = DBSCAN(eps=TIME_CLUSTERING_EPS, min_samples=TIME_CLUSTERING_MIN_SAMPLES, metric='euclidean')
        labels = dbscan.fit_predict(timestamps)
        
        clusters = {}
        for img, label in zip(images, labels):
            if label not in clusters:
                clusters[label] = []
            clusters[label].append(img)
        
        logger.info(f"✅ Clustered {len(images)} images into {len(set(labels))} clusters.")
        return clusters
    except Exception as e:
        logger.error(f"❌ Error clustering images by time: {e}")
        return {}
