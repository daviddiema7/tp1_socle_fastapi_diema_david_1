from app.core.settings import Settings


def test_should_use_default_path_when_env_var_is_not_set(monkeypatch):
    monkeypatch.delenv("USERS_JSON_PATH", raising=False)  # On s'assure que la variable d'environnement n'est pas définie
    settings = Settings()
    assert settings.users_json_path == "data/users.json"  # On vérifie que le chemin par défaut est utilisé

def test_should_use_env_var_path_when_defined(monkeypatch):
    
    monkeypatch.setenv("USERS_JSON_PATH", "custom/users.json")  # On définit une variable d'environnement de test
    settings = Settings()
    assert settings.users_json_path == "custom/users.json"  # On vérifie que le chemin défini dans l'environnement est utilisé