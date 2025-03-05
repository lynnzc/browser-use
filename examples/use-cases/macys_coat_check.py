from langchain_openai import ChatOpenAI
# Use local package
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from browser_use import Agent, Browser, BrowserConfig

from dotenv import load_dotenv
load_dotenv()

import asyncio

task = """
Visit the Macy's website and check if the Lauren Ralph Lauren Women's Faux Fur Hooded Puffer Coat is available in Black color and size XS.

Follow these steps:
1. Go to https://www.macys.com/shop/product/lauren-ralph-lauren-womens-faux-fur-hooded-puffer-coat?ID=18241291
2. Look for the color options and select "Black" color
3. After selecting the color, find and select size "XS" from the size options
4. Check if the "Add to Bag" button is enabled
5. If the "Add to Bag" button is enabled, click it to add the item to cart
6. Report back with:
   - Whether you were able to select the specific color and size
   - If the "Add to Bag" button was enabled
   - Whether adding to cart was successful
   - The current price of the item
   - Any discount information displayed
   - Any inventory/availability messages shown
"""

browser = Browser()

agent = Agent(
    task=task,
    llm=ChatOpenAI(model="gpt-4o"),
    browser=browser,
)

async def main():
    await agent.run()
    input("Press Enter to close the browser...")
    await browser.close()

if __name__ == '__main__':
    asyncio.run(main()) 