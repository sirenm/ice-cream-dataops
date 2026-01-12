import os
import sys

from pathlib import Path
from pprint import pprint

from cognite.client import CogniteClient, ClientConfig
from cognite.client.credentials import OAuthClientCredentials

# This is necessary to import adjacent modules in the function code.
sys.path.insert(0, str(Path(__file__).parent / "local_code"))

from local_code.handler import handle # noqa: E402


def main() -> None:
    credentials = OAuthClientCredentials(
        token_url="https://login.microsoftonline.com/16e3985b-ebe8-4e24-9da4-933e21a9fc81/oauth2/v2.0/token",
        client_id="a5a2e559-16b7-4161-a449-cd984b3134ff",
        client_secret=os.environ["ICAPI_EXTRACTORS_CLIENT_SECRET"],
        scopes=['https://westeurope-1.cognitedata.com/.default'],
    )

    client = CogniteClient(
        config=ClientConfig(
            client_name="CDF-Toolkit:0.6.53",
            project="cdf-bootcamp-50-test",
            base_url="https://westeurope-1.cognitedata.com",
            credentials=credentials,
        )
    )

    print("icapi_datapoints_extractor LOGS:")
    response = handle(
        client=client,
        data={'backfill': True, 'hours': 120},
    )

    print("icapi_datapoints_extractor RESPONSE:")
    pprint(response)


if __name__ == "__main__":
    main()
