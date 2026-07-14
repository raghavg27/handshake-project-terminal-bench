An Apache-style access log sits at /app/access.log in your working directory. Parse every request line and write a JSON summary to /app/report.json.

/app/report.json must be a single JSON object with exactly these keys:

- total_requests: integer — the total number of request lines in the log
- unique_ips: integer — the number of distinct client IP addresses
- top_path: string — the request path requested most often

The client IP is the first whitespace-separated field of each line; the request path is the path portion of the quoted request line (for example /index.html). Ignore blank lines.

Success criteria:

1. total_requests equals the total number of request lines in /app/access.log.
2. unique_ips equals the number of distinct client IP addresses.
3. top_path equals the request path that appears most frequently.