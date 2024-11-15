from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class WebDriverFactory:
    """Factory class for creating WebDriver instances"""
    
    @staticmethod
    def create_driver(browser_type="chrome"):
        """
        Creates a WebDriver instance based on available browsers
        Args:
            browser_type: Optional specific browser to use ("chrome" or "edge")
        Returns:
            WebDriver instance
        """
        if browser_type == "chrome" or browser_type is None:
            try:
                service = ChromeService(ChromeDriverManager().install())
                return webdriver.Chrome(service=service)
            except Exception as e:
                if browser_type == "chrome":
                    raise Exception("Chrome browser initialization failed") from e
                
        if browser_type == "edge" or browser_type is None:
            try:
                service = EdgeService(EdgeChromiumDriverManager().install())
                return webdriver.Edge(service=service)
            except Exception as e:
                if browser_type == "edge":
                    raise Exception("Edge browser initialization failed") from e
                
        raise Exception("No compatible browser found")