# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: sample_authenticate_async.py

DESCRIPTION:
    This sample demonstrates authenticating a client via:
        * api key
        * Azure Active Directory(AAD)

USAGE:
    python sample_authenticate.py

    Set the environment variables with your own values before running this sample:
    1) FACE_ENDPOINT - the endpoint to your Face resource.
    The environment variable below is used for api key authentication.
    2) FACE_KEY - your Face API key.
    The following environment variables are required for using azure-identity's DefaultAzureCredential.
    For more information, refer to https://aka.ms/azsdk/python/identity/docs#azure.identity.DefaultAzureCredential
    3) AZURE_TENANT_ID - the tenant ID in Azure Active Directory
    4) AZURE_CLIENT_ID - the application (client) ID registered in the AAD tenant
    5) AZURE_CLIENT_SECRET - the client secret for the registered application
"""

import asyncio

from dotenv import find_dotenv, load_dotenv

from samples._shared.helpers import get_face_api_endpoint, get_face_api_account_key


class FaceAuthentication():
    def __init__(self):
        load_dotenv(find_dotenv())
        self.endpoint = get_face_api_endpoint()
        self.key = get_face_api_account_key()

    async def authentication_by_api_key(self):
        print("Instantiate a FaceAdministrationClient using an api key")
        # [START authentication_by_api_key]
        from azure.core.credentials import AzureKeyCredential
        from azure.ai.vision.face.aio import FaceAdministrationClient

        async with FaceAdministrationClient(
                endpoint=self.endpoint, credential=AzureKeyCredential(self.key)) as face_admin_client:
            result = await face_admin_client.get_persons()

            print("List all persons' information in person directory:")
            for idx, person in enumerate(result):
                print(f"----- Person: #{idx+1} -----")
                print(f"Person id: {person.person_id}")
                print(f"name: {person.name}")
                print(f"user_data: {person.user_data}")
        # [END authentication_by_api_key]

    async def authentication_by_aad_credential(self):
        print("Instantiate a FaceAdministrationClient using a TokenCredential")
        # [START authentication_by_aad_credential]
        from azure.identity import DefaultAzureCredential
        from azure.ai.vision.face.aio import FaceAdministrationClient

        async with FaceAdministrationClient(
                endpoint=self.endpoint, credential=DefaultAzureCredential()) as face_admin_client:
            result = await face_admin_client.get_persons()

            print("List all persons' information in person directory:")
            for idx, person in enumerate(result):
                print(f"----- Person: #{idx+1} -----")
                print(f"Person id: {person.person_id}")
                print(f"name: {person.name}")
                print(f"user_data: {person.user_data}")
        # [END authentication_by_aad_credential]


async def main():
    sample = FaceAuthentication()
    await sample.authentication_by_api_key()
    await sample.authentication_by_aad_credential()


if __name__ == "__main__":
    asyncio.run(main())
