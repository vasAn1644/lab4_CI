from setuptools import setup

setup(
    name="my_chat_analyzer",
    version="0.1.0",
    description="A tool for analyzing chat data with AI integration",
    author="Hileta Yuliia",
    author_email="yuliia.hileta.pp.2022@lpnu.ua",  
    py_modules=["server"], 
    install_requires=[
        "flask>=2.0.0",
        "groq>=0.1.0",
        "python-dotenv>=0.19.0",
    ],
    package_data={
        "": ["static/css/*.css", "templates/*.html"],  
    },
    include_package_data=True,  
    entry_points={
        "console_scripts": [
            "chat-analyzer=server:main"  
        ]
    },
)