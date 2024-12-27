# homelab
search engine / fediverse / k8s playground

## Search Engine
Define a basic scraper starting on some interesting urls and working to a given depth with blocked urls. Take all results and feed into an index like meilisearch. See if can scrape daily and have a reasonable index of high value content for personal use.

## tools
- https://github.com/linkchecker/linkchecker to crawl/find links
- https://github.com/philschmid/clipper.js to convert links to markdown (use bun maybe)
- https://www.meilisearch.com/docs/learn/self_hosted/getting_started_with_self_hosted_meilisearch to index markdown/url/attribs from linkchecker stats + md docs