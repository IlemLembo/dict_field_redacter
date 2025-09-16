""" 
# Example usage
from models import DictFieldRedacter

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
    "application_settings": {
        "api_keys": {
            "primary_key": "pk_live_abcd1234efgh5678",
            "secret_key": "sk_live_xyz789abc456",
            "webhook_secret": "whsec_test123456"
        },
        "database": {
            "connection_string": "mongodb://user:password@localhost:27017",
            "admin_password": "admin123",
            "backup_settings": {
                "encryption_key": "encrypt_key_12345",
                "signature": "backup_signature_hash"
            }
        }
    },
    "third_party_integrations": {
        "payment_gateway": {
            "merchant_id": "MERCH123",
            "secret_token": "token_abcd1234",
            "signature": "payment_signature"
        },
        "social_media": {
            "facebook": {
                "app_secret": "fb_secret_key_123",
                "access_token": "fb_token_xyz789"
            },
            "twitter": {
                "consumer_secret": "twitter_consumer_secret",
                "oauth_token": "twitter_oauth_token"
            }
        }
    },
    "public_info": {
        "company_name": "Tech Corp",
        "website": "https://techcorp.com",
        "support_email": "support@techcorp.com"
    }
}

redacter = DictFieldRedacter(
    ["secret", "password", "token", "username", "signature", "tx_frais_interbancaire", "pin_reedition_price"],
    maskWith="***REDACTED***"
)
import json
redacted_data = redacter.sanitize(test_data, mode="loose")

print(json.dumps(redacted_data, indent=4))
"""
