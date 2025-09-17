

# DICT_FIELD_REDACTER

## 🇫🇷 Français

### Description
DICT_FIELD_REDACTER est un outil Python permettant de masquer ou supprimer des champs sensibles dans des dictionnaires ou des objets JSON. Idéal pour anonymiser des données avant de les stocker ou de les partager.

### Installation
```bash
pip install dict-field-redacter
```

### Utilisation
```python
test_data = {
    "user_profile": {
        "username": "john_doe",
        "email": "john@example.com",
        "personal_info": {
            "ssn": "123-45-6789",
            "password": "mySecretPass123",
            "banking": {
                "account_number": "ACC123456789",
                "secret": "bank_secret_key",
                "credit_card": {
                    "number": "4532-1234-5678-9012",
                    "cvv": "123",
                    "pin": "1234"
                }
            }
        }
    },
}
from dict_field_redacter import DictFieldRedacter
import json
fields_to_redact = ["email", "password", "secret", "cvv", "pin", "number"]
redacter = DictFieldRedacter(fields_to_redact, maskWith="Redacted") # Vous pouvez personnaliser le placeholder avec une valeur de votre choix
# La redaction en mode strict (seuls les champs spécifiés sont redacted, (ceux qui ne sont pas strictement dans la liste restent inchangés))
redacted = redacter.sanitize(test_data, mode="loose")
print(json.dumps(redacted, indent=4))
#{
#    "user_profile": {
#        "username": "john_doe",
#        "email": "Redacted",
#        "personal_info": {
#            "ssn": "123-45-6789",
#            "password": "Redacted",
#            "banking": {
#                "account_number": "Redacted",
#                "secret": "Redacted",
#                "credit_card": {
#                    "number": "4532-1234-5678-9012",
#                    "cvv": "123",
#                    "pin": "1234"
#                }
#            }
#        }
#    },
#}
```

### Contribution
Les contributions sont les bienvenues ! Veuillez ouvrir une issue ou une pull request sur GitHub.

### Licence
Ce projet est sous licence MIT.

---
## 🇬🇧 English
### Description
DICT_FIELD_REDACTER is a Python tool that allows you to mask or remove sensitive fields in dictionaries or JSON objects. Ideal for anonymizing data before storing or sharing it.
### Installation
```bash
pip install dict-field-redacter
```
### Usage
```python
test_data = {
    "user_profile": {
        "username": "john_doe",
        "email": "john@example.com",
        "personal_info": {
            "ssn": "123-45-6789",
            "password": "mySecretPass123",
            "banking": {
                "account_number": "ACC123456789",
                "secret": "bank_secret_key",
                "credit_card": {
                    "number": "4532-1234-5678-9012",
                    "cvv": "123",
                    "pin": "1234"
                }
            }
        }
    },
}
from dict_field_redacter import DictFieldRedacter
import json
fields_to_redact = ["email", "password", "secret", "cvv", "pin", "number"]
redacter = DictFieldRedacter(fields_to_redact, placeHolder="Redacted") # You can customize the placeholder
# 
redacted = redacter.sanitize(test_data, mode="loose")
print(json.dumps(redacted, indent=4))
#{
#    "user_profile": {
#        "username": "john_doe",
#        "email": "Redacted",
#        "personal_info": {
#            "ssn": "123-45-6789",
#            "password": "Redacted",
#            "banking": {
#                "account_number": "Redacted",
#                "secret": "Redacted",
#                "credit_card": {
#                    "number": "4532-1234-5678-9012",
#                    "cvv": "123",
#                    "pin": "1234"
#                }
#            }
#        }
#    },
#}
```

### Contribution
Contributions are welcome! Please open an issue or a pull request on GitHub.

### Licence
This project is licensed under the MIT License.
