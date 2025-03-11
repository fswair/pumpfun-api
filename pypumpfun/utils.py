import json
from typing import Mapping
import unittest
import requests

"""
API implementation of [pumpfun-scraper-api](https://rapidapi.com/domainfinderapi/api/pumpfun-scraper-api) for free and premium users.

Contact for inquiries about package from [contact@tomris.dev](mailto:contact@tomris.dev)
"""

import requests

class URL:
    def __init__(self, url: str):
        self.url = url.lstrip("/")
    def __truediv__(self, endpoint: str):
        return f"{self.url}/{endpoint.rstrip('/')}"

class _SafeResponse(Mapping):
    pass

class HTTPBase:
    base_url = URL("https://pumpfun-scraper-api.p.rapidapi.com")
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "pumpfun-scraper-api.p.rapidapi.com"
        }
        print("Get API access from here: https://rapidapi.com/domainfinderapi/api/pumpfun-scraper-api")
    
    def request(self, endpoint: str, params: dict = None):
        if "ping" in endpoint.lower():
            res = requests.get(self.base_url / endpoint, params=params, headers=self.headers)
            try:
                assert res.status_code == 200, \
                "Health check failed! "    \
                "Check your API KEY to avoid issues."
            except:
                raise
            finally:
                print("Get API access from here: https://rapidapi.com/domainfinderapi/api/pumpfun-scraper-api")
            return safe(res)
        return safe(requests.get(self.base_url / endpoint, params=params, headers=self.headers))
    
    @staticmethod
    def safe_response(response: requests.Response) -> _SafeResponse:
        try:
            return response.json()
        except json.JSONDecodeError as error:
            return {"content": response.text, "internal_error": error, "status_code": response.status_code}

safe = HTTPBase.safe_response

