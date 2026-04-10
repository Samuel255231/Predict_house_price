from fastapi import APIRouter, HTTPException
from app.services.evaluation_service import load_metrics

router = APIRouter()

@router.get("/perf", summary="Performance du modèle")
def get_model_performance():
    """
    Retourne les performances du modèle (chargées depuis metrics.pkl)
    """
    try:
        metrics = load_metrics()

        return {
            "r2": round(metrics.get("r2", 0), 4),
            "mse": round(metrics.get("mse", 0), 4),
            "rmse": round(metrics.get("rmse", 0), 4),
            "mae": round(metrics.get("mae", 0), 4)
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))