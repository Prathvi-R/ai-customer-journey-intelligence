from collections import deque


class CrawlState:
    """
    Maintains the runtime state of a crawl.

    Responsibilities:
    - Queue management
    - Tracking visited URLs
    - Tracking failed URLs
    """

    def __init__(self, start_url: str):
        self.queue = deque([start_url])
        self.visited: set[str] = set()
        self.failed: list[str] = []

    def has_next(self) -> bool:
        return len(self.queue) > 0

    def next_url(self) -> str:
        return self.queue.popleft()

    def mark_visited(self, url: str) -> None:
        self.visited.add(url)

    def mark_failed(self, url: str) -> None:
        self.failed.append(url)

    def enqueue(self, url: str) -> None:
        if url not in self.visited and url not in self.queue:
            self.queue.append(url)