class Pumpfun(HTTPBase):
    """
    API endpoints of [pumpfun-scraper-api](https://rapidapi.com/domainfinderapi/api/pumpfun-scraper-api)
    """
    def __init__(self, api_key):
        super().__init__(api_key)
        self.ping()
        
    def ping(self):
        """
        Check whether API is alive and the API key is valid.

        This method performs a health check by sending a request to the ping endpoint.
        It will raise an assertion error if the API is not accessible or if the API key is invalid.

        Returns:
            dict: Response from the ping endpoint indicating API status

        Get API access from [pumpfun-scraper-api](https://rapidapi.com/domainfinderapi/api/pumpfun-scraper-api)
        """
        print("Health check was successful!")
        return self.request("ping")
    
    def search_tokens(self, term: str):
        """
        Search tokens by given term.

        Args:
            term (str): The search term to query tokens

        Returns:
            dict: Dictionary containing search results

        Get API access from [pumpfun-scraper-api](https://rapidapi.com/domainfinderapi/api/pumpfun-scraper-api)
        """
        params = {"term": term}
        return self.request("search_tokens", params=params)

    def tokens_for_you(self, limit: int = 50, offset: int = 0, include_nsfw: bool = False):
        """
        Get recommended tokens list.
        
        Args:
            limit (int, optional): Number of tokens to return. Defaults to 50.
            offset (int, optional): Pagination offset. Defaults to 0.
            include_nsfw (bool, optional): Include NSFW tokens. Defaults to False.
            
        Returns:
            dict: List of recommended tokens

        Get API access from [pumpfun-scraper-api](https://rapidapi.com/domainfinderapi/api/pumpfun-scraper-api)
        """
        params = {
            "limit": str(limit),
            "offset": str(offset),
            "include_nsfw": str(include_nsfw).lower()
        }
        return self.request("tokens_for_you", params=params)

    def similar_projects_by_mint(self, address: str, limit: int = 50):
        """
        Get similar projects based on a mint address.

        Args:
            address (str): The mint address to find similar projects
            limit (int, optional): Number of similar projects to return. Defaults to 50.

        Returns:
            dict: Dictionary containing similar projects

        Get API access from [pumpfun-scraper-api](https://rapidapi.com/domainfinderapi/api/pumpfun-scraper-api)
        """
        params = {
            "address": address,
            "limit": str(limit)
        }
        return self.request("similar_projects_by_mint", params=params)

    def get_featured_coins(self):
        """
        Get list of featured coins.

        Returns:
            dict: Dictionary containing featured coins information

        Get API access from [pumpfun-scraper-api](https://rapidapi.com/domainfinderapi/api/pumpfun-scraper-api)
        """
        return self.request("get_featured_coins")

    def get_about_graduates(self):
        """
        Get information about graduates.

        Returns:
            dict: Dictionary containing information about graduates

        Get API access from [pumpfun-scraper-api](https://rapidapi.com/domainfinderapi/api/pumpfun-scraper-api)
        """
        return self.request("get_about_graduates")

    def get_runner_tokens(self):
        """
        Get list of runner tokens.

        Returns:
            dict: Dictionary containing information about runner tokens

        Get API access from [pumpfun-scraper-api](https://rapidapi.com/domainfinderapi/api/pumpfun-scraper-api)
        """
        return self.request("get_runner_tokens")

    def get_tokens_by_meta(self, meta: str, include_nsfw: bool = False):
        """
        Get tokens by metadata search term.

        Args:
            meta (str): The metadata search term
            include_nsfw (bool, optional): Include NSFW tokens in results. Defaults to False.

        Returns:
            dict: Dictionary containing tokens matching the metadata search

        Get API access from [pumpfun-scraper-api](https://rapidapi.com/domainfinderapi/api/pumpfun-scraper-api)
        """
        params = {
            "meta": meta,
            "include_nsfw": str(include_nsfw).lower()
        }
        return self.request("get_tokens_by_meta", params=params)

    def get_token_metadata_trades(self, address: str):
        """
        Get token metadata and trade information for a specific address.

        Args:
            address (str): The token address to get metadata and trades for

        Returns:
            dict: Dictionary containing token metadata and trade information

        Get API access from [pumpfun-scraper-api](https://rapidapi.com/domainfinderapi/api/pumpfun-scraper-api)
        """
        params = {
            "address": address
        }
        return self.request("get_token_metadata_trades", params=params)

    def get_pumpfun_replies(self, address: str, limit: int = 1000, offset: int = 0):
        """
        Get replies for a specific address from Pumpfun.

        Args:
            address (str): The address to get replies for
            limit (int, optional): Number of replies to return. Defaults to 1000.
            offset (int, optional): Pagination offset. Defaults to 0.

        Returns:
            dict: Dictionary containing replies information

        Get API access from [pumpfun-scraper-api](https://rapidapi.com/domainfinderapi/api/pumpfun-scraper-api)
        """
        params = {
            "address": address,
            "limit": str(limit),
            "offset": str(offset)
        }
        return self.request("get_pumpfun_replies", params=params)

    def get_candlesticks(self, address: str, timeframe: int = 5, limit: int = 1000, offset: int = 0):
        """
        Get candlestick data for a specific token address.

        Args:
            address (str): The token address to get candlestick data for
            timeframe (int, optional): Timeframe in minutes for each candlestick. Defaults to 5.
            limit (int, optional): Number of candlesticks to return. Defaults to 1000.
            offset (int, optional): Pagination offset. Defaults to 0.

        Returns:
            dict: Dictionary containing candlestick data

        Get API access from [pumpfun-scraper-api](https://rapidapi.com/domainfinderapi/api/pumpfun-scraper-api)
        """
        params = {
            "address": address,
            "timeframe": str(timeframe),
            "limit": str(limit),
            "offset": str(offset)
        }
        return self.request("get_candlesticks", params=params)

    def get_king_hell(self, include_nsfw: bool = False):
        """
        Get King Hell token information.

        Args:
            include_nsfw (bool, optional): Include NSFW content in results. Defaults to False.

        Returns:
            dict: Dictionary containing King Hell token information

        Get API access from [pumpfun-scraper-api](https://rapidapi.com/domainfinderapi/api/pumpfun-scraper-api)
        """
        params = {
            "include_nsfw": str(include_nsfw).lower()
        }
        return self.request("get_king_hell", params=params)

    def global_params(self):
        """
        Get global parameters and statistics.

        Returns:
            dict: Dictionary containing global parameters and statistics

        Get API access from [pumpfun-scraper-api](https://rapidapi.com/domainfinderapi/api/pumpfun-scraper-api)
        """
        return self.request("global_params")

    def get_latest_token(self):
        """
        Get information about the latest token.

        Returns:
            dict: Dictionary containing information about the most recently added token

        Get API access from [pumpfun-scraper-api](https://rapidapi.com/domainfinderapi/api/pumpfun-scraper-api)
        """
        return self.request("get_latest_token")

