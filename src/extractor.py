from scraper import fetch_page_content, parse_html, extract_email, extract_address, extract_contact_number, detect_cms, categorize_website

def extract_info(url):
    html = fetch_page_content(url)
    if html:
        soup = parse_html(html)
        
        email = extract_email(soup)
        address = extract_address(soup)
        contact_number = extract_contact_number(soup)
        language = soup.html.get('lang', 'N/A')
        cms_mvc = detect_cms(soup)
        
        return (url, email, address, contact_number, language, cms_mvc, )
    return None
