"""
Input validation utilities for domains and IP addresses.
Prevents invalid inputs before passing to scan modules.
"""

import re


def is_valid_domain(domain: str) -> bool:
    """
    Validate a domain name format.
    Domains can contain letters, numbers, hyphens, and dots.
    Example: example.com, sub.domain.co.uk
    """
    if not domain or len(domain) > 253:
        return False
    # Basic domain pattern: alphanumeric, hyphens, dots
    # Each label (part between dots) 1-63 chars
    domain_pattern = re.compile(
        r'^(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$'
    )
    # Also allow simple hostnames like "localhost"
    simple_pattern = re.compile(r'^[a-zA-Z0-9][a-zA-Z0-9\-\.]*[a-zA-Z0-9]$')
    return bool(domain_pattern.match(domain) or simple_pattern.match(domain))


def is_valid_ip(ip: str) -> bool:
    """
    Validate an IPv4 address format.
    IPv4: four octets, each 0-255 (e.g., 192.168.1.1)
    """
    if not ip:
        return False
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    try:
        return all(0 <= int(part) <= 255 for part in parts)
    except ValueError:
        return False


def is_valid_url(url: str) -> bool:
    """
    Validate a URL format (basic check for http/https).
    """
    if not url or len(url) > 2048:
        return False
    url_pattern = re.compile(
        r'^https?://'  # http or https
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain
        r'localhost|'  # localhost
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # or IP
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE
    )
    return bool(url_pattern.match(url))


def validate_target_for_scan(target: str, allow_url: bool = False) -> tuple[bool, str]:
    """
    Validate target for scanning. Returns (is_valid, error_message).
    If allow_url is True, also accept URLs for web-based scans.
    """
    target = target.strip()
    if not target:
        return False, "Target cannot be empty."

    if allow_url:
        if target.startswith(('http://', 'https://')):
            if is_valid_url(target):
                return True, ""
            return False, "Invalid URL format."
        # Fall through to domain/IP check for bare hostnames

    if is_valid_domain(target) or is_valid_ip(target):
        return True, ""

    if '/' in target or ':' in target:
        return False, "Invalid target. Use a domain (example.com) or IP (192.168.1.1)."

    return False, "Invalid domain or IP address format."
