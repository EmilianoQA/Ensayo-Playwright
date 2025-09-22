import pytest
from playwright.sync_api import Page, expect

def test_homepage_title(page: Page) -> None:
    '''Test para verifcar el dahsboard principal'''
    page.goto("https://example.com/")
    expect(page).to_have_title("Example Domain")

def test_verificar_texto(page: Page) -> None:
    '''Test para verificar que el texto principal esté presente'''
    page.goto("https://example.com/")
    expect(page.locator("body > div:nth-child(1) > p:nth-child(2)")).to_contain_text("This domain is for use in illustrative examples in documents.")

def test_mas_info(page: Page) -> None:
    '''Test para verificar el enlace de más información'''
    page.goto("https://example.com/")
    page.locator("a[href='https://www.iana.org/domains/example']").click()  
    expect(page).to_have_url("https://www.iana.org/help/example-domains")

def test_verificar_texto(page: Page) -> None:
    '''Test para verificar el texto de la página de más información'''
    page.goto("https://example.com/")
    page.locator("a[href='https://www.iana.org/domains/example']").click() 
    expect(page).to_have_url("https://www.iana.org/help/example-domains")
    expect(page.locator("h1")).to_contain_text("Example Domains") 


