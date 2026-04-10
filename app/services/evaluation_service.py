from app.core.config import METRICS_PATH
from app.schemas.output_schema import MetricsOutput
import joblib
import os


def load_metrics():
    """
    Charger les métriques sauvegardées
    """
    if not os.path.exists(METRICS_PATH):
        raise FileNotFoundError("metrics.pkl introuvable")

    metrics = joblib.load(METRICS_PATH)

    return MetricsOutput(**metrics)