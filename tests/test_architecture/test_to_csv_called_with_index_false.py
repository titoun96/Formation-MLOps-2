"""Architecture test.

Vérifie que tous les appels à `to_csv` faits dans le package
`formation_mlops_2` sont bien appelés avec l'argument `index=False`.

Cela évite d'écrire l'index du DataFrame dans les fichiers CSV générés
(données, prédictions, etc.).
"""

import ast
from pathlib import Path

PACKAGE_ROOT = Path(__file__).parents[2] / "formation_mlops_2"


def test_to_csv_called_with_index_false():
    # Given
    python_files = PACKAGE_ROOT.rglob("*.py")

    for file in python_files:
        tree = ast.parse(file.read_text(encoding="utf-8"))

        # When
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue

            if not isinstance(node.func, ast.Attribute):
                continue

            if node.func.attr != "to_csv":
                continue

            # Then
            assert any(
                keyword.arg == "index"
                and isinstance(keyword.value, ast.Constant)
                and keyword.value.value is False
                for keyword in node.keywords
            ), (
                f"{file}:{node.lineno} - "
                "L'appel à to_csv doit spécifier index=False"
            )