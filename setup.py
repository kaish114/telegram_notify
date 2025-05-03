from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="telegram-notify",
    version="0.1.0",
    author="Mohammed Kaish Ansari",
    author_email="iiitu17131@gmail.com",
    description="A simple package for sending notifications via Telegram",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kaish114/TQTB.git",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "python-telegram-bot==13.7",
        "requests==2.26.0",
        "python-dotenv==1.1.0"
    ],
)