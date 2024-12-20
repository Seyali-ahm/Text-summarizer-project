import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"
REPO_NAME = "Text-summarizer-project"
AUTHOR_USER_NAME = "Seyali-ahm"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "seyyedaliahmadi9@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,  # Corrected version
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,  # Corrected field name
    long_description_content_type="text/markdown",  # Corrected field name
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
