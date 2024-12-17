import requests
from concurrent.futures import ThreadPoolExecutor


class IntraNetFlowException(Exception):
    """Base exception for IntraNetFlow."""
    pass


class InvalidURLException(IntraNetFlowException):
    """Raised when an invalid URL is provided."""
    pass


class IntraNetFlow:
    """A lightweight HTTP client for intranet API requests with threading support."""

    @staticmethod
    def get(urls, **kwargs):
        if isinstance(urls, str):
            try:
                return requests.get(urls, **kwargs)
            except requests.exceptions.RequestException as e:
                raise IntraNetFlowException(f"GET request failed: {e}")
        elif isinstance(urls, list):
            with ThreadPoolExecutor() as executor:
                try:
                    return list(executor.map(lambda url: requests.get(url, **kwargs), urls))
                except requests.exceptions.RequestException as e:
                    raise IntraNetFlowException(f"GET request failed for one or more URLs: {e}")
        else:
            raise InvalidURLException("URLs must be a string or a list of strings.")

    @staticmethod
    def post(url, data=None, json=None, **kwargs):
        try:
            return requests.post(url, data=data, json=json, **kwargs)
        except requests.exceptions.RequestException as e:
            raise IntraNetFlowException(f"POST request failed: {e}")

    @staticmethod
    def threaded_post(urls, payloads, **kwargs):
        if not isinstance(urls, list) or not isinstance(payloads, list):
            raise InvalidURLException("URLs and payloads must both be lists.")
        if len(urls) != len(payloads):
            raise ValueError("URLs and payloads must have the same length.")

        with ThreadPoolExecutor() as executor:
            try:
                return list(
                    executor.map(
                        lambda args: requests.post(args[0], data=args[1], **kwargs),
                        zip(urls, payloads),
                    )
                )
            except requests.exceptions.RequestException as e:
                raise IntraNetFlowException(f"POST request failed for one or more URLs: {e}")
