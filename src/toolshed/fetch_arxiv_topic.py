import requests
from typing import List


def fetch_arxiv_topic(query: str, max_results: int = 5, output_file: str = "arxiv_topics.md") -> None:
    """
    Fetches research topics from arXiv based on the provided query, formats them as Markdown,
    and saves the output to a .md file.

    Args:
        query (str): The search query string.
        max_results (int): The maximum number of results to retrieve.
        output_file (str): The name of the Markdown file to save the output.

    Returns:
        None
    """
    base_url = "http://export.arxiv.org/api/query"
    params = {
        "search_query": query,
        "start": 0,
        "max_results": max_results,
        "sortBy": "relevance",
        "sortOrder": "descending"
    }

    try:
        # Send GET request to arXiv API
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise exception for HTTP errors
        feed = response.text

        # Parse response
        entries = []
        for entry in feed.split("<entry>")[1:]:
            title_start = entry.find("<title>") + len("<title>")
            title_end = entry.find("</title>")
            summary_start = entry.find("<summary>") + len("<summary>")
            summary_end = entry.find("</summary>")
            link_start = entry.find("<id>") + len("<id>")
            link_end = entry.find("</id>")

            if title_start != -1 and title_end != -1:
                title = entry[title_start:title_end].strip()
                summary = entry[summary_start:summary_end].strip(
                ) if summary_start != -1 else "No summary available."
                link = entry[link_start:link_end].strip(
                ) if link_start != -1 else "No link available."
                entries.append(f"### [{title}]({link})\n\n{summary}\n")

        if not entries:
            md_output = f"# No research topics found for the query: **{query}**."
        else:
            # Format results into Markdown
            md_output = f"# Research Topics from arXiv for Query: **{query}**\n\n"
            md_output += "\n".join(entries)

        # Write Markdown to file
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(md_output)

        print(f"Research topics saved to {output_file}.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from arXiv: {e}")
