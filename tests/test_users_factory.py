import json
import pytest
from pathlib import Path
from pydantic import ValidationError

from app.factories.user_factory import UsersFactory
from app.models.user_model import UserModel

# --- TEST 1 : Le cas parfait ---
def test_should_return_list_of_user_models_given_valid_json(tmp_path: Path):
    # 1. ARRANGE (Given) : On prépare le terrain
    # On crée un faux fichier JSON temporaire
    file_path = tmp_path / "valid_users.json"
    file_path.write_text(json.dumps({
        "users": [
            {"id": 1, "login": "alice", "age": 25},
            {"id": 2, "login": "bob", "age": 30}
        ]
    }), encoding="utf-8")
    
    factory = UsersFactory()

    # 2. ACT (When) : On lance l'action
    result = factory.create_users(str(file_path))

    # 3. ASSERT (Then) : On vérifie le résultat
    assert len(result) == 2  # On a bien 2 utilisateurs
    assert isinstance(result[0], UserModel)  # Ce sont bien des objets UserModel
    assert result[0].login == "alice"  # Les données sont correctes


# --- TEST 2 : La clé "users" n'existe pas ---
def test_should_raise_value_error_given_json_without_users_key(tmp_path: Path):
    # 1. ARRANGE
    file_path = tmp_path / "missing_key.json"
    file_path.write_text(json.dumps({
        "employes": []  # Oups, pas de clé "users" !
    }), encoding="utf-8")
    
    factory = UsersFactory()

    # 2 & 3. ACT & ASSERT : On vérifie que la Factory lève bien l'erreur prévue
    with pytest.raises(ValueError, match="no users found"):
        factory.create_users(str(file_path))


# --- TEST 3 : Les données sont fausses (Pydantic entre en jeu) ---
def test_should_raise_validation_error_given_invalid_user_data(tmp_path: Path):
    # 1. ARRANGE
    file_path = tmp_path / "invalid_data.json"
    file_path.write_text(json.dumps({
        "users": [
            {"id": 1, "login": "al", "age": -5} # Erreur: login trop court ET âge négatif !
        ]
    }), encoding="utf-8")
    
    factory = UsersFactory()

    # 2 & 3. ACT & ASSERT : Pydantic doit lever une ValidationError
    with pytest.raises(ValidationError):
        factory.create_users(str(file_path))