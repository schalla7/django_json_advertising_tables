from django.core.management.base import BaseCommand
import requests
from advertplatform.models import Seller

class Command(BaseCommand):
    help = 'Updates seller data from JSON sources'

    def handle(self, *args, **options):
        urls = {
            'monumetric': 'http://monumetric.com/sellers.json',
            'mediavine': 'http://mediavine.com/sellers.json',
            'adthrive': 'http://cafemedia.com/sellers.json'
        }
        
        # Note:  without the following header, the server responds with 403, presumably because it thinks we're some scraper,
        #   so this header is like saying we're a human agent? Bloody agents!
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

        for platform, url in urls.items():
            print(f"Pulling latest sellers data from [{platform}]")
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                try:
                    data = response.json()['sellers']  # Access the 'sellers' key directly
                except (KeyError, ValueError):
                    self.stderr.write(f"Error processing JSON data from {url}")
                    continue
            else:
                self.stderr.write(f"Error fetching data from {url}: Status code {response.status_code}")
                continue

            for entry in data:
                if not Seller.objects.filter(domain=entry['domain'], ad_platform=platform).exists():
                    Seller.objects.create(
                        seller_id=entry['seller_id'],
                        name=entry['name'],
                        domain=entry['domain'],
                        seller_type=entry['seller_type'],
                        ad_platform=platform
                    )
