import json


class ClientSecrets:
    filename = "client_secret.json"

    def get_value(key):
        try:
            with open(ClientSecrets.filename, "r") as file:
                data = json.load(file)
                return data["web"][key]
        except KeyError:
            print(f'Key {key} does not appear to exist!')
            return 0
        except IOError:
            print(f'File {ClientSecrets.filename} does not appear to exist!')
            return 0
    
    def __init__(self):
        self.client_id = ClientSecrets.get_value("project_id")
        self.auth_uri = ClientSecrets.get_value("auth_uri")
        self.token_uri = ClientSecrets.get_value("token_uri")
        self.auth_provider_x509_cert_url = ClientSecrets.get_value("auth_provider_x509_cert_url")
        self.client_secret = ClientSecrets.get_value("client_secret")
        self.redirect_uris = ClientSecrets.get_value("redirect_uris")
