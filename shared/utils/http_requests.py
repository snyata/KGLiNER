# Python code for making HTTP requests and returning XML content
import aiohttp
import asyncio
from xml.etree import ElementTree

async def fetch_arxiv_papers(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()
        
def parse_xml_response(xml_content):
    parsed_xml = ElementTree(xml_content)
    return parsed_xml