from setuptools import find_packages,setup

setup(
    name='mcqgenrator',
    version='0.0.1',
    author='pubudu lasith',
    author_email='pubudu093@gmail.com',
    install_requires=["langchain_openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)