class TestPumpfun(unittest.TestCase):
    """Test cases for Pumpfun API wrapper"""

    test_address = "FyuJ7S1fmDLsPe1Zr2VPtfDGdT9pdf1AXdRrFoawpump"
    
    @classmethod
    def setUpClass(cls):
        """Initialize API client with your API key"""
        cls.api = Pumpfun(input("Enter your API_KEY to test methods: "))  # API anahtarınızı buraya ekleyin
    
    def assert_status_200(self, response):
        """Helper method to check if response status is 200"""
        self.assertEqual(response.get("status_code", 200), 200)

    def test_ping(self):
        """Test ping endpoint"""
        response = self.api.ping()
        self.assert_status_200(response)

    def test_search_tokens(self):
        """Test search_tokens endpoint"""
        response = self.api.search_tokens(term="test")
        self.assert_status_200(response)

    def test_tokens_for_you(self):
        """Test tokens_for_you endpoint"""
        response = self.api.tokens_for_you(limit=10, offset=0, include_nsfw=False)
        self.assert_status_200(response)

    def test_similar_projects_by_mint(self):
        """Test similar_projects_by_mint endpoint"""
        response = self.api.similar_projects_by_mint(
            address=self.test_address, 
            limit=10
        )
        self.assert_status_200(response)

    def test_get_featured_coins(self):
        """Test get_featured_coins endpoint"""
        response = self.api.get_featured_coins()
        self.assert_status_200(response)

    def test_get_about_graduates(self):
        """Test get_about_graduates endpoint"""
        response = self.api.get_about_graduates()
        self.assert_status_200(response)

    def test_get_runner_tokens(self):
        """Test get_runner_tokens endpoint"""
        response = self.api.get_runner_tokens()
        self.assert_status_200(response)

    def test_get_tokens_by_meta(self):
        """Test get_tokens_by_meta endpoint"""
        response = self.api.get_tokens_by_meta(meta="test", include_nsfw=False)
        self.assert_status_200(response)

    def test_get_token_metadata_trades(self):
        """Test get_token_metadata_trades endpoint"""
        response = self.api.get_token_metadata_trades(
            address=self.test_address
        )
        self.assert_status_200(response)

    def test_get_pumpfun_replies(self):
        """Test get_pumpfun_replies endpoint"""
        response = self.api.get_pumpfun_replies(
            address=self.test_address, 
            limit=10, 
            offset=0
        )
        self.assert_status_200(response)

    def test_get_candlesticks(self):
        """Test get_candlesticks endpoint"""
        response = self.api.get_candlesticks(
            address=self.test_address,
            timeframe=5,
            limit=10,
            offset=0
        )
        self.assert_status_200(response)

    def test_get_king_hell(self):
        """Test get_king_hell endpoint"""
        response = self.api.get_king_hell(include_nsfw=False)
        self.assert_status_200(response)

    def test_global_params(self):
        """Test global_params endpoint"""
        response = self.api.global_params()
        self.assert_status_200(response)

    def test_get_latest_token(self):
        """Test get_latest_token endpoint"""
        response = self.api.get_latest_token()
        self.assert_status_200(response)

if __name__ == "__main__":
    unittest.main()