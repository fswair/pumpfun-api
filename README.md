# Pumpfun API Wrapper

Python wrapper for [pumpfun-scraper-api](https://rapidapi.com/domainfinderapi/api/pumpfun-scraper-api)

## Installation

```bash
pip install pumpfun-api
```

## API Key Required

⚠️ **Important:** This module requires an API key to perform requests. Get your API key from [RapidAPI - Pumpfun Scraper API](https://rapidapi.com/domainfinderapi/api/pumpfun-scraper-api)

## Quick Start

```python
from pumpfun_api import Pumpfun

# Initialize with your API key
api = Pumpfun("YOUR_API_KEY")

# Search for tokens
results = api.search_tokens(term="your_search_term")
print(results)

# Get recommended tokens
tokens = api.tokens_for_you(limit=50, offset=0, include_nsfw=False)
print(tokens)
```

## Available Methods

- `ping()`: Check API health
- `search_tokens(term)`: Search tokens by term
- `tokens_for_you(limit=50, offset=0, include_nsfw=False)`: Get recommended tokens
- `similar_projects_by_mint(address, limit=50)`: Find similar projects
- `get_featured_coins()`: Get featured coins
- `get_about_graduates()`: Get graduates information
- `get_runner_tokens()`: Get runner tokens
- `get_tokens_by_meta(meta, include_nsfw=False)`: Search by metadata
- `get_token_metadata_trades(address)`: Get token metadata and trades
- `get_pumpfun_replies(address, limit=1000, offset=0)`: Get replies
- `get_candlesticks(address, timeframe=5, limit=1000, offset=0)`: Get candlestick data
- `get_king_hell(include_nsfw=False)`: Get King Hell information
- `global_params()`: Get global parameters
- `get_latest_token()`: Get latest token information

## Error Handling

The module includes built-in error handling and will return appropriate error messages if:
- API key is invalid
- API request fails
- Response parsing fails

## Rate Limits

Please be aware of the rate limits associated with your API key tier on RapidAPI.

## Support

For API access and pricing, visit [RapidAPI - Pumpfun Scraper API](https://rapidapi.com/domainfinderapi/api/pumpfun-scraper-api)

For package issues, contact: [contact@tomris.dev](mailto:contact@tomris.dev)
