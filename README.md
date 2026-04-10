predict_price_house/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── routes/
│   │   │   │   ├── predict.py        # Endpoint /predict
│   │   │   │   ├── history.py        # Endpoint /history (pagination, filtre…)
│   │   │   │   ├── perf.py           # Endpoint /perf (performance modèle)
│   │   │   │   └── router.py         # Regroupe toutes les routes
│   │   │
│   │   ├── core/
│   │   │   ├── database.py          # Connexion PostgreSQL
│   │   │   └── config.py            # Variables globales (ex: FEATURE_ORDER)
│   │   │
│   │   ├── models/
│   │   │   └── prediction_model.py  # Modèle SQLAlchemy (table predictions)
│   │   │
│   │   ├── schemas/
│   │   │   ├── input_schema.py      # Features (Pydantic)
│   │   │   └── output_schema.py     # Réponses API
│   │   │
│   │   ├── services/
│   │   │   ├── prediction_service.py  # Logique prédiction
│   │   │   ├── history_service.py     # Logique historique (pagination, filtre)
│   │   │   └── evaluation_service.py  # Calcul des métriques
│   │   │
│   │   └── main.py                  # Point d'entrée FastAPI
│   │
│   ├── data/
│   │   ├── X_test.csv
│   │   └── y_test.csv
│   │
│   ├── ml_models/
│   │   └── best_model_XGboost.pkl   # Ton modèle entraîné
│   │
│   ├── requirements.txt
│   └── README.md
│
├── frontend/
│   └── (React app)
│
└── README.md