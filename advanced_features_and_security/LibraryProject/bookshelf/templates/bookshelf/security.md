# Security Measures Implemented

## HTTPS Enforcement
- All HTTP requests are redirected to HTTPS via `SECURE_SSL_REDIRECT=True`.
- HSTS enabled (`SECURE_HSTS_SECONDS=31536000`) with subdomain and preload options.

## Secure Cookies
- Session and CSRF cookies are transmitted only over HTTPS (`SESSION_COOKIE_SECURE=True`, `CSRF_COOKIE_SECURE=True`).

## Security Headers
- Clickjacking protection via `X_FRAME_OPTIONS='DENY'`.
- MIME type sniffing prevented (`SECURE_CONTENT_TYPE_NOSNIFF=True`).
- Browser XSS filter enabled (`SECURE_BROWSER_XSS_FILTER=True`).

## Deployment
- SSL/TLS certificates configured on web server (Nginx/Apache).
- All connections served securely via HTTPS.