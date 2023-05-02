import hashlib
import hmac
import json
import logging
import os
import pathlib
import subprocess

# Create your views here.
from django.http import HttpRequest, HttpResponseForbidden, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from squidalytics.env_names import GITHUB_WEBHOOK_SECRET

SECRET = os.environ.get(GITHUB_WEBHOOK_SECRET)

logger = logging.getLogger(__name__)


def verify_signature(request: HttpRequest, secret: str) -> bool:
    signature = request.META.get("HTTP_X_HUB_SIGNATURE_256")
    if signature is None:
        return False

    try:
        sha_name, signature = signature.split("=")
    except ValueError:
        return False

    if sha_name != "sha256":
        return False

    mac = hmac.new(
        secret.encode("utf-8"), msg=request.body, digestmod=hashlib.sha256
    )
    expected_signature = mac.hexdigest()
    return hmac.compare_digest(expected_signature, signature)


@csrf_exempt
def handle_webhook(request: HttpRequest) -> JsonResponse:
    if not verify_signature(request, SECRET):
        return HttpResponseForbidden("Invalid signature")

    if request.method == "POST":
        payload = json.loads(request.body)
        ref = payload["ref"]
        logger.info(f"Received webhook for {ref}")

        if ref == "refs/heads/main":
            # Handle the main branch update
            script_path = (
                pathlib.Path(__file__).resolve().parent / "update_site.sh"
            )
            subprocess.run(["bash", str(script_path)])
            logger.info("Main branch updated")

        else:
            # Ignore updates to other branches
            logger.info("Ignoring branch update")
            pass

        return JsonResponse({"status": "success"})
    else:
        return JsonResponse(
            {"status": "failure", "message": "Invalid request method"}
        )
