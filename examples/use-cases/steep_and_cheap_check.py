from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser, BrowserConfig
from dotenv import load_dotenv
load_dotenv()

import asyncio

task = """
Visit the Steep and Cheap website and check if the Scott Kinabalu 2 Trail Running Shoe for women is available in Blush Pink/Dark Purple color and size 7.0.

Follow these steps:
1. Go to https://www.steepandcheap.com/scott-kinabalu-2-trail-running-shoe-womens
2. Look for the color options and select the "Blush Pink/Dark Purple" color
3. After selecting the color, find and select size "7.0" from the size options
4. Check if the "Add to Cart" button is enabled
5. If the "Add to Cart" button is enabled, click it to add the item to cart
6. Report back with:
   - Whether you were able to select the specific color and size
   - If the "Add to Cart" button was enabled
   - Whether adding to cart was successful
   - The current price of the item
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