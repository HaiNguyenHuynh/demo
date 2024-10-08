"""
This module provides a function to load and configure SAML settings dynamically using environment
variables. The function reads a `settings.json` file and replaces certain fields with environment 
variable values. If environment variables are not set, default values are used.
"""

import os
import json


def load_saml_settings():
    """
    Loads SAML settings from a JSON file and replaces certain placeholders
    with values from environment variables.

    The function reads the SAML configuration from the "settings.json" file
    located in the "saml" directory, and then replaces specific fields with
    environment variables to allow dynamic configuration. If environment
    variables are not set, default values are used.

    Environment Variables:
    ----------------------
    SP_ENTITY_ID : str
        The entity ID for the service provider (SP).
    SP_ACS_URL : str
        The URL for the Assertion Consumer Service (ACS).
    SP_SLS_URL : str
        The URL for the Single Logout Service (SLS).
    SP_x509_CERT : str
        The x509 certificate for the service provider (SP).
    SP_PRIVATE_KEY : str
        The private key for the service provider (SP).
    IDP_ENTITY_ID : str
        The entity ID for the identity provider (IdP).
    IDP_SSO_URL : str
        The URL for the Identity Provider's Single Sign-On Service (SSO).
    IDP_SLO_URL : str
        The URL for the Identity Provider's Single Logout Service (SLO).
    IDP_CERT : str
        The x509 certificate for the Identity Provider.

    Returns:
    --------
    dict
        A dictionary containing the updated SAML settings with dynamic values
        from environment variables or default values if not provided.
    """

    # Load the settings JSON file with explicit encoding
    saml_settings_path = os.path.join(os.getcwd(), "saml", "settings.json")
    with open(saml_settings_path, "r", encoding="utf-8") as f:
        saml_settings = json.load(f)

    # Replace placeholder values with environment variables
    saml_settings["sp"]["entityId"] = os.getenv(
        "SP_ENTITY_ID", "http://localhost:5000/saml2/metadata/"
    )
    saml_settings["sp"]["assertionConsumerService"]["url"] = os.getenv(
        "SP_ACS_URL", "http://localhost:5000/saml2/acs/"
    )
    saml_settings["sp"]["singleLogoutService"]["url"] = os.getenv(
        "SP_SLS_URL", "http://localhost:5000/saml2/sls/"
    )
    saml_settings["sp"]["x509cert"] = os.getenv("SP_x509_CERT", "")
    saml_settings["sp"]["privateKey"] = os.getenv("SP_PRIVATE_KEY", "")
    saml_settings["idp"]["entityId"] = os.getenv(
        "IDP_ENTITY_ID", "https://idp.example.com/entity"
    )
    saml_settings["idp"]["singleSignOnService"]["url"] = os.getenv(
        "IDP_SSO_URL", "https://idp.example.com/sso"
    )
    saml_settings["idp"]["singleLogoutService"]["url"] = os.getenv(
        "IDP_SLO_URL", "https://idp.example.com/slo"
    )
    saml_settings["idp"]["x509cert"] = os.getenv("IDP_CERT", "")

    return saml_settings
