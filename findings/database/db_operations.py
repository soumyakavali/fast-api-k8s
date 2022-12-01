import os

from pymongo import MongoClient


class DBClient:
    def __init__(self) -> None:
        self.db_name = os.getenv("DB_NAME")
        self.db_collection = os.getenv("DB_COLLECTION")
        self.db_url =os.getenv("MONGO_DB_URL")
        self.db_tls_certfificatekeyfile = os.getenv("TLS_CERTIFICATEKEYFILE")
        self.tls_certificatekeyfile_password =os.getenv("TLS_CERTIFICATEKEYFILE_PASSWORD")
        self.tls_ca_certificatekeyfile=os.getenv("TLS_CA_CERTIFICATEKEYFILE")
        if os.getenv("LOCAL") == "Yes":
           self.db_client = MongoClient("mongodb://mongoadmin:secret@localhost:27888/?authSource=admin")
        else:
            self.db_client= MongoClient(self.db_url,
                            tls=True,
                            tlsCertificateKeyFile=self.db_tls_certfificatekeyfile,
                            tlsCertificateKeyFilePassword= self.tls_certificatekeyfile_password,
                            tlsCAFile= self.tls_ca_certificatekeyfile)
       