import os
from dotenv import load_dotenv

from docusign_esign import ApiClient, EnvelopesApi, EnvelopeDefinition, Document, Signer, SignHere, Recipients
from docusign_esign.client.api_exception import ApiException

from encode import encode_base64

load_dotenv()

# Configure API client
api_client = ApiClient()
api_client.set_base_path('https://demo.docusign.net/restapi')
api_client.set_default_header("Authorization", "Bearer " + os.getenv("ACCESS_TOKEN"))

envelopes_api = EnvelopesApi(api_client)

account_id = os.getenv("ACCOUNT_ID")


def createsend_contract(contracttext:str, emaillist ):
    # TODO : find the type of emaillist

    recipients_info = emaillist
    # recipients_info = [
    # {"email": "recipient1@example.com", "name": "Recipient One", "recipient_id": "1"},
    # {"email": "recipient2@example.com", "name": "Recipient Two", "recipient_id": "2"},
    # # Add more recipients as needed
    # ]

    # Create a document
    document = Document()
    contracttext = encode_base64(contracttext)
    document.document_base64 = contracttext
    document.name = "contract Document"  # Name of the document
    document.file_extension = "txt"      # Document extension
    document.document_id = "1"

    # Create signers and tabs
    signers = []
    for recipient in recipients_info:
        signer = Signer()
        signer.email = recipient["email"]
        signer.name = recipient["name"]
        signer.recipient_id = recipient["recipient_id"]
        signer.routing_order = str(int(recipient["recipient_id"]))  # Set routing order

        # where to sign
        sign_here = SignHere()
        sign_here.document_id = "1"
        sign_here.page_number = "1"
        sign_here.recipient_id = recipient["recipient_id"]
        sign_here.x_position = "100"  # X position for signature place
        sign_here.y_position = "150"  # Y position for signature place

        # Add the Sign Here tab to the signer
        tabs = Recipients()
        tabs.signers = [signer]
        signer.tabs = tabs

        signers.append(signer)

    # envelope definition
    envelope_definition = EnvelopeDefinition()
    envelope_definition.email_subject = "Please sign this document"
    envelope_definition.email_blurb = "This is a sample email blurb."
    envelope_definition.documents = [document]
    envelope_definition.recipients = Recipients(signers=signers)
    envelope_definition.status = "sent"  # Change to 'created' to save as draft

    try:
        # Send the envelope
        envelope_summary = envelopes_api.create_envelope(account_id, envelope_definition)
        return (f"Envelope has been sent. Envelope ID: {envelope_summary.envelope_id}")
    except ApiException as e:
        return (f"Exception when calling EnvelopesApi: {e}")