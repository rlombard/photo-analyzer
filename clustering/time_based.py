import numpy as np
import datetime
from sklearn.cluster import DBSCAN
from utils.logger import logger

def cluster_images(images):
    """
    Cluster images by time using DBSCAN.

    Groups images taken within a day (`eps=86400` seconds) into the same cluster.
    """
    try:
        timestamps = np.array([
            datetime.datetime.strptime(img["takenAt"], "%Y-%m-%dT%H:%M:%S.%fZ").timestamp()
            for img in images
        ]).reshape(-1, 1)

        # Use DBSCAN to detect time-based clusters
        clustering = DBSCAN(eps=86400, min_samples=3).fit(timestamps)  # 1-day separation

        clusters = {}
        for img, label in zip(images, clustering.labels_):
            if label != -1:
                if label not in clusters:
                    clusters[label] = []
                clusters[label].append(img)

        logger.info(f"⏳ Found {len(clusters)} time-based clusters.")
        for cluster_id, cluster_images in clusters.items():
            logger.info(f"  - Cluster {cluster_id}: {len(cluster_images)} images")

        return clusters

    except Exception as e:
        logger.error(f"❌ Error clustering images by time: {e}")
        return {}
