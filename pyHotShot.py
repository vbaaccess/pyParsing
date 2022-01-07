from dataclasses import dataclass
from typing import Set, Tuple
from bs4 import BeautifulSoup
import requests

@dataclass
class HotShot:
    promotion_name: str
    promotion_total_count: int
      
def get_hotshot_product_data() -> HotShot:
    """
    Function retrieving information about the transfer of the offer of the day.
    Example:
    >>> get_hotshot_product_data()
    HotShot(promotion_name='Telefon NoKia 3310', promotion_total_count=123)
    """
    url = "https://mobileapi.x-kom.pl/api/v1/xkom/hotShots/current?onlyHeader=true"
    j = requests.get(url, headers={'User-Agent': 'Mozilla/5.0', 'x-api-key': 'jfsTOgOL23CN2G8Y'}).json()

    return HotShot(j['PromotionName'], int(j['PromotionTotalCount']))
  
def get_matching_keywords(name: str, keywords: Set[str]) -> Set[str]:
    """
    Function that checks if any of the keywords are present in the given string.
    Example:
    >>> get_matching_keywords("ASUS TUF GAMING Z590-PLUS\xa0(Socket 1200)", {"Grafika", "GAMING", "ASUS"})
    {'ASUS'}
    """
    words = set(name.split(' '))

    matching_keywords = set()
    for k_lower in set([k.lower() for k in keywords]):
        for w_lower in set([w.lower() for w in words]):
            if k_lower in w_lower:
                matching_keywords.add(k_lower)

    return matching_keywords
  
def check_hotshot(keywords: Set[str]) -> Tuple[HotShot, Set[str]]:
    """
    Function that returns the name of the product and all its keywords contained in the product name.

    Example:
    >>> check_hotshot(keywords={'nokia'})
    (HotShot(promotion_name='Telefon NoKia 3310', promotion_total_count=45), {'nokia'})
    """

    hotshot = get_hotshot_product_data()
    matching_keywords = get_matching_keywords(hotshot.promotion_name, keywords)
    return hotshot, matching_keywords
